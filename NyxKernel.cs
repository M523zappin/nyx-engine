using System;
using System.IO;
using System.IO.Pipes;
using System.Threading.Tasks;

namespace NyxKernel 
{
    class Daemon 
    {
        static async Task Main() 
        {
            Console.WriteLine("Nyx Sovereign Daemon [v8.1] Online.");
            
            // The daemon loop remains persistent, awaiting client connections
            while (true) 
            {
                var server = new NamedPipeServerStream(
                    "NyxPipe", 
                    PipeDirection.InOut, 
                    NamedPipeServerStream.MaxAllowedServerInstances, 
                    PipeTransmissionMode.Byte, 
                    PipeOptions.Asynchronous
                );

                await server.WaitForConnectionAsync();
                
                // Fire-and-forget task to handle client communication
                _ = HandleClientAsync(server);
            }
        }

        static async Task HandleClientAsync(NamedPipeServerStream pipe) 
        {
            using (pipe) 
            {
                try 
                {
                    using (var reader = new StreamReader(pipe))
                    using (var writer = new StreamWriter(pipe) { AutoFlush = true }) 
                    {
                        string command = await reader.ReadLineAsync();
                        
                        if (string.IsNullOrWhiteSpace(command)) return;

                        // Intelligence Layer: Query the registry for Grafted Skills
                        string cachedLogic = RegistryManager.GetSkillLogic(command);
                        
                        string response = (cachedLogic != null) 
                            ? $"[SKILL EXECUTED] {cachedLogic}" 
                            : $"[SYSTEM] Nyx processed command: {command}";
                        
                        await writer.WriteLineAsync(response);
                    }
                }
                catch (Exception ex) 
                {
                    Console.WriteLine($"[KERNEL ERROR]: {ex.Message}");
                }
            }
        }
    }
}
