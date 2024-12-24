# Deploy prometheus chart via helm, you must be in prometheus chart root dir
helm install prometheus ./ --version 26.0.0 --create-namespace -n prometheus

# Upgrade prometheus
  helm upgrade prometheus ./ -f ./values.yaml -n prometheus

# Delete prometheus
  helm delete prometheus -n prometheus

# Create port-forward for prometheus server if not using ingress and minikube tunnel
export POD_NAME=$(kubectl get pods --namespace prometheus -l "app.kubernetes.io/name=prometheus,app.kubernetes.io/instance=prometheus" -o jsonpath="{.items[0].metadata.name}") && kubectl --namespace prometheus port-forward $POD_NAME 9090

# Create port-forward for prometheus pushgateway if not using ingress and minikube tunnel
export POD_NAME=$(kubectl get pods --namespace prometheus -l "app.kubernetes.io/name=prometheus-pushgateway" -o jsonpath="{.items[0].metadata.name}") && kubectl --namespace prometheus port-forward $POD_NAME 9091

# Create port-forward for prometheus alertmanager if not using ingress and minikube tunnel
export POD_NAME=$(kubectl get pods --namespace prometheus -l "app.kubernetes.io/name=alertmanager,app.kubernetes.io/instance=prometheus" -o jsonpath="{.items[0].metadata.name}") && kubectl --namespace prometheus port-forward $POD_NAME 9093