import subprocess
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.live import Live
from rich.table import Table

# --- KERNEL LOGIC ---
class NyxKernel:
    def __init__(self):
        self.version = "1.1.0-CAT"
        self.state = "OBSERVING"
        self.output_buffer = "Awaiting Directive..."

    def execute_directive(self, command):
        if not command.strip():
            return
        self.state = "POUNCING"
        try:
            result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
            self.output_buffer = result.decode()
        except subprocess.CalledProcessError as e:
            self.output_buffer = f"Error: {e.output.decode()}"
        self.state = "OBSERVING"

# --- INTERFACE DEFINITION ---
def make_layout() -> Layout:
    layout = Layout()
    layout.split_column(
        Layout(name="header", size=3),
        Layout(name="main", ratio=1),
        Layout(name="footer", size=3),
    )
    layout["main"].split_row(
        Layout(name="sidebar", ratio=1),
        Layout(name="body", ratio=3),
    )
    return layout

def update_ui(kernel: NyxKernel) -> Layout:
    layout = make_layout()
    
    # Header
    layout["header"].update(Panel(f"[bold cyan]⚡ NYX-CAT // KERNEL {kernel.version} // {kernel.state}[/bold cyan]"))
    
    # Sidebar
    table = Table(title="Whisker Protocol")
    table.add_column("Agent ID", style="magenta")
    table.add_column("Status")
    table.add_row("Core-01", "Active")
    layout["sidebar"].update(Panel(table, title="Agents"))
    
    # Body
    layout["body"].update(Panel(kernel.output_buffer, title="Execution Canvas"))
    
    # Footer
    layout["footer"].update(Panel("[bold cyan]tab[/bold cyan] agents | [bold cyan]ctrl+p[/bold cyan] commands | [bold cyan]ctrl+c[/bold cyan] exit", border_style="dim"))
    
    return layout

# --- MAIN EXECUTION LOOP ---
if __name__ == "__main__":
    kernel = NyxKernel()
    console = Console()

    with Live(update_ui(kernel), refresh_per_second=4, screen=True) as live:
        try:
            while True:
                # Refresh UI state
                live.update(update_ui(kernel))
                
                # Input must be handled carefully outside the Live display
                # We temporarily stop Live to take input
                live.stop()
                cmd = console.input("[bold green]NYX-CAT > [/bold green]")
                if cmd.lower() == "exit":
                    break
                kernel.execute_directive(cmd)
                live.start()
        except KeyboardInterrupt:
            pass
