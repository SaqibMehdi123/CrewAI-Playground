from crewai import Task
from tasks.CrisisQueryListenerTask import crisis_query_listener_task
from agents.RiskClassifierAgent import risk_classifier_agent
from tasks.FactCheckerTask import fact_checker_task

risk_classifier_task = Task(
    description = (
        "Analyze the false or misleading claims reported by the FactCheckerAgent. "
        "Classify the risk level (Low, Medium, High) based on criteria like potential for panic, health harm, political instability, or public safety concerns. "
        "Provide brief justification and recommend mitigation urgency."
    ),
    agent=risk_classifier_agent,
    context=[crisis_query_listener_task, fact_checker_task],
    expected_output = (
        "A risk classification tag (LOW / MEDIUM / HIGH) with 2-3 sentences explaining the rationale and recommended response urgency."
    )
)