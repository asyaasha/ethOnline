# eth_global_online



## Table of Contents

- [eth\_global\_online](#eth_global_online)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
    - [Setup for Development](#setup-for-development)
  - [Commands](#commands)
    - [Formatting](#formatting)
    - [Linting](#linting)
    - [Testing](#testing)
    - [Locking](#locking)
    - [all](#all)
  - [License](#license)
  
<img width="1434" alt="screen" src="https://github.com/asyaasha/ethOnline/assets/20131841/d897fb77-9e5c-40ec-b93e-d8c11e9456c3">

## Getting Started

```shell
git clone https://github.com/asyaasha/ethOnline.git
```

```shell
cd ethOnline
```

```shell
poetry install && poetry shell
```

0. 

```shell
autonomy packages sync
```

Which should sync up all the agent packages from IPFS

```shell
[2023-10-22 15:40:55,397][INFO] Performing sync @ /home/zarathustra/Projects/test/ethOnline/packages
[2023-10-22 15:40:55,397][INFO] Checking third party packages.
[2023-10-22 15:40:55,397][INFO] (protocol, eightballer/prometheus:1.0.0) not found locally, downloading...
[2023-10-22 15:40:55,720][INFO] (connection, eightballer/prometheus:0.1.1) not found locally, downloading...
[2023-10-22 15:40:55,928][INFO] (protocol, eightballer/http:0.1.0) not found locally, downloading...
[2023-10-22 15:40:56,155][INFO] (protocol, valory/contract_api:1.0.0) not found locally, downloading...
[2023-10-22 15:40:56,460][INFO] (connection, eightballer/http_server:0.1.0) not found locally, downloading...
[2023-10-22 15:40:56,685][INFO] (connection, eightballer/http_client:0.1.0) not found locally, downloading...
[2023-10-22 15:40:56,923][INFO] (protocol, valory/ledger_api:1.0.0) not found locally, downloading...
[2023-10-22 15:40:57,262][INFO] (skill, eightballer/prometheus:0.1.0) not found locally, downloading...
[2023-10-22 15:40:57,501][INFO] (contract, eightballer/erc_20:0.1.0) not found locally, downloading...
[2023-10-22 15:40:57,787][INFO] (protocol, valory/http:0.1.0) not found locally, downloading...
[2023-10-22 15:40:58,050][INFO] (protocol, open_aea/signing:1.0.0) not found locally, downloading...
[2023-10-22 15:40:58,334][INFO] (protocol, eightballer/default:0.1.0) not found locally, downloading...
[2023-10-22 15:40:58,608][INFO] (protocol, eightballer/fipa:0.1.0) not found locally, downloading...
[2023-10-22 15:40:58,882][INFO] Sync complete
```

Now we're all setup and ready to run.

1. To access Grafana / Prometheus:

```shell
docker compose up
```

2. In another terminal: run the agent
 
```shell
make run_agent
```

At this point, one may validate whether the application is running via a simple curl

```shell
curl -X 'POST' 0.0.0.0:5555/claim -H "ContentType: application/json" -d '{"public_address": "0x92e4E69ea99c42337c3ea70a9B6aa1b6c91ba5E2", "ledger_id": "ethereum"}'
{"result": "Address has already claimed today."}
```

Turns out we were greedy during development today 😅


3. And last but not least of all, a third terminal to start the frontend:

```shell
npm install and npm run dev
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

