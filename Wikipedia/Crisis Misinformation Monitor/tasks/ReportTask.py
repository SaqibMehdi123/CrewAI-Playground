from crewai import Task
from agents.ReportAgent import report_agent
from tasks.CrisisQueryListenerTask import crisis_query_listener_task
from tasks.ResearcherTask import researcher_task
from tasks.FactCheckerTask import fact_checker_task
from tasks.RiskClassifierTask import risk_classifier_task

report_task = Task(
    description = (
        "Based on inputs from the FactCheckerAgent, ResearchAgent, and ListenerAgent, generate a concise crisis misinformation report. "
        "Include:\n"
        "1. The original claim/topic\n"
        "2. Articles that triggered the check\n"
        "3. Verdict and justification\n"
        "4. Summary of verified information\n"
        "5. Suggestions for public correction or further investigation"
    ),
    context=[crisis_query_listener_task, researcher_task, fact_checker_task, risk_classifier_task],
    expected_output = (
        "A structured text report summarizing the claim, its credibility status, evidence, and recommendations for stakeholders."
    ),
    agent=report_agent
)