import json

import yaml

from packages.valory.connections.ledger.base import EVM_LEDGERS

# read in the skill.yaml and check whether the evm_chains are the same
from pathlib import Path

CURRENT_DIR = Path(__file__).parent.absolute()

with open(CURRENT_DIR / "connection.yaml", "r") as f:
    skill_yaml = yaml.safe_load(f)


def test_evm_chains_all_in_skill_yaml():

    for chain in set(EVM_LEDGERS.keys()):
        assert chain in set(
            skill_yaml["config"]["ledger_apis"].keys()
        ), f"{chain} not in skill.yaml"


def get_config_for_evm_chain(evm_chain):
    """
    Read in the data json file and locate the config for the given evm_chain.
    """
    with open(CURRENT_DIR / "chains.json", "r") as f:
        data = json.load(f)

    for value in data:
        if value["name"].lower() == evm_chain:
            return value
        if value["shortName"].lower() == evm_chain:
            return value
        if value["chain"].lower() == evm_chain:
            return value

    print(f"Could not find config for {evm_chain} in chains.json")


def get_chain_info(chain_name):
    print()
    print("Config for EVM chains:")
    config = get_config_for_evm_chain(chain_name)
    if config:
        config = {
            chain_name: {
                "address": config["rpc"][0],
                "chain_id": config["chainId"],
                "default_gas_price_strategy": "eip1559",
                "gas_price_strategies": "*id001",
                "is_gas_estimation_enabled": True,
                "poa_chain": False,
            }
        }
        print(yaml.dump(config))
    print()

def get_as_ledger(chain_name):
    print()
    print("Config for EVM chains:")
    config = get_config_for_evm_chain(chain_name)
    chain_id =  config["chainId"]
    explorer_uri = config["explorers"].pop()['name']
    native_currency = config["nativeCurrency"]["symbol"]
    template = f"""
Ledger(
    ledger_id="{chain_name}",
    chain_id={chain_id},
    chain_name="{chain_name}",
    explorer_url="{explorer_uri}",
    native_currency="{native_currency}",
)
"""
    print(template)




for chains in [
    "celo",
    "bsc",
    "canto",
    "matic",
    "zksync",
    "arb1",
    "avax",
    "op mainnet",
    "base",
    "gnosis",
    "fantom opera",
    "filecoin",
    "mantle",
    "spark",
    "scroll",


]:
    get_chain_info(chains)
    try:
        get_as_ledger(chains)
    except:
        pass
