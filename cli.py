from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from core.engine import SecurityEngine
from core.logger import save_report
from core.risk import calculate_risk
from core.response_handler import respond

import modules.sqli as sqli
import modules.xss as xss
import modules.rate_limit as rate
import modules.path_traversal as pt
import modules.command_injection as cmd
import modules.bot_detection as bot

console = Console()

engine = SecurityEngine([
    sqli,
    xss,
    rate,
    pt,
    cmd,
    bot
])

# =========================
# UI
# =========================

def show_banner():
    console.print(Panel.fit(
        "[bold cyan]CYBERCHECK 🔐[/bold cyan]\n[white]Active Security Console[/white]",
        border_style="cyan"
    ))


def main_menu():
    while True:
        show_banner()

        console.print("[1] Monitor Traffic")
        console.print("[2] Run Scan")
        console.print("[3] Active Defense (Block)")
        console.print("[4] View Reports")
        console.print("[5] Exit\n")

        choice = input("Select an option > ")

        if choice == "1":
            monitor_mode()
        elif choice == "2":
            scan_mode()
        elif choice == "3":
            defense_mode()
        elif choice == "4":
            console.print("[yellow]Check generated JSON reports in project folder[/yellow]\n")
        elif choice == "5":
            break
        else:
            console.print("[red]Invalid option[/red]")


# =========================
# MODES
# =========================

def process_request(mode):
    report = []

    while True:
        data = input("Input (or 'exit') > ")

        if data.lower() == "exit":
            break

        request = {
            "ip": "127.0.0.1",
            "data": data,
            "agent": "cli"
        }

        findings = engine.inspect(request)

        if findings:
            table = Table(title="⚠️ Threat Detected")

            table.add_column("Type", style="red")
            table.add_column("Severity", style="yellow")

            for f in findings:
                table.add_row(f["type"], f["severity"])

            console.print(table)

            risk = calculate_risk(findings)

            console.print(f"[bold]Risk Score:[/bold] {risk}")

            respond(request, findings, mode, risk)

            report.append({
                "input": data,
                "findings": findings,
                "risk": risk,
                "mode": mode
            })

        else:
            console.print("[green]✔ No threats detected[/green]")

    file = save_report(report)
    console.print(f"[cyan]Report saved:[/cyan] {file}")


def monitor_mode():
    console.print("\n[bold yellow]MONITOR MODE[/bold yellow]\n")
    process_request("monitor")


def scan_mode():
    console.print("\n[bold blue]SCAN MODE[/bold blue]\n")
    process_request("allow")


def defense_mode():
    console.print("\n[bold red]ACTIVE DEFENSE MODE[/bold red]\n")
    process_request("block")


# =========================
# ENTRY POINT
# =========================

if __name__ == "__main__":
    main_menu()