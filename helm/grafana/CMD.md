# Deploy grafana chart via helm, you must be in grafana chart root dir
    helm install grafana ./ --version 8.6.4 --create-namespace -n grafana

# Upgrade grafana
    helm upgrade grafana ./ -f ./values.yaml -n grafana

# Delete grafana
    helm delete grafana -n grafana

# Create port-forward if not using ingress and minikube tunnel
    export POD_NAME=$(kubectl get pods --namespace grafana -l "app.kubernetes.io/name=grafana,app.kubernetes.io/instance=grafana" -o jsonpath="{.items[0].metadata.name}") && kubectl --namespace grafana port-forward $POD_NAME 3000

# Get Password for grafana admin, the output in the terminal as well as copy it to the clipboard
    U: admin
    P: kubectl get secret --namespace grafana grafana -o jsonpath="{.data.admin-password}" | base64 -d | tee >(pbcopy)