using System;
using System.Data.SQLite;
using System.IO;

namespace NyxKernel {
    public static class RegistryManager {
        // Use a lock object for thread safety
        private static readonly object _dbLock = new object();
        private static readonly string dbPath = "Data Source=" + Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.UserProfile), ".nyx", "registry.db");

        static RegistryManager() {
            // Ensure schema exists on first access
            ExecuteNonQuery("CREATE TABLE IF NOT EXISTS skills (name TEXT, command_alias TEXT PRIMARY KEY, logic_block TEXT, source_agent TEXT, last_accessed DATETIME);");
        }

        public static void GraftSkill(string name, string alias, string logic, string source) {
            lock (_dbLock) {
                using (var conn = new SQLiteConnection(dbPath)) {
                    conn.Open();
                    string sql = "INSERT OR REPLACE INTO skills (name, command_alias, logic_block, source_agent, last_accessed) VALUES (@n, @a, @l, @s, CURRENT_TIMESTAMP)";
                    using (var cmd = new SQLiteCommand(sql, conn)) {
                        cmd.Parameters.AddWithValue("@n", name);
                        cmd.Parameters.AddWithValue("@a", alias);
                        cmd.Parameters.AddWithValue("@l", logic);
                        cmd.Parameters.AddWithValue("@s", source);
                        cmd.ExecuteNonQuery();
                    }
                }
            }
        }

        public static string GetSkillLogic(string alias) {
            lock (_dbLock) {
                using (var conn = new SQLiteConnection(dbPath)) {
                    conn.Open();
                    string sql = "SELECT logic_block FROM skills WHERE command_alias = @a";
                    using (var cmd = new SQLiteCommand(sql, conn)) {
                        cmd.Parameters.AddWithValue("@a", alias);
                        return cmd.ExecuteScalar()?.ToString();
                    }
                }
            }
        }

        private static void ExecuteNonQuery(string sql) {
            lock (_dbLock) {
                using (var conn = new SQLiteConnection(dbPath)) {
                    conn.Open();
                    new SQLiteCommand(sql, conn).ExecuteNonQuery();
                }
            }
        }
    }
}


