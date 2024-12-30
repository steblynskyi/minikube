# Install brew package manager on your Mac https://brew.sh/
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install the Docker Desktop on your Mac
    brew install --cask docker

# Install Minikube on your Mac
    brew install minikube

# Setup Minikube Cluster
    minikube start --driver=docker --memory=4g --cpus=2 --nodes=3 --addons=ingress,ingress-dns,metrics-server,storage-provisioner

# To Delete Minikube Cluster and Cleanup
    minikube stop
    minikube delete
    rm -rf ~/.minikube
    docker network prune

# Deploy helm charts, argocd, jenkins, grafana, etc.. Please see CMD.md it will explain how to deploy it.

# Need to modify /etc/hosts on your Mac for new dns records
    HOSTS_TO_ADD="# Minikube setup
    127.0.0.1 jenkins.test"

    while read -r line; do
        if ! grep -qF "$line" /etc/hosts; then
            echo "$line" | sudo tee -a /etc/hosts > /dev/null
        fi
    done <<< "$HOSTS_TO_ADD"

# To refresh the DNS cache on your Mac
    sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder
# To confirm that your DNS refresh was successful
    ping grafana.test

# Start Minikube Tunnel to allow accessing the services
    minikube tunnel --cleanup

# Test accessing the services
    curl -I -v http://grafana.test