# 🚀 CrewAI-Brainstormer - Mobile App Ideas Generator with Design Thinking of IBM

![Design Thinking](https://img.shields.io/badge/Methodology-Design%20Thinking-blue)
![CrewAI](https://img.shields.io/badge/Framework-CrewAI-orange)
![Python](https://img.shields.io/badge/Language-Python%203.10+-green)

## 📋 Overview

CrewAI-Brainstormer is a powerful application that leverages the crewAI framework to automate the design thinking process, from IBM, and generate innovative mobile app ideas. The system simulates a collaborative team of AI agents, each with specialized roles, working through a structured design thinking methodology to create compelling product concepts with Hills statements.

CrewAI-Brainstormer autonomously creates innovative mobile app ideas by leveraging IBM's Enterprise Design Thinking toolkit with no user input required. The system generates random user personas, then simulates a complete design thinking workshop where AI agents collaborate through empathy mapping, scenario analysis, ideation, and solution refinement. The entire process - from random persona creation to final Hills statements - is handled by specialized AI agents working together to produce thoroughly researched mobile app concepts with clear value propositions.

Each generation process costs approximately $0.07 with Gemini 2.0 Flash.

## 🎯 Key Features

- **Multi-Agent Architecture**: Utilizes specialized AI agents (UX Designer, Product Manager, Business Strategist, etc.)
- **AI-Powered Design Thinking**: Automates the entire design thinking process from empathy mapping to solution design
- **Structured Workflow**: Sequential process with validation, challenges, and refinement at each stage
- **True Randomization**: Integrates with Random.org API for genuine randomization in persona creation
- **Parallel Execution**: Run multiple idea generation instances simultaneously
- **Comprehensive Outputs**: Generates complete reports with user personas, empathy maps, scenario maps, and Hills statements

## 🛠️ Requirements

- Python >=3.10 and <3.13
- [OpenRouter](https://openrouter.ai/) API key - A unified API that routes to various AI models including OpenAI, Anthropic, and others
- Random.org API key - Required for creating truly random user personas and preventing repetitive outputs

## 🚀 Getting Started

### Setup

1. Clone the repository:

   ```bash
   git clone git@github.com:Cyril-Deschamps/crewai-brainstormer.git
   cd crewai-brainstormer
   ```

2. Use the Makefile to initialize the project:

   ```bash
   make init
   ```

   This will install all required dependencies including crewAI and prepare the environment.

3. Configure your environment:
   - Copy `.env.example` to `.env`
   - Add your OpenRouter and Random.org API keys to the `.env` file

### Running the Application

To generate one idea:

```bash
make run
```

To run multiple generation processes in parallel:

```bash
make run i=3  # Runs 3 instances in parallel
```

### Viewing Results

To view all generated solution ideas and their Hills statements:

```bash
make solutions
```

## 🧠 How It Works

The CrewAI-Brainstormer follows the IBM Design Thinking methodology to create innovative solutions:

1. **Initialization**: Creates random personas with specific needs and problems
2. **Empathy Mapping**: Develops deep understanding of user needs through simulated interviews
3. **As-Is Scenario Mapping**: Documents current workflow and pain points
4. **To-Be Scenario Mapping**: Envisions an ideal future state
5. **Big Idea Vignettes**: Creates compelling narratives around the solution
6. **Hills Statements**: Defines the "Who-What-Wow" of the solution

Multiple AI agents collaborate through these stages with built-in challenges and verification steps to ensure quality.

## 📂 Project Structure

```
crewai-brainstormer/
├── src/
│   ├── config/
│   │   ├── agents.yaml  # Agent roles and personalities
│   │   └── tasks.yaml   # Task definitions and workflows
│   ├── CrewAIBrainstormer.py  # Main crewAI implementation
│   ├── main.py         # Entry point
│   ├── random_helper.py # Random.org integration and utilities
├── scripts/            # Utility scripts for project management
├── conversations/      # Output directory for reports
├── .env.example       # Example environment variables
├── Makefile           # Project automation
├── pyproject.toml     # Project metadata and dependencies
└── uv.lock            # Dependency lock file
```

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgements

- [crewAI](https://github.com/joaomdmoura/crewai) - The foundation of the multi-agent system framework
- [IBM Design Thinking](https://www.ibm.com/design/thinking/) - Methodology inspiration
- [Random.org](https://www.random.org/) - True randomization service
