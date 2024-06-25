import boto3
import docker
import yaml
import base64
import os
import requests
import ollama

config = {}
modelfile = ""

with open("config.yml") as configf:
    config = yaml.safe_load(configf)

with open("Modelfile") as modelfilef:
    modelfile = modelfilef.read()

ollama_url = config["ollama_url"]

r = requests.post(
    f"{ollama_url}/api/create",
    json={"name": config["image_name"], "modelfile": modelfile, "stream": False},
)
print(r.text)

client = docker.from_env()

# Build Docker image
image, build_log = client.images.build(
    path="./", dockerfile="./app/Dockerfile", tag="frend"
)
