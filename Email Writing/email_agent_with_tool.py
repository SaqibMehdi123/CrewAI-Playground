from crewai import LLM, Agent, Task, Crew
from dotenv import load_dotenv
from crewai.tools import BaseTool

load_dotenv()

llm = LLM(
    model='gemini/gemini-2.0-flash',
    temperature=0.5
)

original_email = """
looping in Priya. TAS  and PRX updates are in the deck. ETA for SDS integration is Friday.
Let's sync up tomorrow if SYBCBOT allows 😀. Ping me if any blockers.
"""

class ReplaceJargonTool(BaseTool):
    name: str = 'Replace Jargons'
    description: str = "Replace jargon or abbreviations with more specific terms or full forms."

    def _run(self, email: str) -> str:
        replacements = {
            'TAS': 'Technical Architecture Stack',
            'PRX': 'Project Review Exchange',
            'SDS': 'Smart Data Syncer',
            'SYBCBOT': 'Internal Standup Assistant Bot',
            'DBX': 'Client Database Exchange',
            'WIP': 'Work In Progress',
            'POC': 'Proof of Concept',
            'ping': 'reach out',
            'ETA': 'Estimated Time of Arrival',
        }
        
        suggestions = []
        email_lower = email.lower()
        for jargon, replacement in replacements.items():
            # email = email.replace(jargon, replacement)
            # email = email.replace(jargon.lower(), replacement)
            if jargon.lower() in email_lower:
                suggestions.append(f"Replace '{jargon}' with '{replacement}'")

        return '\n'.join(suggestions) if suggestions else 'No Jargon or Internal Abbreviations found.'
    

replace_jargon_tool = ReplaceJargonTool()


email_assistant = Agent(
    role='Email Assistant Agent',
    goal='Improve emails and make them sound professional and clear.',
    backstory='A highly experienced communication expert skilled in crafting professional emails.',
    tools=[replace_jargon_tool],
    verbose=True,
    llm=llm
)

email_task = Task(
    description=f"""'You are given an unpolished internal email.
        Your job is to rewrite it to make it sound professional, clear, and free of internal jargon.

        MANDATORY: Use the provided tool `Replace Jargons` to expand abbreviations and replace internal terms with full forms.
        Ensure that the final email is complete, grammatically correct, and suitable for external communication.

        Original Email:
        '''{original_email}'''
    """,
    agent=email_assistant,
    expected_output="A professional written email with proper formatting and content."
)

crew = Crew(
    agents=[email_assistant],
    tasks=[email_task],
    verbose=True
)

result = crew.kickoff()
# print(result)