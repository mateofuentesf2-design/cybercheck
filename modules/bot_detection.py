def check(request):
    user_agent = request.get("agent", "")

    suspicious = ["curl", "bot", "scammer"]

    for s in suspicious:
        if s in user_agent.lower():
            return {"type": "Bot Activity", "serverity": "MEDIUM"}
        
    return None