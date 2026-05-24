using System;
using System.IO;
using System.IO.Pipes;
using System.Threading.Tasks;

namespace NyxKernel {
    class Daemon {
        static async Task Main() {
            Console.WriteLine("Nyx Sovereign Daemon [v8.1] Online.");
            while (true) {
                var server = new NamedPipeServerStream("NyxPipe", PipeDirection.InOut, 
                                                       NamedPipeServerStream.MaxAllowedServerInstances, 
                                                       PipeTransmissionMode.Byte, 
                                                       PipeOptions.Asynchronous);
                await server.WaitForConnectionAsync();
                _ = HandleClientAsync(server);
            }
        }

        static async Task HandleClientAsync(NamedPipeServerStream pipe) {
            using (pipe) {
                using (var reader = new StreamReader(pipe))
                using (var writer = new StreamWriter(pipe) { AutoFlush = true }) {
                    string command = await reader.ReadLineAsync();
                    string cachedLogic = RegistryManager.GetSkillLogic(command);
                    
                    string response = (cachedLogic != null) 
                        ? $"Executing Grafted Skill: {cachedLogic}" 
                        : $"Nyx Processed: {command}";
                    
                    await writer.WriteLineAsync(response);
                }
            }
        }
    }
}
