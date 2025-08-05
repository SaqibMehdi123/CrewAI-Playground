from crewai import Agent, LLM
from dotenv import load_dotenv
from tools.WikipediaSearchTool import WikipediaSearchTool
from tools.news_tool import NewsSearchTool

load_dotenv()

llm = LLM(
    model='gemini/gemini-2.0-flash',
    temperature=0.2
)

wiki_tool = WikipediaSearchTool()
news_tool = NewsSearchTool()

researcher_agent=Agent(
    role = "Wikipedia Researcher Agent",
    goal = "Fetch detailed and relevant information from Wikipedia about the topic: {topic}",
    backstory = (
        "You are a diligent researcher specializing in gathering accurate and comprehensive information from Wikipedia. "
        "You excel at finding relevant details and presenting them in a well-structured format to support factual claims."
    ),
    tools=[wiki_tool, news_tool],
    llm=llm,
    verbose=True
)