# Makefile for Crewai Brainstormer
.PHONY: help init run solutions

i ?= 1

help:
	@echo "Available commands:"
	@echo "  make help      - Display this help"
	@echo "  make init      - Initialize the project (dependencies and environment)"
	@echo "  make run       - Run the crewai brainstormer (1 instance by default)"
	@echo "  make run i=3   - Run 3 instances of the brainstormer in parallel"
	@echo "  make clean     - Clean temporary files and caches"
	@echo "  make solutions - List all solutions and their Hills Statements"

init:
	@echo "🚀 Initializing Crewai Brainstormer project..."
	@echo "📦 Installing pip dependencies..."
	pip install -e .
	@echo "📦 Installing crewai dependencies..."
	crewai install
	@echo "✅ Installation complete!"
	@echo "ℹ️  Don't forget to configure your .env file with your API keys."
	
run:
	python src/parallel_runner.py $(i)

solutions:
	@echo "\n\033[1;36m🎯 Solutions and their Hills Statements:\033[0m\n"
	@find conversations -type f -name "*.txt" | while read -r file; do \
		echo "\033[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m"; \
		echo "\033[1;33m📄 Report:\033[0m $$(basename "$$file")"; \
		json_block=$$(tac "$$file"); \
		solution=$$(echo "$$json_block" | grep '"solution_name":' | head -n1 | sed 's/.*": "//; s/".*//' || echo "Not found"); \
		hills=$$(echo "$$json_block" | grep '"hills_statement":' | head -n1 | sed 's/.*": "//; s/".*//' || echo "Not found"); \
		echo "\033[1;32m🚀 Solution:\033[0m $$solution"; \
		echo "\033[1;35m📝 Hills Statement:\033[0m $$hills\n"; \
	done