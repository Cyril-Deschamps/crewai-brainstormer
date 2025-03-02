# Makefile for IdeaGenerator

.PHONY: help init run clean

i ?= 1

help:
	@echo "Available commands:"
	@echo "  make help      - Display this help"
	@echo "  make init      - Initialize the project (dependencies and environment)"
	@echo "  make run       - Run the idea generator (1 instance by default)"
	@echo "  make run i=3   - Run 3 instances of the generator in parallel"
	@echo "  make clean     - Clean temporary files and caches"

init:
	@echo "🚀 Initializing IdeaGenerator project..."
	@echo "📦 Installing pip dependencies..."
	pip install -r requirements.txt
	@echo "📦 Installing crewai dependencies..."
	crewai install
	@echo "✅ Installation complete!"
	@echo "ℹ️  Don't forget to configure your .env file with your API keys."
	
run:
	python src/idea_generator/parallel_runner.py $(i)

clean:
	@echo "Cleaning temporary files and caches..."
	rm -rf logs