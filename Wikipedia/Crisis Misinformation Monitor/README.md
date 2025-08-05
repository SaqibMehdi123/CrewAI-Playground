# Crisis Misinformation Monitor

A CrewAI-powered system for analyzing potential misinformation on user-specified topics during crisis situations. The system takes user input, searches relevant news articles, performs Wikipedia fact-checking, and generates comprehensive risk assessments.

## 🎯 Key Features

- **User-Driven Analysis**: Takes specific topics from users for targeted misinformation analysis
- **News Article Search**: Uses NewsAPI to find articles related to the user-specified topic
- **Wikipedia Fact-Checking**: Cross-references claims with Wikipedia for verification
- **Risk Assessment**: Classifies misinformation risk levels (Low/Medium/High)
- **Comprehensive Reporting**: Generates structured misinformation assessment reports

## Features

- **Topic-Specific Analysis**: Analyzes user-provided topics for potential misinformation
- **Real-time News Search**: Uses NewsAPI to fetch articles related to the specified topic
- **Wikipedia Verification**: Cross-references information with Wikipedia for accuracy
- **Risk Classification**: Assesses misinformation risk levels (Low/Medium/High)
- **Detailed Reporting**: Generates structured reports with evidence and recommendations

## Agents

1. **Crisis Query Listener Agent**: Monitors and searches for news articles related to the user-specified topic
2. **Research Agent**: Gathers comprehensive information from Wikipedia about the topic
3. **Fact Checker Agent**: Cross-verifies claims from news articles against Wikipedia data
4. **Risk Classifier Agent**: Assesses the risk level of identified misinformation
5. **Report Agent**: Generates final structured misinformation reports

## Setup

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Environment Variables**:
   - Copy `.env.example` to `.env`
   - Get a free NewsAPI key from [newsapi.org](https://newsapi.org/)
   - Add your NewsAPI key to the `.env` file

3. **Run the System**:
   ```bash
   cd crew
   python crisis_monitor_crew.py
   ```

## Usage

When you run the system, you'll be prompted to enter a topic to analyze:

```bash
Enter a topic to analyze for misinformation (or press Enter for default): 
```

### How it Works:
1. **User Input**: Enter a specific topic you want to analyze for misinformation
2. **News Search**: The system searches NewsAPI for articles related to your topic
3. **Wikipedia Research**: Gathers factual information about the topic from Wikipedia
4. **Fact-Checking**: Cross-verifies claims from news articles against Wikipedia data
5. **Risk Assessment**: Classifies the misinformation risk level
6. **Report Generation**: Creates a comprehensive analysis report

### Example Topics:
- "vaccine safety concerns"
- "climate change denial"
- "election fraud claims"
- "natural disaster response"
- "Pakistan flood 2025"

## How the Analysis Works

The system follows this workflow:
1. **Topic Input**: User provides a specific topic to investigate
2. **News Collection**: Searches for recent news articles about the topic
3. **Wikipedia Research**: Gathers verified information from Wikipedia
4. **Claim Verification**: Compares news claims against Wikipedia facts
5. **Risk Assessment**: Evaluates potential misinformation threats
6. **Report Generation**: Produces actionable recommendations

## Output

The system generates a structured report including:
- **Original Topic**: The user-specified topic that was analyzed
- **News Articles Found**: Articles from NewsAPI related to the topic
- **Wikipedia Research**: Factual information gathered from Wikipedia
- **Fact-Checking Results**: Verification status of claims (TRUE/FALSE/PARTIALLY TRUE)
- **Risk Assessment**: Classification of misinformation risk level
- **Recommendations**: Suggestions for public correction or further investigation

## Example Analysis

```
Topic: "Pakistan flood 2025 wipes out entire district"

Results:
- Verdict: UNSUBSTANTIATED
- Evidence: No Wikipedia or news evidence supports claim of entire district destruction
- Risk Level: MEDIUM
- Recommendation: Issue public clarification with accurate flood impact information
```
