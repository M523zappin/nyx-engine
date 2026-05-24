using System;
using System.IO;
using System.Data.SQLite;

namespace NyxKernel {
    public static class RegistryManager {
        private static readonly string dbPath = "Data Source=" + Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.UserProfile), ".nyx", "registry.db");

        public static void GraftSkill(string name, string alias, string logic, string source) {
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

        public static string GetSkillLogic(string alias) {
            using (var conn = new SQLiteConnection(dbPath)) {
                conn.Open();
                string sql = "SELECT logic_block FROM skills WHERE command_alias = @a";
                using (var cmd = new SQLiteCommand(sql, conn)) {
                    cmd.Parameters.AddWithValue("@a", alias);
                    object result = cmd.ExecuteScalar();
                    return result?.ToString();
                }
            }
        }
    }
}
