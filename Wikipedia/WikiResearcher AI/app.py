# app.py (or main.py)
from crewai import Task, Crew
from wikipedia_agent import researcher_agent

# Define the task with clear instructions
research_task = Task(
    description=(
        'Research and gather comprehensive information about the topic: {topic}. '
        'Use Wikipedia to find detailed information including:\n'
        '1. Overview and definition\n'
        '2. Key features and characteristics\n' 
        '3. Applications and use cases\n'
        '4. Current developments\n'
        '5. Relevant examples or case studies\n'
        'Present the information in a well-structured format.'
    ),
    agent=researcher_agent,
    expected_output=(
        'A comprehensive research report about the topic with well-organized '
        'sections covering all key aspects found in Wikipedia sources.'
    )
)

# Create and configure the crew
research_crew = Crew(
    agents=[researcher_agent],
    tasks=[research_task],
    verbose=True,
    process='sequential'
)

# Execute the crew with the correct input parameter
if __name__ == "__main__":
    try:
        result = research_crew.kickoff(inputs={"topic": "Data Science"})
        print("\n" + "="*50)
        print("RESEARCH COMPLETED")
        print("="*50)
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please check your configuration and try again.")