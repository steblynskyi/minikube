# Deploy jenkins chart via helm, you must be in jenkins chart root dir
    helm install jenkins ./ --version 5.7.21 --create-namespace -n jenkins

# Upgrade jenkins
    helm upgrade jenkins ./ -f ./values.yaml -n jenkins

# Delete jenkins
    helm delete jenkins -n jenkins

# Create port-forward if not using ingress and minikube tunnel
    export POD_NAME=$(kubectl get pods --namespace jenkins -l "app.kubernetes.io/name=jenkins" -o jsonpath="{.items[0].metadata.name}") && kubectl --namespace jenkins port-forward $POD_NAME 8081:8080

# Get Password for jenkins admin, the output in the terminal as well as copy it to the clipboard
    U: admin
    P: kubectl get secret --namespace jenkins jenkins -o jsonpath="{.data.jenkins-admin-password}" | base64 -d | tee >(pbcopy)