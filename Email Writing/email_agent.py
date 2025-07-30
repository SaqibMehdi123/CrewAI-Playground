from crewai import LLM, Agent, Task, Crew
from dotenv import load_dotenv

load_dotenv()

llm = LLM(
    model='gemini/gemini-2.0-flash',
    temperature=0.1
)

email_assistant = Agent(
    role='Email Assistant Agent',
    goal='Improve emails and make them sound professional and clear',
    backstory='A highly experienced communication expert skilled in crafting professional emails.',
    verbose=True,
    llm=llm
)

original_email = """
Hey team, just wanted to tell you that the demo is kind of ready, but there's still stuff left.
Maybe we can show what we have and say the rest is WIP.
Let me know what you think. Thanks!
"""
# print("Original Email:", original_email)

email_task = Task(
    description=f"""'Improve the following rough email and rewrite it to sound more professional and polished 
    version.
    Expand abbreviations, use complete sentences, and ensure clarity and professionalism.
    Original Email: '''{original_email}'''
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
print(result)