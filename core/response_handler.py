from rich.console import Console
from actions.firewall import block_ip
from actions.rate_control import throttle_ip

console = Console()

def respond(request, findings, mode, risk_score):
    ip = request.get("ip")

    for f in findings:
        console.print(f"[red]Threat:[/red] {f['type']} ({f['severity']})")

    if mode == "monitor":
        console.print("[yellow]Monitoring only[/yellow]")
        return

    if mode == "allow":
        console.print("[green]Allowed[/green]")
        return

    # modo block inteligente
    if risk_score >= 5:
        block_ip(ip)
        console.print(f"[bold red]IP BLOCKED: {ip}[/bold red]")
    elif risk_score >= 3:
        throttle_ip(ip)
        console.print(f"[yellow]Rate limited: {ip}[/yellow]")