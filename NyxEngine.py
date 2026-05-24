import os
import sys
from rich.console import Console
from rich.panel import Panel
from rich.columns import Columns

console = Console()

class NyxSentinel:
    """The Operational Guardian of the Sovereign Engine."""
    def __init__(self):
        self.active_agent = "Sovereign Core"
        self.system_state = "READY"
        self.iteration = 1.0

    def evaluate_directive(self, directive: str) -> bool:
        """Monitors inputs for critical evolutionary triggers or system escapes."""
        clean_directive = directive.strip().lower()
        
        if not clean_directive:
            return True # Continue waiting safely
            
        if "evolve" in clean_directive or "rewrite" in clean_directive:
            self.system_state = "MUTATING"
            self.trigger_evolution()
            return True
            
        if clean_directive in ["exit", "shutdown", "power down"]:
            self.system_state = "TERMINATING"
            return False # Break the loop safely
            
        # Standard execution path
        self.system_state = "EXECUTING"
        return True

    def trigger_evolution(self):
        """Placeholder for the core self-rewriting logic."""
        console.print("\n[bold yellow]⚡ [SENTINEL] CRITICAL MUTATION DETECTED // REWRITING RUNTIME CORE...[/bold yellow]")
        self.iteration += 0.1
        # Self-adaptation mechanics happen here
        self.system_state = "READY"

def render_ui(sentinel: NyxSentinel):
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Header Anchor
    console.print(f"[bold cyan]SYSTEM: {sentinel.system_state} // CORE: ZERO-DEPENDENCY // ADAPTATION: ENGAGED[/bold cyan]\n")
    
    # Center Contextual Terminal Panel
    center_content = (
        f"\n[bold magenta]⚡ NYX-CAT // SOVEREIGN ENGINE DEPLOYMENT v{sentinel.iteration:.1f}[/bold magenta]\n\n"
        "[dim white]Ask anything... \"Extract skills from connected a2a agents\"[/dim white]\n"
    )
    console.print(Panel(center_content, border_style="bright_blue", expand=False, align="center"))
    
    print("\n" * 2)
    
    # Bilateral Metadata Footer
    meta_left = f"[bold green]Engine ·[/bold green] {sentinel.active_agent}\n[bold green]Status ·[/bold green] Awaiting Directive..."
    meta_right = "[bold cyan]tab[/bold cyan] agents\n[bold cyan]ctrl+p[/bold cyan] commands"
    console.print(Columns([meta_left, meta_right], justify="space-between"))
    print("\n")

def main():
    sentinel = NyxSentinel()
    running = True
    
    while running:
        render_ui(sentinel)
        try:
            directive = input(" > DIRECTIVE: ")
            running = sentinel.evaluate_directive(directive)
        except KeyboardInterrupt:
            # Sentinel catches manual cancellations gracefully
            console.print("\n[bold red]⚡ [SENTINEL] INTERRUPT DETECTED. HOLDING CORE STABILITY.[/bold red]")
            break

if __name__ == "__main__":
    main()
