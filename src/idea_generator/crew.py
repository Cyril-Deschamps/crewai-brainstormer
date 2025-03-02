from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from datetime import datetime
import uuid
from .utils import get_true_random

@CrewBase
class IdeaGenerator:
	def __init__(self, model, api_key, base_url):
		"""Mobile app idea generation team following Design Thinking methodology"""
		self.llm = LLM(
			model=model,
			api_key=api_key,
			base_url=base_url
		)
		
		self.agents_config = 'config/agents.yaml'
		self.tasks_config = 'config/tasks.yaml'

	@agent
	def design_facilitator(self) -> Agent:
		"""Lead Facilitator agent responsible for orchestrating the design thinking session"""
		return Agent(
			config=self.agents_config['design_facilitator'],
			llm=self.llm,
			verbose=True
		)

	@agent
	def ux_designer(self) -> Agent:
		"""UX Specialist agent focused on user behaviors and design insights"""
		return Agent(
			config=self.agents_config['ux_designer'],
			llm=self.llm,
			verbose=True
		)

	@agent
	def product_manager(self) -> Agent:
		"""Product Strategist agent aligning design with business objectives"""
		return Agent(
			config=self.agents_config['product_manager'],
			llm=self.llm,
			verbose=True
		)

	@agent
	def business_strategist(self) -> Agent:
		"""Commercial Analyst agent evaluating business viability"""
		return Agent(
			config=self.agents_config['business_strategist'],
			llm=self.llm,
			verbose=True
		)

	@agent
	def data_analyst(self) -> Agent:
		"""Insights Specialist agent for data-driven design decisions"""
		return Agent(
			config=self.agents_config['data_analyst'],
			llm=self.llm,
			verbose=True
		)

	@agent
	def researcher(self) -> Agent:
		"""User Researcher agent for comprehensive user research"""
		return Agent(
			config=self.agents_config['researcher'],
			llm=self.llm,
			verbose=True
		)

	@agent
	def creative_facilitator(self) -> Agent:
		"""Innovation Catalyst agent for creative ideation"""
		return Agent(
			config=self.agents_config['creative_facilitator'],
			llm=self.llm,
			verbose=True
		)

	@agent
	def innovation_coach(self) -> Agent:
		"""Change Agent for fostering innovation culture"""
		return Agent(
			config=self.agents_config['innovation_coach'],
			llm=self.llm,
			verbose=True
		)

	@task
	def initialization_proposition_a(self) -> Task:
		"""Generate a random persona with problem statement"""
		# Get true random values for age and other parameters
		age = get_true_random(18, 60)
		num_pain_points = get_true_random(1, 9)
		
		# Inject these random values into the task configuration
		config = self.tasks_config['initialization_proposition_A'].copy()
		config['description'] = config['description'] + f"\nUse these true random values: age={age}, number_of_pain_points={num_pain_points}"
		
		return Task(config=config)

	@task
	def initialization_challenge(self) -> Task:
		"""Challenge the initial persona to identify assumptions and biases"""
		return Task(
			config=self.tasks_config['initialization_challenge']
		)
	
	@task
	def initialization_refinement(self) -> Task:
		"""Refine the persona based on the challenges and feedback"""
		return Task(
			config=self.tasks_config['initialization_refinement']
		)

	@task
	def empathy_map_verification(self) -> Task:
		"""Verify the consistency and reliability of the empathy map data"""
		return Task(
			config=self.tasks_config['empathy_map_verification']
		)

	@task
	def empathy_map_collect_a(self) -> Task:
		"""Simulate user interview based on persona"""
		return Task(
			config=self.tasks_config['empathy_map_collect_A']
		)

	@task
	def empathy_map_collect_b(self) -> Task:
		"""Simulate observations of persona behavior"""
		return Task(
			config=self.tasks_config['empathy_map_collect_B']
		)

	@task
	def empathy_map_comparison(self) -> Task:
		"""Compare interview insights and observations"""
		return Task(
			config=self.tasks_config['empathy_map_comparison']
		)

	@task
	def empathy_map_synthesis(self) -> Task:
		"""Synthesize final empathy map"""
		return Task(
			config=self.tasks_config['empathy_map_synthesis']
		)

	@task
	def asis_scenario_map_proposition_a(self) -> Task:
		"""Document current state steps and pain points"""
		return Task(
			config=self.tasks_config['asis_scenario_map_proposition_A']
		)

	@task
	def asis_scenario_map_proposition_b(self) -> Task:
		"""Propose alternative current workflow mapping"""
		return Task(
			config=self.tasks_config['asis_scenario_map_proposition_B']
		)

	@task
	def asis_scenario_map_comparison(self) -> Task:
		"""Compare As-Is maps outputs"""
		return Task(
			config=self.tasks_config['asis_scenario_map_comparison']
		)

	@task
	def asis_scenario_map_synthesis(self) -> Task:
		"""Synthesize final As-Is scenario map"""
		return Task(
			config=self.tasks_config['asis_scenario_map_synthesis']
		)

	@task
	def tobe_scenario_map_proposition_a(self) -> Task:
		"""Envision ideal future state"""
		return Task(
			config=self.tasks_config['tobe_scenario_map_proposition_A']
		)

	@task
	def tobe_scenario_map_proposition_b(self) -> Task:
		"""Propose alternative future state focusing on UX"""
		return Task(
			config=self.tasks_config['tobe_scenario_map_proposition_B']
		)
	
	@task
	def tobe_scenario_map_proposition_c(self) -> Task:
		"""Propose alternative future state focusing on UX"""
		return Task(
			config=self.tasks_config['tobe_scenario_map_proposition_C']
	)

	@task
	def tobe_scenario_map_proposition_d(self) -> Task:
		"""Propose alternative future state focusing on UX"""
		return Task(
			config=self.tasks_config['tobe_scenario_map_proposition_D']
	)

	@task
	def tobe_scenario_map_proposition_e(self) -> Task:
		"""Propose alternative future state focusing on UX"""
		return Task(
			config=self.tasks_config['tobe_scenario_map_proposition_E']
	)

	@task
	def tobe_scenario_map_comparison(self) -> Task:
		"""Compare To-Be maps outputs"""
		return Task(
			config=self.tasks_config['tobe_scenario_map_comparison']
		)

	@task
	def tobe_scenario_map_synthesis(self) -> Task:
		"""Synthesize final To-Be scenario map"""
		return Task(
			config=self.tasks_config['tobe_scenario_map_synthesis']
		)

	@task
	def big_idea_vignettes_proposition_a(self) -> Task:
		"""Create a compelling solution narrative"""
		return Task(
			config=self.tasks_config['big_idea_vignettes_proposition_A']
		)

	@task
	def big_idea_vignettes_proposition_b(self) -> Task:
		"""Propose alternative solution narrative"""
		return Task(
			config=self.tasks_config['big_idea_vignettes_proposition_B']
		)
	
	@task
	def big_idea_vignettes_proposition_c(self) -> Task:
		"""Create a solution narrative from a skeptical perspective"""
		return Task(
			config=self.tasks_config['big_idea_vignettes_proposition_C']
		)

	@task
	def big_idea_vignettes_comparison(self) -> Task:
		"""Compare and evaluate solution narratives"""
		return Task(
			config=self.tasks_config['big_idea_vignettes_comparison']
		)

	@task
	def big_idea_vignettes_synthesis(self) -> Task:
		"""Synthesize the vignettes into a cohesive narrative"""
		return Task(
			config=self.tasks_config['big_idea_vignettes_synthesis']
		)

	@task
	def writing_hills_proposition_a(self) -> Task:
		"""Create Who-What-Wow narrative"""
		return Task(
			config=self.tasks_config['writing_hills_proposition_A']
		)

	@task
	def writing_hills_proposition_b(self) -> Task:
		"""Propose alternative Who-What-Wow narrative"""
		return Task(
			config=self.tasks_config['writing_hills_proposition_B']
		)

	@task
	def writing_hills_comparison(self) -> Task:
		"""Compare and evaluate the Hills statements"""
		return Task(
			config=self.tasks_config['writing_hills_comparison']
		)

	@task
	def writing_hills_synthesis(self) -> Task:
		"""Synthesize final Who-What-Wow narrative"""
		return Task(
			config=self.tasks_config['writing_hills_synthesis']
		)

	@task
	def final_solution_overview(self) -> Task:
		"""Create a comprehensive overview of the final solution"""
		return Task(
			config=self.tasks_config['final_solution_overview']
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the idea generation team"""
		timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
		unique_id = str(uuid.uuid4())[:8]  # Using first 8 characters of UUID for brevity
		return Crew(
			agents=self.agents,
			output_log_file=f"logs/idea_generation_report_{timestamp}_{unique_id}.md",
			tasks=[
				# Phase 1: Initial Research & Empathy with multi-turn feedback
				self.initialization_proposition_a(),
				self.initialization_challenge(),
				self.initialization_refinement(),
				self.empathy_map_collect_a(),
				self.empathy_map_verification(),
				self.empathy_map_collect_b(),
				self.empathy_map_comparison(),
				self.empathy_map_synthesis(),

				# Phase 2: Current State Analysis
				self.asis_scenario_map_proposition_a(),
				self.asis_scenario_map_proposition_b(),
				self.asis_scenario_map_comparison(),
				self.asis_scenario_map_synthesis(),

				# Phase 3: Future State Vision with contextual dynamics
				self.tobe_scenario_map_proposition_a(),
				self.tobe_scenario_map_proposition_b(),
				self.tobe_scenario_map_proposition_c(),
				self.tobe_scenario_map_proposition_d(),
				self.tobe_scenario_map_proposition_e(),
				self.tobe_scenario_map_comparison(),
				self.tobe_scenario_map_synthesis(),

				# Phase 4: Solution Ideation with varying perspectives
				self.big_idea_vignettes_proposition_a(),
				self.big_idea_vignettes_proposition_b(),
				self.big_idea_vignettes_proposition_c(),
				self.big_idea_vignettes_comparison(),
				self.big_idea_vignettes_synthesis(),

				# Phase 5: Final Narrative with iterative refinement
				self.writing_hills_proposition_a(),
				self.writing_hills_proposition_b(),
				self.writing_hills_comparison(),
				self.writing_hills_synthesis(),
				
				# Final comprehensive overview
				self.final_solution_overview()
			],
			process=Process.sequential,
			verbose=True,
		)


