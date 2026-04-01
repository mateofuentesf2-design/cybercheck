from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/inspect")
async def inspect(req: Request):
    data = await req.json()

    findings = engine.inspect(data)
    risk = calculate_risk(findings)

    return {"findings": findings, "risk": risk}