#! /bin/bash
# Start the MAS service.

set -e

echo "Using autonomy version: $(autonomy --version)"

# we check if the service alias is already used
# if it is, we hard exit
if [ -d "service" ]; then
    echo "Service $1 already exists at path ./service"
    exit 1
fi
echo "-----------------------------"
echo "Starting service $1"

# if the service name is not set, we hard exit
if [ -z "$1" ]; then
    echo "Service name is not set!"
    exit 1
fi

autonomy fetch --service $1 --local --alias service
cd service 
autonomy build-image --version latest
docker tag eightballer/oar-defi_agent:latest 8ball030/oar-defi_agent:latest
docker push 8ball030/oar-defi_agent:latest

# if the the --run flag is set, we run the service

if [ -z "$MAS_KEYPATH" ]; then
    echo "MAS_KEYPATH is not set!"
    exit 1
fi
echo "-----------------------------"
echo "Using keys: $MAS_KEYPATH"
export MAS_ADDRESS=$(echo -n $(cat $MAS_KEYPATH | jq '.[].address' -r))
echo "Using Address: $MAS_ADDRESS"
autonomy deploy build $MAS_KEYPATH --kubernetes --image-version latest

echo "-----------------------------"
# we need to replace `eightballer/oar-defi_agent` with `8ball030/oar-defi_agent` in the folder `abci_build`
sed -i 's/eightballer\/oar-defi_agent/8ball030\/oar-defi_agent/g' abci_build/build.yaml

# we also need to replace `nfs-ephemeral` with `local-path`
sed -i 's/nfs-ephemeral/local-path/g' abci_build/build.yaml
echo "Service $1 built!"