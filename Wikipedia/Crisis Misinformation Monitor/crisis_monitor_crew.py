import sys
import os
from pathlib import Path

# Add the Crisis Misinformation Monitor directory to the Python path
current_dir = Path(__file__).parent
project_dir = current_dir.parent
sys.path.append(str(project_dir))

from crewai import Crew
from agents.ResearchAgent import researcher_agent
from agents.ReportAgent import report_agent
from agents.FactCheckerAgent import fact_checker_agent
from agents.RiskClassifierAgent import risk_classifier_agent
from agents.CrisisQueryListenerAgent import crisis_query_listener_agent

from tasks.ResearcherTask import researcher_task
from tasks.ReportTask import report_task
from tasks.FactCheckerTask import fact_checker_task
from tasks.RiskClassifierTask import risk_classifier_task
from tasks.CrisisQueryListenerTask import crisis_query_listener_task

def run_crisis_monitor_crew(topic: str = "climate change misinformation"):
    """
    Run the Crisis Misinformation Monitor Crew with a specific topic
    
    Args:
        topic (str): The topic to analyze for misinformation
    """
    
    crisis_monitor_crew = Crew(
        agents=[
            crisis_query_listener_agent,
            researcher_agent,
            fact_checker_agent,
            risk_classifier_agent,
            report_agent
        ],
        tasks=[
            crisis_query_listener_task,
            researcher_task,
            fact_checker_task,
            risk_classifier_task,
            report_task
        ],
        verbose=True,
        process="sequential"  # Tasks will be executed in order
    )
    
    # Execute the crew with the provided topic
    result = crisis_monitor_crew.kickoff(inputs={"topic": topic})
    return result

if __name__ == "__main__":
    # Example usage - you can change the topic here
    topic = input("Enter a topic to analyze for misinformation (or press Enter for default): ").strip()
    if not topic:
        topic = "climate change misinformation"
    
    print(f"\n🔍 Starting Crisis Misinformation Monitor for topic: '{topic}'\n")
    result = run_crisis_monitor_crew(topic)
    print(f"\n✅ Analysis complete for topic: '{topic}'")