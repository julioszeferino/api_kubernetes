docker build -f docker/fastapi.dockerfile -t julioszeferino/fastapi:v1 .
docker login --username=julioszeferino
docker image push julioszeferino/fastapi:v1

kubectl create namespace api

kubectl apply -f kubernetes/api-deployment.yaml -n api
kubectl apply -f kubernetes/api-service.yaml -n api

http://192.168.49.2:30001/

kubectl delete pods --all -n api
kubectl delete service --all -n api
kubectl delete namespace api
