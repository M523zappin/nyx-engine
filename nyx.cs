using System;
using System.IO.Pipes;
using System.IO;

class NyxClient {
    static void Main() {
        Console.Clear();
        // Enter Alternate Screen Buffer for a "Sovereign" app look
        Console.Write("\x1b[?1049h");
        
        try {
            using (var client = new NamedPipeClientStream(".", "NyxPipe", PipeDirection.InOut)) {
                client.Connect(1000);
                using (var writer = new StreamWriter(client) { AutoFlush = true })
                using (var reader = new StreamReader(client)) {
                    
                    Console.WriteLine("--- Nyx Sovereign Chat [Connected] ---");
                    
                    while (true) {
                        Console.Write("\nNyx > ");
                        string input = Console.ReadLine();
                        if (input == "exit") break;

                        writer.WriteLine(input);
                        string response = reader.ReadLine();
                        
                        // Structured UI output
                        Console.ForegroundColor = ConsoleColor.Cyan;
                        Console.WriteLine($"[Kernel]: {response}");
                        Console.ResetColor();
                    }
                }
            }
        } finally {
            Console.Write("\x1b[?1049l"); // Exit buffer
        }
    }
}
