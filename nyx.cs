using System;
using System.IO;
using System.IO.Pipes;

class NyxClient {
    static void Main(string[] args) {
        if (args.Length == 0) {
            Console.WriteLine("Nyx: Awaiting command.");
            return;
        }

        string command = string.Join(" ", args);
        
        try {
            using (var client = new NamedPipeClientStream(".", "NyxPipe", PipeDirection.InOut)) {
                // Connect with a 1-second timeout to allow the daemon breathing room
                client.Connect(1000); 

                using (var writer = new StreamWriter(client) { AutoFlush = true })
                using (var reader = new StreamReader(client)) {
                    writer.WriteLine(command);
                    
                    // Read the daemon's response
                    string response = reader.ReadLine();
                    Console.WriteLine(response ?? "Nyx: No response received.");
                }
            }
        } catch (TimeoutException) {
            Console.WriteLine("Error: Nyx Daemon connection timed out. Is the kernel running?");
        } catch (IOException) {
            Console.WriteLine("Error: Pipe broken. The Daemon may have terminated unexpectedly.");
        } catch (Exception ex) {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }
}
