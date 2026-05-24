using System;
using System.IO.Pipes;
using System.IO;

class NyxClient {
    static void Main(string[] args) {
        // 1049: Enter Alternate Screen Buffer (Clear shell history, start fresh)
        Console.Write("\x1b[?1049h"); 
        
        try {
            using (var client = new NamedPipeClientStream(".", "NyxPipe", PipeDirection.InOut)) {
                client.Connect(1000);
                using (var writer = new StreamWriter(client) { AutoFlush = true })
                using (var reader = new StreamReader(client)) {
                    // Start an infinite loop to keep the UI alive
                    while (true) {
                        string input = Console.ReadLine();
                        writer.WriteLine(input);
                        string response = reader.ReadLine();
                        // Redraw only the dynamic area of the screen
                        UpdateUI(response);
                    }
                }
            }
        } finally {
            // 1049l: Exit Alternate Screen Buffer (Restore original shell)
            Console.Write("\x1b[?1049l");
        }
    }

    static void UpdateUI(string content) {
        Console.SetCursorPosition(0, 5); // Lock UI to a specific vertical area
        Console.WriteLine($"[Nyx Kernel]: {content}");
    }
}
