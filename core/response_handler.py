from rich.console import Console

console = Console()

def handle(action, result):
    if action == "block":
        console.print(f"[bold red]BLOCKED:[/bold red] {result['type']}")
    elif action == "monitor":
        console.print(f"[yellow]MONITOR:[/yellow] {result['type']}")
    elif action == "allow":
        console.print(f"[green]ALLOWED[/green]")