# PARTE 1
# Instalar Docker previamente
docker login
docker build -t lexact/flask-circleci:latest .
docker push lexact/flask-circleci:latest


# Instalar kubernetes previamente ( minikube y kubectl para esta demo)
minikube start
kubectl apply -f .

# Verificar la implementacion en el pod
kubectl exec -it  pod/demoapp-5d9f7cb598-496r6 -- /bin/sh
apt update
apt install curl
curl http://localhost:8080
<!-- {"message":"Hello World! (Version info: 1.00, build date: 21/05/2023)"} -->

# Verificar la implementacion a  traves del servicio
minikube service demoapp
<!-- |-----------|---------|-------------|---------------------------|
| NAMESPACE |  NAME   | TARGET PORT |            URL            |
|-----------|---------|-------------|---------------------------|
| default   | demoapp |          80 | http://192.168.49.2:32409 |
|-----------|---------|-------------|---------------------------| -->
curl http://192.168.49.2:32409

<!-- minikube tunnel -->


# PARTE 2
# Creando repositorio de github
git init
git add .
git commit -m "Primer commit"
git remote add origin https://github.com/Gibbs155/circleci-kubernetes-docker-flask
git push -u origin master

# Configurar entorno circleci   <-->  https://circleci.com/
