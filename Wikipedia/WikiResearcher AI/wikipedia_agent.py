# wikipedia_agent.py
from crewai import Agent, LLM
from dotenv import load_dotenv
from custom_wikipedia_tool import WikipediaSearchTool

load_dotenv()

# Configure LLM
llm = LLM(
    model='gemini/gemini-2.0-flash',
    temperature=0.3
)

# Instantiate the tool
wikipedia_tool = WikipediaSearchTool()

# Create the agent with proper configuration
researcher_agent = Agent(
    role='Wikipedia Researcher Agent',
    goal='Fetch detailed and relevant information from Wikipedia about the topic: {topic}',
    backstory=(
        'You are a diligent researcher specializing in gathering accurate and '
        'comprehensive information from Wikipedia. You excel at finding relevant '
        'details and presenting them in a well-structured format.'
    ),
    tools=[wikipedia_tool],
    llm=llm,
    verbose=True,  # Enable verbose output for debugging
    allow_delegation=False  # Prevent delegation to other agents
)