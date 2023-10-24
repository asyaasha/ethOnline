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
	find -name 'packages/**/*.db' -exec rm -fr {} +
	rm -fr .idea .history
	rm -fr venv
	rm -rf packages/tmp 
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

start_infra:
	sudo chown -R $(shell whoami):$(shell whoami) ./data/
	docker-compose up --force-recreate -d --remove-orphans grafana prometheus
make_meta:
	adev metadata generate . protocol/eightballer/prometheus/1.0.0 0 && adev -v metadata validate  mints/0.json
	adev metadata generate . connection/eightballer/prometheus/0.1.1 1 && adev -v metadata validate  mints/1.json
	adev metadata generate . skill/eightballer/prometheus/0.1.0 2 && adev -v metadata validate  mints/2.json
	# we need to have the default protocol and the fipa protocol and the contract
	adev metadata generate . protocol/eightballer/default/0.1.0 3 && adev -v metadata validate  mints/3.json
	adev metadata generate . protocol/eightballer/fipa/0.1.0 4 && adev -v metadata validate  mints/4.json
	adev metadata generate . contract/eightballer/erc_20/0.1.0 5 && adev -v metadata validate  mints/5.json
	
	adev metadata generate . skill/eightballer/balance_metrics/0.1.0 6 && adev -v metadata validate  mints/6.json
	adev metadata generate . skill/eightballer/faucet/0.1.0 7 && adev -v metadata validate  mints/7.json
	# agent
	adev metadata generate . agent/eightballer/defi_agent/0.1.0 8 && adev -v metadata validate  mints/8.json
	# service
	adev metadata generate . service/eightballer/multichain_faucet/0.1.0 9 && adev -v metadata validate  mints/9.json

