# Deploy fluentbit chart via helm, you must be in fluentbit chart root dir
    helm install fluentbit ./ --version 3.2.2 --create-namespace -n fluentbit

# Upgrade fluentbit
    helm upgrade fluentbit ./ -f ./values.yaml -n fluentbit

# Delete fluentbit
    helm delete fluentbit -n fluentbit

# Create port-forward if not using ingress and minikube tunnel
    export POD_NAME=$(kubectl get pods --namespace fluentbit -l "app.kubernetes.io/name=fluent-bit" -o jsonpath="{.items[0].metadata.name}") && kubectl --namespace fluentbit port-forward $POD_NAME 2020