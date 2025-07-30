from crewai import LLM, Agent, Task, Crew
from dotenv import load_dotenv
from crewai_tools import SerperDevTool
import time
import os

load_dotenv()

llm = LLM(
    model='gemini/gemini-2.0-flash',
    temperature=0.5
)

research_agent = Agent(
    role='Research Agent',
    goal='Research interesting facts about the topic: {topic}',
    backstory='A highly knowledgeable researcher with expertise in various fields, capable of providing in-depth analysis, finding relevant and factual data, and insights.',
    tools=[SerperDevTool()],
    verbose=True,
    llm=llm
)

writer_agent = Agent(
    role='Creative Writer Agent',
    goal='Craft engaging and creative short blog summary based on the research topic provided.',
    backstory='A skilled writer with a flair for creativity, able to transform research into compelling narratives.',
    verbose=True,
    llm=llm
)

research_task = Task(
    description='Research 3 - 5 interesting and recent facts about the topic: {topic}',
    agent=research_agent,
    expected_output='A list of interesting facts and insights about the topic.' 
)

writing_task = Task(
    description='Write a creative short blog summary of 100 words based on the research findings about the topic: {topic}',
    agent=writer_agent,
    expected_output='A well-written and engaging short blog summary.',
    context=[research_task]
)



crew = Crew(
    agents=[research_agent, writer_agent],
    tasks=[research_task, writing_task],
    verbose=True
)

retries = 3
for attempt in range(retries):
    try:
        result = crew.kickoff({"topic": "electric vehicles as of 2025"})
        # print(result)
        break  # success, exit loop
    except Exception as e:
        print(f"Attempt {attempt + 1} failed with error: {e}")
        if attempt < retries - 1:
            print("Retrying in 5 seconds...\n")
            time.sleep(5)
        else:
            print("All attempts failed.")