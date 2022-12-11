import boto3
import base64

def get_docker_login():
    ecr_client = boto3.client('ecr')

    response = ecr_client.get_authorization_token()

    b64result = response['authorizationData'][0]['authorizationToken']
    docker_username, docker_password = base64.b64decode(b64result).decode('utf8').split(':')

    return docker_username, docker_password

class ECRRepo:

    def __init__(self, repo_name):
        ecr_client = boto3.client('ecr')

        self.repo_name = repo_name

        try:
            self.repo_uri = ecr_client.describe_repositories(repositoryNames=[repo_name])['repositories'][0]['repositoryUri']
        except ecr_client.exceptions.RepositoryNotFoundException:
            self.repo_uri = ecr_client.create_repository(repositoryName=repo_name)['repository']['repositoryUri']

        self.registry_uri = self.repo_uri.split('/')[0]
    