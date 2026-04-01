import argparse
from core.engine import SecurityEngine
from core.logger import save_report

import modules.sqli as sqli
import modules.xss as xss
import modules.rate_limit as rate
import modules.csrf as csrf
import modules.auth_bypass as auth
import modules.path_traversal as pt
import modules.command_injection as cmd
import modules.file_upload as upload
import modules.headers_security as headers
import modules.bot_detection as bot

import json

def load_rules():
    with open("config/rules.json") as f:
        return json.load(f)


from rich.console import Console
from rich.table import Table

console = Console()

engine = SecurityEngine([
    sqli, 
    xss, 
    rate,
    csrf,
    auth,
    pt,
    cmd,
    upload,
    headers,
    bot
    ])

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