from crewai import Agent, LLM
from dotenv import load_dotenv

load_dotenv()

llm = LLM(
    model='gemini/gemini-2.0-flash',
    temperature=0.2
)

risk_classifier_agent = Agent(
    role='Misinformation Risk Classifier Agent',
    goal='Classify the risk level of misinformation based on the provided data.',
    backstory=(
        'You are a specialist in threat assessment and content sensitivity. '
        'You analyze misinformation for its potential social impact, virality, and danger — especially in times of crisis or emergency.'
    ),
    llm=llm,
    verbose=True
)
