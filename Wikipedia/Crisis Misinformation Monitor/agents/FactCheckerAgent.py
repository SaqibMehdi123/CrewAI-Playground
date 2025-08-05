from crewai import Agent, LLM
from dotenv import load_dotenv
from tools.WikipediaSearchTool import WikipediaSearchTool

load_dotenv()

llm = LLM(
    model='gemini/gemini-2.0-flash',
    temperature=0.2
)

wiki_tool = WikipediaSearchTool()

fact_checker_agent = Agent(
    role='Fact Validator Agent',
    goal='Cross-verify claims from the news and Wikipedia data to detect misinformation',
    backstory=(
        "You are a critical thinker and fact-checking specialist trained to detect inconsistencies between trending claims and verified factual content. "
        "You analyze controversial or trending statements and judge their truthfulness using known trusted sources."
    ),
    tools=[wiki_tool],
    llm=llm,
    verbose=True
)
