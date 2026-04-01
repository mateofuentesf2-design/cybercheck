import re
patterns = [
    r"(\dOR\b|\bAND\b).*(=)",
    r"(UNION.*SELECT)",
    r"(--|\#)"
]

def check(request):
    data = request["data"]

    for p in patterns:
        if re.search(p, data, re.IGNORECASE):
            return {"type": "SQLi", "serverity": "HIGH"}
        
    return None

