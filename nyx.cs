using System;
using System.IO;
using System.IO.Pipes;

class NyxClient {
    static void Main(string[] args) {
        if (args.Length == 0) return;
        string command = string.Join(" ", args);
        
        try {
            using (var client = new NamedPipeClientStream(".", "NyxPipe", PipeDirection.InOut)) {
                client.Connect(500); // 500ms timeout
                using (var writer = new StreamWriter(client) { AutoFlush = true })
                using (var reader = new StreamReader(client)) {
                    writer.WriteLine(command);
                    Console.WriteLine(reader.ReadLine());
                }
            }
        } catch {
            Console.WriteLine("Error: Nyx Daemon is not running. Please start it.");
        }
    }
}
