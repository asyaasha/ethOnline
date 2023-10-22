# Makefile

.PHONY: clean
clean: clean-build clean-pyc clean-test clean-docs

.PHONY: clean-build
clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	rm -fr deployments/build/
	rm -fr deployments/Dockerfiles/open_aea/packages
	rm -fr pip-wheel-metadata
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -fr {} +
	find . -name '*.svn' -exec rm -fr {} +
	find . -name '*.db' -exec rm -fr {} +
	rm -fr .idea .history
	rm -fr venv
	rm -rf tmp 
	rm -rf packages/eightballer/agents/agent
	rm -rf agent

.PHONY: clean-docs
clean-docs:
	rm -fr site/

.PHONY: clean-pyc
clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +
	find . -name '.DS_Store' -exec rm -fr {} +

.PHONY: clean-test
clean-test:
	rm -fr .tox/
	rm -f .coverage
	find . -name ".coverage*" -not -name ".coveragerc" -exec rm -fr "{}" \;
	rm -fr coverage.xml
	rm -fr htmlcov/
	rm -fr .hypothesis
	rm -fr .pytest_cache
	rm -fr .mypy_cache/
	find . -name 'log.txt' -exec rm -fr {} +
	find . -name 'log.*.txt' -exec rm -fr {} +

.PHONY: hashes
hashes: clean
	poetry run autonomy hash all
	poetry run autonomy packages lock
	poetry run autonomy push-all

lint:
	poetry run adev -v -n 0 lint -co

fmt: 
	poetry run adev -n 0 fmt -co

test:
	poetry run adev -v test

all: fmt lint test hashes

run_agent: clean-build
	 bash scripts/run_single_agent.sh eightballer/defi_agent

pull_from_main:
	git checkout main
	rm -rf packages/eightballer 
	rm -rf packages/valory
	rm -rf packages/open_aea
	git checkout packages
	poetry run autonomy packages sync
	
