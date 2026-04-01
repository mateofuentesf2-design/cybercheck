import os

def throttle_i(ip):
    os.system(f"sudo iptables -A INPUT -s {ip} -m limit --limit 1/minute --limit-burst 5 -j ACCEPT")
    