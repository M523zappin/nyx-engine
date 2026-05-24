using System;
using System.IO;
using System.IO.Pipes;
using System.Threading.Tasks;

namespace NyxKernel {
    class Daemon {
        static async Task Main() {
            Console.WriteLine("Nyx Sovereign Daemon [v8.1] Online.");
            while (true) {
                // Create a pipe instance for each connection
                var server = new NamedPipeServerStream("NyxPipe", PipeDirection.InOut, 
                                                       NamedPipeServerStream.MaxAllowedServerInstances, 
                                                       PipeTransmissionMode.Byte, 
                                                       PipeOptions.Asynchronous);
                
                await server.WaitForConnectionAsync();
                // Handle the client in a separate task so the server remains ready
                _ = HandleClientAsync(server);
            }
        }

        static async Task HandleClientAsync(NamedPipeServerStream pipe) {
            using (pipe) {
                try {
                    using (var reader = new StreamReader(pipe))
                    using (var writer = new StreamWriter(pipe) { AutoFlush = true }) {
                        string command = await reader.ReadLineAsync();
                        // TODO: Integrate SQLite Registry logic here
                        string response = $"Nyx Processed: {command}";
                        await writer.WriteLineAsync(response);
                    }
                } catch (Exception ex) {
                    Console.WriteLine($"Kernel Error: {ex.Message}");
                }
            }
        }
    }
}
