class SecurityEngine:
    def __init__(self, module):
        self.module = module

    def inspect (self, request):
        findings = []

        for module in self.modules:
            result = module.check(request)
            if result:
                findings.append(result)

        return findings