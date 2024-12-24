# Setup Minikube Cluster
    minikube start --driver=docker --memory=4g --cpus=2 --nodes=3 --addons=ingress,ingress-dns,metrics-server,storage-provisioner

# Delete Minikube Cluster and Cleanup
    minikube stop
    minikube delete
    rm -rf ~/.minikube
    docker network prune

# Start Minikube Tunel to access services
    minikube tunnel --cleanup