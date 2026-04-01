def calculate_risk(findings):
    weights = {"CRITICAL": 5, "HIGH": 3, "MEDIUM": 2, "LOW": 1}
    return sum(weights.get(f["severity"], 0) for f in findings)
