.PHONY: clean test lint

TEST_PATH=./

help:
	@echo "    train-nlu"
	@echo "        Train the natural language understanding using Rasa NLU."
	@echo "    train-core"
	@echo "        Train a dialogue model using Rasa core."
	@echo "    visualize"
	@echo "        Saves the story graphs into a file"
	@echo "    action-server"
	@echo "        Runs action server."
	@echo "    run-cmdline"
	@echo "        Starts the bot on the command line"

train-nlu:
	python -m rasa_nlu.train -c nlu_tensorflow.yml --fixed_model_name current --data data/nlu/ -o models --project nlu --verbose

train-core:
	python -m rasa_core.train -d domain.yml -s data/core/stories.md -o models/dialogue -c policies.yml

visualize:
	python -m rasa_core.visualize -s data/core/ -d domain.yml -o story_graph.html

action-server:
	python -m rasa_sdk.endpoint --actions actions

cmdline:
	python -m rasa_core.run -d models/dialogue -u models/nlu/current --endpoints endpoints.yml