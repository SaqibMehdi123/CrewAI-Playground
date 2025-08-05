# Crisis Misinformation Monitor

A CrewAI-powered autonomous system for monitoring and analyzing potential misinformation during crisis situations. The system proactively scans trending news, performs Wikipedia fact-checking, and generates risk assessments without waiting for user input.

## 🤖 Autonomous Features

- **Proactive News Monitoring**: Automatically scans trending headlines and breaking news
- **Crisis Detection**: Monitors crisis-related keywords (disasters, emergencies, health scares)
- **Real-time Analysis**: Continuously analyzes news patterns for misinformation indicators
- **Autonomous Operation**: Works independently or can focus on specific topics

## Features

- **Real-time News Monitoring**: Uses NewsAPI to fetch trending crisis-related articles
- **Wikipedia Fact-Checking**: Cross-references claims with Wikipedia for verification
- **Risk Assessment**: Classifies misinformation risk levels (Low/Medium/High)
- **Comprehensive Reporting**: Generates structured misinformation assessment reports
- **Pattern Detection**: Identifies conflicting information and suspicious patterns

## Agents

1. **Crisis Query Listener Agent**: Autonomously monitors trending news and detects crisis-related misinformation
2. **Research Agent**: Gathers comprehensive information from Wikipedia
3. **Fact Checker Agent**: Cross-verifies claims from news and Wikipedia data
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

The system now operates in two modes:

### 1. Autonomous Monitoring Mode (Default)
```bash
cd crew
python crisis_monitor_crew.py
```
Choose option 1 for autonomous monitoring. The system will:
- Automatically scan trending headlines from major news sources
- Monitor crisis-related keywords (disasters, emergencies, health scares, etc.)
- Detect potential misinformation patterns without user input
- Generate comprehensive monitoring reports

### 2. Focused Topic Mode
Choose option 2 and specify a topic. The system will focus its monitoring on that specific area while still performing general scans.

## Monitoring Keywords

The system automatically monitors these crisis-related categories:
- **Breaking News**: Emergency situations, disasters
- **Health Crises**: Pandemics, outbreaks, medical misinformation
- **Natural Disasters**: Earthquakes, floods, hurricanes, wildfires
- **Security Events**: Terrorism, accidents, evacuations
- **Misinformation Patterns**: Fake news, conspiracy theories, viral hoaxes

## Example Output

The autonomous monitoring generates reports including:
- Current trending headlines with misinformation risk assessment
- Crisis-related articles flagged for fact-checking
- Pattern analysis of conflicting information
- Prioritized recommendations for immediate attention

## Output

The system generates a structured report including:
- Original claims/topics analyzed
- Articles that triggered the analysis
- Fact-checking verdict and justification
- Risk assessment and recommendations
- Suggestions for public correction or further investigation
