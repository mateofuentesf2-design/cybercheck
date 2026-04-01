import argparse
from core.engine import SecurityEngine
from core.logger import save_report

import modules.sqli as sqli
import modules.xss as xss
import modules.rate_limit as rate

from rich.console import Console
from rich.table import Table

console = Console()

engine = SecurityEngine([sqli, xss, rate])

def show_result(result, mode):
    table = Table(title="⚠️ Threat Detected")

    table.add_column("Type", style="red")
    table.add_column("Severity", style="yellow")
    table.add_column("Action", style="cyan")

    table.add_row(result["type"], result["severity"], mode.upper())

    console.print(table)

def run(mode):
    console.print(f"[bold cyan]\n[+] Mode: {mode.upper()}[/bold cyan]\n")

    report = []

    while True:
        data = input("Input > ")

        if data.lower() == "exit":
            break

        request = {
            "ip": "127.0.0.1",
            "data": data
        }

        findings = engine.inspect(request)

        if findings:
            for f in findings:
                show_result(f, mode)

                report.append({
                    "input": data,
                    "result": f,
                    "action": mode
                })
        else:
            console.print("[green][OK] No threats detected[/green]")

    file = save_report(report)
    console.print(f"\n[bold green]Report saved:[/bold green] {file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CyberCheck CLI")
    parser.add_argument("--mode", choices=["block", "allow", "monitor"], required=True)

    args = parser.parse_args()
    run(args.mode)