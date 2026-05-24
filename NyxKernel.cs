using System;
using System.IO;
using System.IO.Pipes;
using System.Threading.Tasks;

namespace NyxKernel {
    class Daemon {
        static async Task Main() {
            while (true) {
                var server = new NamedPipeServerStream("NyxPipe", PipeDirection.InOut, 1, PipeTransmissionMode.Byte, PipeOptions.Asynchronous);
                await server.WaitForConnectionAsync();
                _ = HandleRequest(server);
            }
        }

        static async Task HandleRequest(NamedPipeServerStream pipe) {
            using (var reader = new StreamReader(pipe))
            using (var writer = new StreamWriter(pipe) { AutoFlush = true }) {
                string request = await reader.ReadLineAsync();
                // Logic: Handle command or model switch
                await writer.WriteLineAsync($"[MODEL:ACTIVE] Ready");
            }
        }
    }
}
