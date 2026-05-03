class ReportAgent:
    def generate(self, tasks, risk):
        return {
            "summary": "Project risk detected",
            "risk": risk,
            "tasks": tasks
        }
