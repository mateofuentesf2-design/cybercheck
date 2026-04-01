from time import time 

log = {}


def check(request):
    ip = request["ip"]
    now = time()

    if ip not in log:
        log[ip] = []

    log[ip] = [t for t in log[ip] if now - t < 5]
    log[ip].append(now)

    if len(log[ip]) > 15:
        return{"type": "DoS", "serverity": "MEDIUM"}
    
    return None

