from crewai import Task
from agents.FactCheckerAgent import fact_checker_agent
from tasks.CrisisQueryListenerTask import crisis_query_listener_task
from tasks.ResearcherTask import researcher_task

fact_checker_task = Task(
    description=(
        'Given information from Wikipedia and news articles, extract factual claims and verify them. '
        'Compare claims with the Wikipedia research report and NewsAPI article results. '
        'Use comparison logic like:\n'
        '- Conflicting dates or events\n'
        '- Differing statistics\n'
        '- Unsupported claims in news articles\n'
        'Determine if each claim is: TRUE, FALSE, or PARTIALLY TRUE. '
        'Highlight any inconsistencies or lack of evidence with brief justifications.'
    ),
    agent=fact_checker_agent,
    context=[crisis_query_listener_task, researcher_task],
    expected_output=(
        'A table of claims with their verification status (TRUE/FALSE/PARTIALLY TRUE) and justification notes. '
        'Include conflicting points and quote supporting/rejecting evidence from the research.'
    )
)
