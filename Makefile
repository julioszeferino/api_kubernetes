

upapi:
	kubectl create namespace api && \
    kubectl apply -f kubernetes/api-deployment.yaml -n api && \
	kubectl apply -f kubernetes/api-service.yaml -n api

downapi:
	kubectl delete -f kubernetes/api-deployment.yaml -n api && \
	kubectl delete -f kubernetes/api-service.yaml -n api && \
	kubectl delete namespace api