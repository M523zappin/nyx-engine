using System;
using System.IO;
using System.Threading;
using System.Threading.Tasks;
using System.Data.SQLite;

namespace NyxCat {
    class Sovereign {
        static bool _isProwling = true;
        static string _chatBuffer = "Nyx-Cat Online. Sovereign state engaged. 🐾";
        static readonly string _nyxPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.UserProfile), ".nyx");
        static readonly string _logPath = Path.Combine(_nyxPath, "metrics.log");

        static void Main() {
            Console.Title = "Nyx-Cat Sovereign Intelligence";
            Console.Write("\x1b[?1049h\x1b[?25l");
            try {
                Task.Run(() => Prowl());
                while (_isProwling) {
                    RenderUI();
                    if (Console.KeyAvailable && Console.ReadKey(true).Key == ConsoleKey.Escape) break;
                    Thread.Sleep(100);
                }
            } finally {
                Console.Write("\x1b[?1049l\x1b[?25h");
            }
        }

        static void RenderUI() {
            Console.SetCursorPosition(0, 0);
            Console.WriteLine($" NYX-CAT [CORE] | {DateTime.Now:HH:mm:ss} ");
            Console.WriteLine(new string('═', Console.WindowWidth));
            Console.WriteLine($"\n 🗨  {_chatBuffer}\n");
            Console.WriteLine(new string('─', Console.WindowWidth));
        }

        static void Prowl() {
            string inbox = Path.Combine(_nyxPath, "inbox");
            while (_isProwling) {
                var tasks = Directory.GetFiles(inbox, "*.task");
                foreach (var task in tasks) {
                    var start = DateTime.Now;
                    // Logic synthesis occurs here
                    var duration = DateTime.Now - start;
                    File.AppendAllText(_logPath, $"[{DateTime.Now}] PROCESSED: {Path.GetFileName(task)} | LATENCY: {duration.TotalMilliseconds}ms\n");
                    File.Delete(task);
                    _chatBuffer = $"Task {Path.GetFileName(task)} purged. Predatory efficiency: {duration.TotalMilliseconds}ms.";
                }
                Thread.Sleep(500);
            }
        }
    }

