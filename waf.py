from fastaip import FastAPI, request
from core.engine import SecurityEngine
from core.risk import calculate_risk
from core.response_handler import respond

import modules.sqli as sqli
import modules.xss as xss
import modules.rate_limit as rate
import modules.path_traversal as pt
import modules.command_injection as cmd
import modules.bot_detection as bot

app = FastAPI()

engine = SecurityEngine([
    sqli,
    xss,
    rate,
    pt,
    cmd,
    bot
])

@app.middleware("http")
async def waf_middleware(request: Request, call_next):
    
    body = await request.body()

    req_data = {
        "ip": request.client.host,
        "data": body.decode("utf-8", errors="ignore"),
        "agent": request.headers.get("User-Agent", "")
    }

    findings = engine.inspect(req_data)
    risk_score = calculate_risk(findings)

    #logica del bloque real

    if risk >=5:
        return {"error": "Blocked by CyberCheck WAF"}
    
    response = await call_next(request)
    return response

@app.get("/")
def home():
    return {"status": "CyberCheck WAF Running"}