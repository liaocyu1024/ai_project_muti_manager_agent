from app.agents.data_agent import DataAgent
from app.agents.task_agent import TaskAgent
from app.agents.risk_agent import RiskAgent
from app.agents.report_agent import ReportAgent

class Orchestrator:
    def __init__(self):
        self.data_agent = DataAgent()
        self.task_agent = TaskAgent()
        self.risk_agent = RiskAgent()
        self.report_agent = ReportAgent()

    def run_pipeline(self):
        data = self.data_agent.fetch()
        tasks = self.task_agent.process(data)
        risk = self.risk_agent.evaluate(tasks)
        report = self.report_agent.generate(tasks, risk)
        return report
