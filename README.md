# 🚀 IdeaGenerator - Mobile App Ideas Generator with Design Thinking

![Design Thinking](https://img.shields.io/badge/Methodology-Design%20Thinking-blue)
![CrewAI](https://img.shields.io/badge/Framework-CrewAI-orange)
![Python](https://img.shields.io/badge/Language-Python%203.10+-green)

## 📋 Overview

IdeaGenerator is a multi-agent system based on [crewAI](https://crewai.com) that simulates a complete IBM-style design thinking team to generate innovative mobile app ideas. The system orchestrates collaboration between different specialized agents, each bringing their own expertise, to produce complete and well-developed mobile app concepts.

### 🎯 Key Features

- **Complete Design Thinking Process Simulation** — Goes through all phases of design thinking: empathy, definition, ideation, conceptual prototyping, and testing.
- **Specialized Agent Team** — 8 expert agents with distinct roles collaborate to generate and refine ideas.
- **Random Persona Generation** — Uses random values to create realistic and varied personas.
- **Structured Sequential Workflow** — 5-phase process with 30+ distinct tasks for thorough idea development.
- **Detailed Reports** — Generates detailed reports documenting the entire creative process and its results.
- **Multiple Launches** — Ability to launch multiple instances in parallel to generate various ideas simultaneously.

## 🧠 Multi-Agent Architecture

IdeaGenerator employs a team of 8 specialized agents, each with distinct roles and responsibilities:

| 🤖 Agent                 | 🎭 Role                    | 🎯 Objective                                                       |
| ------------------------ | -------------------------- | ------------------------------------------------------------------ |
| **Design Facilitator**   | Lead Facilitator           | Orchestrate design thinking sessions and facilitate collaboration  |
| **UX Designer**          | User Experience Specialist | Discover user behaviors and needs for human-centered solutions     |
| **Product Manager**      | Product Strategist         | Align user needs with business objectives and market opportunities |
| **Business Strategist**  | Commercial Analyst         | Evaluate commercial viability and potential of concepts            |
| **Data Analyst**         | Insights Specialist        | Use data to guide design decisions and validate hypotheses         |
| **Researcher**           | User Researcher            | Discover user needs and behaviors through research                 |
| **Creative Facilitator** | Innovation Catalyst        | Inspire creative ideas and encourage unconventional thinking       |
| **Innovation Coach**     | Change Agent               | Foster a culture of continuous innovation and adaptation           |

## 🛠️ Process Structure

The system simulates a complete design thinking process in 5 sequential phases:

1. **Initial Research & Empathy** — Persona generation, empathy mapping
2. **Current State Analysis** — Documentation of current workflows and pain points
3. **Future State Vision** — Design of ideal and improved scenarios
4. **Solution Ideation** — Creation of idea vignettes and solution narratives
5. **Final Narrative** — Development of a coherent "Who-What-Wow" story for the solution

## 📦 Installation

### Prerequisites

- Python >=3.10 <3.13
- [Make](https://www.gnu.org/software/make/) (optional, to use the Makefile)

### Installation Steps

1. Clone this repository and navigate to the project directory:

```bash
git clone https://github.com/your-username/idea_generator.git
cd idea_generator
```

2. Project initialization:

- Quick method:

```bash
# Single command to install everything
make init
```

- Manual method:

```bash
# Install pip dependencies
pip install -r requirements.txt

# Install crewai dependencies
crewai install
```

3. Configure your environment variables in the `.env` file. You can use the OpenRouter API which allows using different LLMs:

```
AI_API_KEY=your_api_key
AI_MODEL=your_preferred_model
AI_BASE_URL=optional_base_url
RANDOM_ORG_API_KEY=your_random_org_api_key (optional, for generating random values)
```

## 🚀 Usage

### Launch Methods

#### With Make (recommended)

```bash
# Launch a single instance
make run

# Launch multiple instances in parallel (example with 3)
make run i=3
```

#### With CrewAI CLI

```bash
crewai run
```

The system will generate a detailed report in the `conversations/` folder with a timestamp, containing the entire design process and final results.

## 🛠 Customization

- Modify `src/idea_generator/config/agents.yaml` to adjust agent roles and skills
- Adapt `src/idea_generator/config/tasks.yaml` to modify tasks and prompts
- Customize `src/idea_generator/crew.py` to change workflow or add new tasks

## 🔄 Project Architecture

```
idea_generator/
├── src/
│   └── idea_generator/
│       ├── config/
│       │   ├── agents.yaml    # Agent configuration
│       │   └── tasks.yaml     # Task definition
│       ├── tools/            # Custom tools
│       ├── crew.py           # Team and task definition
│       ├── main.py           # Entry point
│       └── utils.py          # Utility functions
├── conversations/           # Generated reports
├── Makefile                 # Commands to initialize and run the project
├── requirements.txt         # Python dependencies
├── pyproject.toml           # Project configuration
└── README.md                # This file
```

## 📄 License

[MIT](LICENSE)

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## 📚 Resources

- [CrewAI Documentation](https://docs.crewai.com)
- [CrewAI GitHub Repository](https://github.com/joaomdmoura/crewai)
