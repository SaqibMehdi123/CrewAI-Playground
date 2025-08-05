from crewai import Task
from agents.ResearchAgent import researcher_agent
from tasks.CrisisQueryListenerTask import crisis_query_listener_task

researcher_task = Task(
    description = (
        "Research and gather comprehensive information about the topic: {topic}. "
        "Use Wikipedia to find detailed information including:\n"
        "1. Overview and definition\n"
        "2. Key features and characteristics\n" 
        "3. Historical or recent developments\n"
        "4. Expert consensus or citations\n"
        "5. Contradictions or warnings\n"
        "Present the information in a clean, bullet-pointed format."
    ),
    agent=researcher_agent,
    context=[crisis_query_listener_task],
    expected_output = (
        "A Wikipedia-based research report about the topic with organized sections covering all key aspects."
    )
)