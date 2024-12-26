# Deploy opensearch chart via helm, you must be in opensearch chart root dir
    helm install opensearch ./ --version 1.5.1 --create-namespace -n opensearch

# Upgrade opensearch
    helm upgrade opensearch ./ -f ./values.yaml -n opensearch

# Delete opensearch
    helm delete opensearch -n opensearch

# Create port-forward if not using ingress and minikube tunnel
    export POD_NAME=$(kubectl get pods --namespace opensearch -l "app.kubernetes.io/name=fluent-bit" -o jsonpath="{.items[0].metadata.name}") && kubectl --namespace opensearch port-forward $POD_NAME 2020

# Get Password for opensearch admin, the output in the terminal as well as copy it to the clipboard
    U: admin
    P: kubectl get pod opensearch-cluster-master-0 -n opensearch -o jsonpath='{.spec.containers[0].env[?(@.name=="OPENSEARCH_INITIAL_ADMIN_PASSWORD")].value}' | tee >(pbcopy)