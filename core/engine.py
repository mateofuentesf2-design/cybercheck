class SecurityEngine:
    def __init__(self, modules):
        self.modules = modules
    
    def inspect(self, request):
        findings = []

        for module in self.modules:
            try:
                result = module.check(request)

                if result:
                    findings.append(result)
            except Exception:
                continue

        return findings
    