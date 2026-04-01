import json
from datetime import datetime

def save_report(data, risk):
    report = {
        "summary": {
            "total_events": len(data),
            "risk_score": risk
        },
        "events": data
    }

