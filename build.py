import boto3
import docker
import yaml
import base64
import os

config = {} 

with open('config.yml') as configf:
    config = yaml.safe_load(configf)

os.environ['AWS_ACCESS_KEY_ID']=config['aws_access_key_id']
os.environ['AWS_SECRET_ACCESS_KEY']=config['aws_secret_access_key']
os.environ['AWS_DEFAULT_REGION']=config['region_name']

# Get ECR client
ecr_client = boto3.client('ecr')

try:
    repo_name = ecr_client.describe_repositories(repositoryNames=[config['image_name']])
except ecr_client.exceptions.RepositoryNotFoundException:
    ecr_client.create_repository(repositoryName=config['image_name'])

b64result = ecr_client.get_authorization_token(
    )['authorizationData'][0]['authorizationToken']
docker_username, docker_password = base64.b64decode(b64result).decode('utf8').split(':')

acct_id = boto3.client('sts').get_caller_identity()["Account"]

registry = '{0}.dkr.ecr.{1}.amazonaws.com'.format(acct_id, config['region_name'])
tag='{0}/{1}'.format(registry, config['image_name'])

client = docker.from_env()

# Build Docker image
image, build_log = client.images.build(
    path='./',
    dockerfile='./app/Dockerfile',
    tag=tag)

# Push Docker image to ECR
client.login(username=docker_username, password=docker_password, registry=registry)
result = client.images.push(
    repository=tag
)
print(result)