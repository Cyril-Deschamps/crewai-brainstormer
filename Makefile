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
	@bash -c "trap 'kill 0; exit 1' INT TERM; \
		echo \"🚀 Launching $(i) instance(s) of the idea generator...\" && \
		for i in \$$(seq 1 $(i)); do \
			echo \"🔄 Launching instance \$$i...\" && \
			python src/idea_generator/main.py > /dev/null 2>&1 & \
		done && \
		wait && \
		echo \"✅ All instances have completed.\" && \
		echo \"📝 Reports have been generated in the logs/ directory\""

clean:
	@echo "Cleaning temporary files and caches..."
	rm -rf __pycache__
	rm -rf logs/*
	@echo "✅ Cleaning complete!"