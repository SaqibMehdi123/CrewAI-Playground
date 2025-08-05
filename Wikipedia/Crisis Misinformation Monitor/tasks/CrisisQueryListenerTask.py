from crewai import Task
from agents.CrisisQueryListenerAgent import crisis_query_listener_agent

crisis_query_listener_task = Task(
    description = (
        "Listen for emerging crisis topics by analyzing the given topic: {topic}. "
        "Use NewsAPI to collect currently trending news articles related to this topic that appear to be unverified, sensational, or controversial. "
        "Flag potential misinformation candidates based on unusual frequency, clickbait, or conflicting headlines."
    ),
    agent=crisis_query_listener_agent,
    expected_output=(
        "A curated list of suspicious or high-risk crisis-related news articles with metadata (source, title, publication date). "
        "Flagged articles should include a rationale for their selection as potential misinformation candidates."
    )
)
