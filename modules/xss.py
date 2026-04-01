import re

patterns = [
    r"<script.*?>",
    r"javascript:",
    r"onerror="
]

def check(request):
    data = request["data"]

    for p in patterns:
        if re.search(p, data, re.IGNORECASE):
            return {"type": "XSS", "serverity": "HIGH"}
        
    return None
