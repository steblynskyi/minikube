# Deploy argocd chart via helm, you must be in argocd chart root dir
helm install argocd ./ --version 7.7.7 --create-namespace -n argocd

# Upgrade argocd
    helm upgrade argocd ./ -f ./values.yaml -n argocd

# Delete argocd
    helm delete argocd -n argocd

# Create port-forward if not using ingress and minikube tunnel
    export POD_NAME=$(kubectl get pods --namespace argocd -l "app.kubernetes.io/name=argocd-server" -o jsonpath="{.items[0].metadata.name}") && kubectl --namespace argocd port-forward $POD_NAME 8081

# Get Password for argocd, the output in the terminal as well as copy it to the clipboard
    kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d | tee >(pbcopy)