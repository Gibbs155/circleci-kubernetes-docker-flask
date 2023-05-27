FROM python:3.9-slim as build-env
ADD src /src

FROM python:3.9-slim
WORKDIR /app
COPY --from=build-env /src /app
RUN pip install --no-cache-dir -r /app/requirements.txt
EXPOSE 8080
CMD ["python", "/app/main.py"]

# FROM golang:alpine as build-env
# ADD src /src 
# RUN cd /src && go build -o demo-app main.go

# FROM alpine 
# WORKDIR /app 
# COPY --from=build-env /src/demo-app /app/
# EXPOSE 8080
# ENTRYPOINT ./demo-app
