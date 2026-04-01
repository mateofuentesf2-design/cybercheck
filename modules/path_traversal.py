import re

patterns = [
    r"\.\./",
    r"\.\.\\",
    r"/etc/passwd"
]

def check(request):
    data = request["data"]

    for p in patterns:
        if re.search(p, data):
            return {"type": "Path Traversal", "serverity": "HIGH"}
        
    return None

