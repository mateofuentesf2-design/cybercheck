import re

patterns = [
    r";\s*ls",
    r";\s*cat",
    r";\s*whoami",
]

def check(request):
    data = request["data"]

    for p in patterns:
        if re.search(p, data, re.IGNORECASE):
            return {"type": "Command Injection", "serverity": "CRITICAL"}
        
    return None