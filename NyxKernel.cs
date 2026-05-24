using System;
using System.IO;
using System.IO.Pipes;
using System.Threading;

namespace NyxKernel {
    class Daemon {
        static void Main() {
            Console.WriteLine("Nyx Daemon Initialized. Standing by...");
            // Start the IPC listener in a background thread
            Thread ipcThread = new Thread(ListenForCommands);
            ipcThread.IsBackground = true;
            ipcThread.Start();
            
            // Keep the daemon alive
            while (true) { Thread.Sleep(1000); }
        }

        static void ListenForCommands() {
            while (true) {
                using (var server = new NamedPipeServerStream("NyxPipe", PipeDirection.InOut)) {
                    server.WaitForConnection();
                    using (var reader = new StreamReader(server))
                    using (var writer = new StreamWriter(server) { AutoFlush = true }) {
                        string command = reader.ReadLine();
                        // Process command (e.g., query SQLite registry)
                        writer.WriteLine($"Nyx Executed: {command}");
                    }
                }
            }
        }
    }
}
