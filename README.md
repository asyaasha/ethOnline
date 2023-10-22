# eth_global_online



## Table of Contents

- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Setup for Development](#setup-for-development)
- [Usage](#usage)
- [Commands](#commands)
  - [Testing](#testing)
  - [Linting](#linting)
  - [Formatting](#formatting)
  - [Releasing](#releasing)
- [License](#license)
  
<img width="1434" alt="screen" src="https://github.com/asyaasha/ethOnline/assets/20131841/d897fb77-9e5c-40ec-b93e-d8c11e9456c3">

## Getting Started

git clone https://github.com/asyaasha/ethOnline.git

cd ethOnline
```shell
poetry install && poetry shell
```

to access grafana / prometheus: 
```shell
docker compose up
``` 

to  the agent in another terminal tab run: 
```shell
make run_agent
``` 

in third one to start the frontend:
```shell
npm install and npm run dev
``` 

### Installation

Install `eth_global_online` with pip:

```shell
pip install eth_global_online
```

### Setup for Development

If you're looking to contribute or develop with `eth_global_online`, get the source code and set up the environment:

```shell
git clone https://github.com/eightballer/eth_global_online
cd eth_global_online
poetry install && poetry shell
```

## Commands

Here are common commands you might need while working with the project:

### Formatting

```shell
make fmt
```

### Linting

```shell
make lint
```

### Testing

```shell
make test
```

### Locking

```shell
make hashes
```

### all

```shell
make all
```

## License

This project is licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)

