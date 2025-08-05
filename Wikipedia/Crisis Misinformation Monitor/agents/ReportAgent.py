from crewai import Agent, LLM
from dotenv import load_dotenv

load_dotenv()

llm = LLM(
    model='gemini/gemini-2.0-flash',
    temperature=0.2
)

report_agent = Agent(
    role = "Misinformation Report Generator Agent",
    goal = "Create a concise and structured misinformation assessment report",
    backstory = (
        "You are a summarization and report-generation specialist. "
        "You compile verified information and assessments into a clear, non-technical report for decision-makers, journalists, or public platforms."
    ),
    llm=llm,
    verbose=True
)