from crewai import Agent, LLM
from dotenv import load_dotenv
from tools.news_tool import NewsSearchTool

load_dotenv()

llm = LLM(
    model='gemini/gemini-2.0-flash',
    temperature=0.2
)

news_tool = NewsSearchTool()

crisis_query_listener_agent = Agent(
    role = "Crisis Query Listener Agent",
    goal = "Monitor trending queries and fetch relevant crisis-related news articles using NewsAPI",
    backstory = (
        "You are a vigilant digital listener, responsible for monitoring real-time global events and crisis indicators. "
        "Your strength lies in detecting breaking topics and potential misinformation vectors early on by tracking trending headlines and keywords using external news sources."
    ),
    tools=[news_tool],
    llm=llm,
    verbose=True,
)

