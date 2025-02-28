from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
import os

# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

llm = LLM(
    model=os.environ.get("AI_MODEL"),
    api_key=os.environ.get("AI_API_KEY"),
	base_url=os.environ.get("AI_BASE_URL")
)

@CrewBase
class IdeaGenerator():
	"""Équipe de génération d'idées d'applications mobiles suivant le Design Thinking"""

	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def design_facilitator(self) -> Agent:
		"""Lead Facilitator agent responsible for orchestrating the design thinking session"""
		return Agent(
			config=self.agents_config['design_facilitator'],
			llm=llm,
			verbose=True
		)

	@agent
	def ux_designer(self) -> Agent:
		"""UX Specialist agent focused on user behaviors and design insights"""
		return Agent(
			config=self.agents_config['ux_designer'],
			llm=llm,
			verbose=True
		)

	@agent
	def ui_designer(self) -> Agent:
		"""UI Expert agent for visual and interactive interface design"""
		return Agent(
			config=self.agents_config['ui_designer'],
			llm=llm,
			verbose=True
		)

	@agent
	def software_engineer(self) -> Agent:
		"""Technical Architect agent for technical feasibility and implementation"""
		return Agent(
			config=self.agents_config['software_engineer'],
			llm=llm,
			verbose=True
		)

	@agent
	def product_manager(self) -> Agent:
		"""Product Strategist agent aligning design with business objectives"""
		return Agent(
			config=self.agents_config['product_manager'],
			llm=llm,
			verbose=True
		)

	@agent
	def business_strategist(self) -> Agent:
		"""Commercial Analyst agent evaluating business viability"""
		return Agent(
			config=self.agents_config['business_strategist'],
			llm=llm,
			verbose=True
		)

	@agent
	def data_analyst(self) -> Agent:
		"""Insights Specialist agent for data-driven design decisions"""
		return Agent(
			config=self.agents_config['data_analyst'],
			llm=llm,
			verbose=True
		)

	@agent
	def researcher(self) -> Agent:
		"""User Researcher agent for comprehensive user research"""
		return Agent(
			config=self.agents_config['researcher'],
			llm=llm,
			verbose=True
		)

	@agent
	def creative_facilitator(self) -> Agent:
		"""Innovation Catalyst agent for creative ideation"""
		return Agent(
			config=self.agents_config['creative_facilitator'],
			llm=llm,
			verbose=True
		)

	@agent
	def innovation_coach(self) -> Agent:
		"""Change Agent for fostering innovation culture"""
		return Agent(
			config=self.agents_config['innovation_coach'],
			llm=llm,
			verbose=True
		)

	# =========================
	# Phase: Autonomous Initialization
	# =========================
	@task
	def initialization_proposition_A(self) -> Task:
		"""Generate initial personas using market trends"""
		return Task(
			config=self.tasks_config['initialization_proposition_A']
		)

	@task
	def initialization_proposition_B(self) -> Task:
		"""Propose global context and usage scenarios"""
		return Task(
			config=self.tasks_config['initialization_proposition_B']
		)

	@task
	def initialization_proposition_C(self) -> Task:
		"""Add strategic perspective and market opportunities"""
		return Task(
			config=self.tasks_config['initialization_proposition_C']
		)

	@task
	def initialization_comparison(self) -> Task:
		"""Compare initialization outputs"""
		return Task(
			config=self.tasks_config['initialization_comparison'],
			context=[
				self.initialization_proposition_A(),
				self.initialization_proposition_B(),
				self.initialization_proposition_C()
			]
		)

	@task
	def initialization_synthesis(self) -> Task:
		"""Synthesize initial framework"""
		return Task(
			config=self.tasks_config['initialization_synthesis'],
			context=[self.initialization_comparison()]
		)

	# =========================
	# Phase: Empathy - Empathy Map
	# =========================
	@task
	def empathy_map_collect_A(self) -> Task:
		"""Collect user interview insights"""
		return Task(
			config=self.tasks_config['empathy_map_collect_A'],
			context=[self.initialization_synthesis()]
		)

	@task
	def empathy_map_collect_B(self) -> Task:
		"""Observe user behaviors"""
		return Task(
			config=self.tasks_config['empathy_map_collect_B'],
			context=[self.initialization_synthesis()]
		)

	@task
	def empathy_map_collect_C(self) -> Task:
		"""Analyze secondary data"""
		return Task(
			config=self.tasks_config['empathy_map_collect_C'],
			context=[self.initialization_synthesis()]
		)

	@task
	def empathy_map_comparison(self) -> Task:
		"""Compare empathy map data"""
		return Task(
			config=self.tasks_config['empathy_map_comparison'],
			context=[
				self.empathy_map_collect_A(),
				self.empathy_map_collect_B(),
				self.empathy_map_collect_C()
			]
		)

	@task
	def empathy_map_synthesis(self) -> Task:
		"""Synthesize empathy map"""
		return Task(
			config=self.tasks_config['empathy_map_synthesis'],
			context=[self.empathy_map_comparison()]
		)

	# =========================
	# Phase: Empathy - Hopes and Fears
	# =========================
	@task
	def hopes_fears_collect_A(self) -> Task:
		"""Collect hopes and fears from interviews"""
		return Task(
			config=self.tasks_config['hopes_fears_collect_A'],
			context=[self.empathy_map_synthesis()]
		)

	@task
	def hopes_fears_collect_B(self) -> Task:
		"""Add creative perspectives"""
		return Task(
			config=self.tasks_config['hopes_fears_collect_B'],
			context=[self.empathy_map_synthesis()]
		)

	@task
	def hopes_fears_collect_C(self) -> Task:
		"""Validate with quantitative analysis"""
		return Task(
			config=self.tasks_config['hopes_fears_collect_C'],
			context=[self.empathy_map_synthesis()]
		)

	@task
	def hopes_fears_comparison(self) -> Task:
		"""Compare hopes and fears lists"""
		return Task(
			config=self.tasks_config['hopes_fears_comparison'],
			context=[
				self.hopes_fears_collect_A(),
				self.hopes_fears_collect_B(),
				self.hopes_fears_collect_C()
			]
		)

	@task
	def hopes_fears_synthesis(self) -> Task:
		"""Synthesize final hopes and fears"""
		return Task(
			config=self.tasks_config['hopes_fears_synthesis'],
			context=[self.hopes_fears_comparison()]
		)

	# =========================
	# Phase: Empathy - Stakeholder Map
	# =========================
	@task
	def stakeholder_map_collect_A(self) -> Task:
		"""Identify main stakeholders"""
		return Task(
			config=self.tasks_config['stakeholder_map_collect_A'],
			context=[
				self.empathy_map_synthesis(),
				self.hopes_fears_synthesis()
			]
		)

	@task
	def stakeholder_map_collect_B(self) -> Task:
		"""Add strategic perspective"""
		return Task(
			config=self.tasks_config['stakeholder_map_collect_B'],
			context=[
				self.empathy_map_synthesis(),
				self.hopes_fears_synthesis()
			]
		)

	@task
	def stakeholder_map_collect_C(self) -> Task:
		"""Validate stakeholder list"""
		return Task(
			config=self.tasks_config['stakeholder_map_collect_C'],
			context=[
				self.empathy_map_synthesis(),
				self.hopes_fears_synthesis()
			]
		)

	@task
	def stakeholder_map_comparison(self) -> Task:
		"""Compare stakeholder lists"""
		return Task(
			config=self.tasks_config['stakeholder_map_comparison'],
			context=[
				self.stakeholder_map_collect_A(),
				self.stakeholder_map_collect_B(),
				self.stakeholder_map_collect_C()
			]
		)

	@task
	def stakeholder_map_synthesis(self) -> Task:
		"""Create final stakeholder map"""
		return Task(
			config=self.tasks_config['stakeholder_map_synthesis'],
			context=[self.stakeholder_map_comparison()]
		)

	# =========================
	# Phase: Definition - Needs Statements
	# =========================
	@task
	def needs_statements_proposition_A(self) -> Task:
		"""Propose initial needs statements"""
		return Task(
			config=self.tasks_config['needs_statements_proposition_A'],
			context=[
				self.empathy_map_synthesis(),
				self.hopes_fears_synthesis(),
				self.stakeholder_map_synthesis()
			]
		)

	@task
	def needs_statements_proposition_B(self) -> Task:
		"""Add contextual insights"""
		return Task(
			config=self.tasks_config['needs_statements_proposition_B'],
			context=[
				self.empathy_map_synthesis(),
				self.hopes_fears_synthesis(),
				self.stakeholder_map_synthesis()
			]
		)

	@task
	def needs_statements_proposition_C(self) -> Task:
		"""Add strategic perspective"""
		return Task(
			config=self.tasks_config['needs_statements_proposition_C'],
			context=[
				self.empathy_map_synthesis(),
				self.hopes_fears_synthesis(),
				self.stakeholder_map_synthesis()
			]
		)

	@task
	def needs_statements_comparison(self) -> Task:
		"""Compare need statements"""
		return Task(
			config=self.tasks_config['needs_statements_comparison'],
			context=[
				self.needs_statements_proposition_A(),
				self.needs_statements_proposition_B(),
				self.needs_statements_proposition_C()
			]
		)

	@task
	def needs_statements_synthesis(self) -> Task:
		"""Synthesize final needs"""
		return Task(
			config=self.tasks_config['needs_statements_synthesis'],
			context=[self.needs_statements_comparison()]
		)

	# =========================
	# Phase: Definition - Assumptions and Questions
	# =========================
	@task
	def assumptions_questions_proposition_A(self) -> Task:
		"""Propose initial assumptions"""
		return Task(
			config=self.tasks_config['assumptions_questions_proposition_A'],
			context=[self.needs_statements_synthesis()]
		)

	@task
	def assumptions_questions_proposition_B(self) -> Task:
		"""Add user insights"""
		return Task(
			config=self.tasks_config['assumptions_questions_proposition_B'],
			context=[self.needs_statements_synthesis()]
		)

	@task
	def assumptions_questions_proposition_C(self) -> Task:
		"""Add technical perspective"""
		return Task(
			config=self.tasks_config['assumptions_questions_proposition_C'],
			context=[self.needs_statements_synthesis()]
		)

	@task
	def assumptions_questions_comparison(self) -> Task:
		"""Compare assumptions"""
		return Task(
			config=self.tasks_config['assumptions_questions_comparison'],
			context=[
				self.assumptions_questions_proposition_A(),
				self.assumptions_questions_proposition_B(),
				self.assumptions_questions_proposition_C()
			]
		)

	@task
	def assumptions_questions_synthesis(self) -> Task:
		"""Synthesize final assumptions"""
		return Task(
			config=self.tasks_config['assumptions_questions_synthesis'],
			context=[self.assumptions_questions_comparison()]
		)

	# =========================
	# Phase: Ideation - Big Idea Vignettes
	# =========================
	@task
	def big_idea_vignettes_proposition_A(self) -> Task:
		"""Propose initial narrative"""
		return Task(
			config=self.tasks_config['big_idea_vignettes_proposition_A'],
			context=[
				self.needs_statements_synthesis(),
				self.assumptions_questions_synthesis()
			]
		)

	@task
	def big_idea_vignettes_proposition_B(self) -> Task:
		"""Propose alternative narrative"""
		return Task(
			config=self.tasks_config['big_idea_vignettes_proposition_B'],
			context=[
				self.needs_statements_synthesis(),
				self.assumptions_questions_synthesis()
			]
		)

	@task
	def big_idea_vignettes_proposition_C(self) -> Task:
		"""Add UX perspective"""
		return Task(
			config=self.tasks_config['big_idea_vignettes_proposition_C'],
			context=[
				self.needs_statements_synthesis(),
				self.assumptions_questions_synthesis()
			]
		)

	@task
	def big_idea_vignettes_comparison(self) -> Task:
		"""Compare narratives"""
		return Task(
			config=self.tasks_config['big_idea_vignettes_comparison'],
			context=[
				self.big_idea_vignettes_proposition_A(),
				self.big_idea_vignettes_proposition_B(),
				self.big_idea_vignettes_proposition_C()
			]
		)

	@task
	def big_idea_vignettes_synthesis(self) -> Task:
		"""Synthesize final narrative"""
		return Task(
			config=self.tasks_config['big_idea_vignettes_synthesis'],
			context=[self.big_idea_vignettes_comparison()]
		)

	# =========================
	# Phase: Ideation - Writing Hills
	# =========================
	@task
	def writing_hills_proposition_A(self) -> Task:
		"""Propose visual objectives"""
		return Task(
			config=self.tasks_config['writing_hills_proposition_A'],
			context=[self.big_idea_vignettes_synthesis()]
		)

	@task
	def writing_hills_proposition_B(self) -> Task:
		"""Add visual metaphors"""
		return Task(
			config=self.tasks_config['writing_hills_proposition_B'],
			context=[self.big_idea_vignettes_synthesis()]
		)

	@task
	def writing_hills_proposition_C(self) -> Task:
		"""Add business goals"""
		return Task(
			config=self.tasks_config['writing_hills_proposition_C'],
			context=[self.big_idea_vignettes_synthesis()]
		)

	@task
	def writing_hills_comparison(self) -> Task:
		"""Compare hills proposals"""
		return Task(
			config=self.tasks_config['writing_hills_comparison'],
			context=[
				self.writing_hills_proposition_A(),
				self.writing_hills_proposition_B(),
				self.writing_hills_proposition_C()
			]
		)

	@task
	def writing_hills_synthesis(self) -> Task:
		"""Create final hills"""
		return Task(
			config=self.tasks_config['writing_hills_synthesis'],
			context=[self.writing_hills_comparison()]
		)

	# =========================
	# Phase: Ideation - Prioritization
	# =========================
	@task
	def prioritization_proposition_A(self) -> Task:
		"""Initial idea ranking"""
		return Task(
			config=self.tasks_config['prioritization_proposition_A'],
			context=[
				self.big_idea_vignettes_synthesis(),
				self.writing_hills_synthesis()
			]
		)

	@task
	def prioritization_proposition_B(self) -> Task:
		"""UX-focused ranking"""
		return Task(
			config=self.tasks_config['prioritization_proposition_B'],
			context=[
				self.big_idea_vignettes_synthesis(),
				self.writing_hills_synthesis()
			]
		)

	@task
	def prioritization_proposition_C(self) -> Task:
		"""Innovation-focused ranking"""
		return Task(
			config=self.tasks_config['prioritization_proposition_C'],
			context=[
				self.big_idea_vignettes_synthesis(),
				self.writing_hills_synthesis()
			]
		)

	@task
	def prioritization_comparison(self) -> Task:
		"""Compare rankings"""
		return Task(
			config=self.tasks_config['prioritization_comparison'],
			context=[
				self.prioritization_proposition_A(),
				self.prioritization_proposition_B(),
				self.prioritization_proposition_C()
			]
		)

	@task
	def prioritization_synthesis(self) -> Task:
		"""Create final ranking"""
		return Task(
			config=self.tasks_config['prioritization_synthesis'],
			context=[self.prioritization_comparison()]
		)

	# =========================
	# Phase: Prototyping - As-Is Scenario Map
	# =========================
	@task
	def asis_scenario_map_proposition_A(self) -> Task:
		"""Map current experience"""
		return Task(
			config=self.tasks_config['asis_scenario_map_proposition_A'],
			context=[
				self.needs_statements_synthesis(),
				self.prioritization_synthesis()
			]
		)

	@task
	def asis_scenario_map_proposition_B(self) -> Task:
		"""Add observational data"""
		return Task(
			config=self.tasks_config['asis_scenario_map_proposition_B'],
			context=[
				self.needs_statements_synthesis(),
				self.prioritization_synthesis()
			]
		)

	@task
	def asis_scenario_map_proposition_C(self) -> Task:
		"""Add business insights"""
		return Task(
			config=self.tasks_config['asis_scenario_map_proposition_C'],
			context=[
				self.needs_statements_synthesis(),
				self.prioritization_synthesis()
			]
		)

	@task
	def asis_scenario_map_comparison(self) -> Task:
		"""Compare current maps"""
		return Task(
			config=self.tasks_config['asis_scenario_map_comparison'],
			context=[
				self.asis_scenario_map_proposition_A(),
				self.asis_scenario_map_proposition_B(),
				self.asis_scenario_map_proposition_C()
			]
		)

	@task
	def asis_scenario_map_synthesis(self) -> Task:
		"""Create final as-is map"""
		return Task(
			config=self.tasks_config['asis_scenario_map_synthesis'],
			context=[self.asis_scenario_map_comparison()]
		)

	# =========================
	# Phase: Prototyping - To-Be Scenario Map
	# =========================
	@task
	def tobe_scenario_map_proposition_A(self) -> Task:
		"""Map future experience"""
		return Task(
			config=self.tasks_config['tobe_scenario_map_proposition_A'],
			context=[
				self.asis_scenario_map_synthesis(),
				self.prioritization_synthesis()
			]
		)

	@task
	def tobe_scenario_map_proposition_B(self) -> Task:
		"""Add UX improvements"""
		return Task(
			config=self.tasks_config['tobe_scenario_map_proposition_B'],
			context=[
				self.asis_scenario_map_synthesis(),
				self.prioritization_synthesis()
			]
		)

	@task
	def tobe_scenario_map_proposition_C(self) -> Task:
		"""Add creative elements"""
		return Task(
			config=self.tasks_config['tobe_scenario_map_proposition_C'],
			context=[
				self.asis_scenario_map_synthesis(),
				self.prioritization_synthesis()
			]
		)

	@task
	def tobe_scenario_map_comparison(self) -> Task:
		"""Compare future maps"""
		return Task(
			config=self.tasks_config['tobe_scenario_map_comparison'],
			context=[
				self.tobe_scenario_map_proposition_A(),
				self.tobe_scenario_map_proposition_B(),
				self.tobe_scenario_map_proposition_C()
			]
		)

	@task
	def tobe_scenario_map_synthesis(self) -> Task:
		"""Create final to-be map"""
		return Task(
			config=self.tasks_config['tobe_scenario_map_synthesis'],
			context=[self.tobe_scenario_map_comparison()]
		)

	# =========================
	# Phase: Prototyping - Storyboard
	# =========================
	@task
	def storyboard_proposition_A(self) -> Task:
		"""Create initial storyboard"""
		return Task(
			config=self.tasks_config['storyboard_proposition_A'],
			context=[self.tobe_scenario_map_synthesis()]
		)

	@task
	def storyboard_proposition_B(self) -> Task:
		"""Add narrative details"""
		return Task(
			config=self.tasks_config['storyboard_proposition_B'],
			context=[self.tobe_scenario_map_synthesis()]
		)

	@task
	def storyboard_proposition_C(self) -> Task:
		"""Add creative elements"""
		return Task(
			config=self.tasks_config['storyboard_proposition_C'],
			context=[self.tobe_scenario_map_synthesis()]
		)

	@task
	def storyboard_comparison(self) -> Task:
		"""Compare storyboards"""
		return Task(
			config=self.tasks_config['storyboard_comparison'],
			context=[
				self.storyboard_proposition_A(),
				self.storyboard_proposition_B(),
				self.storyboard_proposition_C()
			]
		)

	@task
	def storyboard_synthesis(self) -> Task:
		"""Create final storyboard"""
		return Task(
			config=self.tasks_config['storyboard_synthesis'],
			context=[self.storyboard_comparison()]
		)

	# =========================
	# Phase: Technical Feasibility
	# =========================
	@task
	def tech_feasibility_proposition_A(self) -> Task:
		"""Technical analysis"""
		return Task(
			config=self.tasks_config['tech_feasibility_proposition_A'],
			context=[
				self.tobe_scenario_map_synthesis(),
				self.storyboard_synthesis()
			]
		)

	@task
	def tech_feasibility_proposition_B(self) -> Task:
		"""Risk assessment"""
		return Task(
			config=self.tasks_config['tech_feasibility_proposition_B'],
			context=[
				self.tobe_scenario_map_synthesis(),
				self.storyboard_synthesis()
			]
		)

	@task
	def tech_feasibility_proposition_C(self) -> Task:
		"""Cost-benefit analysis"""
		return Task(
			config=self.tasks_config['tech_feasibility_proposition_C'],
			context=[
				self.tobe_scenario_map_synthesis(),
				self.storyboard_synthesis()
			]
		)

	@task
	def tech_feasibility_comparison(self) -> Task:
		"""Compare analyses"""
		return Task(
			config=self.tasks_config['tech_feasibility_comparison'],
			context=[
				self.tech_feasibility_proposition_A(),
				self.tech_feasibility_proposition_B(),
				self.tech_feasibility_proposition_C()
			]
		)

	@task
	def tech_feasibility_synthesis(self) -> Task:
		"""Create final analysis"""
		return Task(
			config=self.tasks_config['tech_feasibility_synthesis'],
			context=[self.tech_feasibility_comparison()]
		)

	# =========================
	# Phase: Test & Feedback - Playbacks
	# =========================
	@task
	def playbacks_proposition_A(self) -> Task:
		"""Initial playback plan"""
		return Task(
			config=self.tasks_config['playbacks_proposition_A'],
			context=[
				self.storyboard_synthesis(),
				self.tech_feasibility_synthesis()
			]
		)

	@task
	def playbacks_proposition_B(self) -> Task:
		"""Add interactive elements"""
		return Task(
			config=self.tasks_config['playbacks_proposition_B'],
			context=[
				self.storyboard_synthesis(),
				self.tech_feasibility_synthesis()
			]
		)

	@task
	def playbacks_proposition_C(self) -> Task:
		"""Add demonstrations"""
		return Task(
			config=self.tasks_config['playbacks_proposition_C'],
			context=[
				self.storyboard_synthesis(),
				self.tech_feasibility_synthesis()
			]
		)

	@task
	def playbacks_comparison(self) -> Task:
		"""Compare playback plans"""
		return Task(
			config=self.tasks_config['playbacks_comparison'],
			context=[
				self.playbacks_proposition_A(),
				self.playbacks_proposition_B(),
				self.playbacks_proposition_C()
			]
		)

	@task
	def playbacks_synthesis(self) -> Task:
		"""Create final playback plan"""
		return Task(
			config=self.tasks_config['playbacks_synthesis'],
			context=[self.playbacks_comparison()]
		)

	# =========================
	# Phase: Test & Feedback - Feedback Grid
	# =========================
	@task
	def feedback_grid_proposition_A(self) -> Task:
		"""Initial feedback grid"""
		return Task(
			config=self.tasks_config['feedback_grid_proposition_A'],
			context=[self.playbacks_synthesis()]
		)

	@task
	def feedback_grid_proposition_B(self) -> Task:
		"""Add UX metrics"""
		return Task(
			config=self.tasks_config['feedback_grid_proposition_B'],
			context=[self.playbacks_synthesis()]
		)

	@task
	def feedback_grid_proposition_C(self) -> Task:
		"""Add business metrics"""
		return Task(
			config=self.tasks_config['feedback_grid_proposition_C'],
			context=[self.playbacks_synthesis()]
		)

	@task
	def feedback_grid_comparison(self) -> Task:
		"""Compare grids"""
		return Task(
			config=self.tasks_config['feedback_grid_comparison'],
			context=[
				self.feedback_grid_proposition_A(),
				self.feedback_grid_proposition_B(),
				self.feedback_grid_proposition_C()
			]
		)

	@task
	def feedback_grid_synthesis(self) -> Task:
		"""Create final grid"""
		return Task(
			config=self.tasks_config['feedback_grid_synthesis'],
			context=[self.feedback_grid_comparison()]
		)

	# =========================
	# Phase: Roadmapping
	# =========================
	@task
	def roadmapping_proposition_A(self) -> Task:
		"""Initial roadmap"""
		return Task(
			config=self.tasks_config['roadmapping_proposition_A'],
			context=[
				self.tech_feasibility_synthesis(),
				self.feedback_grid_synthesis()
			]
		)

	@task
	def roadmapping_proposition_B(self) -> Task:
		"""Technical planning"""
		return Task(
			config=self.tasks_config['roadmapping_proposition_B'],
			context=[
				self.tech_feasibility_synthesis(),
				self.feedback_grid_synthesis()
			]
		)

	@task
	def roadmapping_proposition_C(self) -> Task:
		"""Strategic planning"""
		return Task(
			config=self.tasks_config['roadmapping_proposition_C'],
			context=[
				self.tech_feasibility_synthesis(),
				self.feedback_grid_synthesis()
			]
		)

	@task
	def roadmapping_comparison(self) -> Task:
		"""Compare roadmaps"""
		return Task(
			config=self.tasks_config['roadmapping_comparison'],
			context=[
				self.roadmapping_proposition_A(),
				self.roadmapping_proposition_B(),
				self.roadmapping_proposition_C()
			]
		)

	@task
	def roadmapping_synthesis(self) -> Task:
		"""Create final roadmap"""
		return Task(
			config=self.tasks_config['roadmapping_synthesis'],
			context=[self.roadmapping_comparison()]
		)

	# =========================
	# Phase: Documentation
	# =========================
	@task
	def documentation_proposition_A(self) -> Task:
		"""Initial documentation"""
		return Task(
			config=self.tasks_config['documentation_proposition_A'],
			context=[
				self.initialization_synthesis(),
				self.empathy_map_synthesis(),
				self.hopes_fears_synthesis(),
				self.stakeholder_map_synthesis(),
				self.needs_statements_synthesis(),
				self.assumptions_questions_synthesis(),
				self.big_idea_vignettes_synthesis(),
				self.writing_hills_synthesis(),
				self.prioritization_synthesis(),
				self.asis_scenario_map_synthesis(),
				self.tobe_scenario_map_synthesis(),
				self.storyboard_synthesis(),
				self.tech_feasibility_synthesis(),
				self.playbacks_synthesis(),
				self.feedback_grid_synthesis(),
				self.roadmapping_synthesis()
			]
		)

	@task
	def documentation_proposition_B(self) -> Task:
		"""Add narrative"""
		return Task(
			config=self.tasks_config['documentation_proposition_B'],
			context=[self.documentation_proposition_A()]
		)

	@task
	def documentation_proposition_C(self) -> Task:
		"""Add strategic view"""
		return Task(
			config=self.tasks_config['documentation_proposition_C'],
			context=[self.documentation_proposition_A()]
		)

	@task
	def documentation_comparison(self) -> Task:
		"""Compare documentation"""
		return Task(
			config=self.tasks_config['documentation_comparison'],
			context=[
				self.documentation_proposition_A(),
				self.documentation_proposition_B(),
				self.documentation_proposition_C()
			]
		)

	@task
	def documentation_synthesis(self) -> Task:
		"""Create final documentation"""
		return Task(
			config=self.tasks_config['documentation_synthesis'],
			context=[self.documentation_comparison()]
		)

	@crew
	def crew(self) -> Crew:
		"""Crée l'équipe de génération d'idées"""
		return Crew(
			agents=self.agents,
			tasks=self.tasks,
			process=Process.sequential,
			verbose=True,
		)
