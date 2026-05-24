using System;
using System.IO.Pipes;
using System.IO;

class NyxClient {
    static string[] models = { "Nyx-Core", "Nyx-Science", "Nyx-Quantum" };
    static int selectedModel = 0;
    static bool showMenu = false;

    static void Main() {
        Console.Write("\x1b[?1049h\x1b[?25l"); // App Mode
        Console.Clear();
        
        while (true) {
            RenderUI();
            var key = Console.ReadKey(true);
            if (key.Key == ConsoleKey.F1) showMenu = !showMenu;
            if (showMenu && key.Key == ConsoleKey.DownArrow) selectedModel = (selectedModel + 1) % models.Length;
            if (key.Key == ConsoleKey.Escape) break;
        }
        Console.Write("\x1b[?1049l\x1b[?25h");
    }

    static void RenderUI() {
        Console.SetCursorPosition(0, 0);
        Console.WriteLine(" Nyx Sovereign Intelligence | [F1] Models ");
        Console.WriteLine("──────────────────────────────────────────");
        if (showMenu) {
            for (int i = 0; i < models.Length; i++)
                Console.WriteLine(i == selectedModel ? $"> {models[i]} <" : $"  {models[i]}  ");
        }
    }
}
