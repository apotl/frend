import boto3
from .ecr import ECRRepo

class ECS:

    def __init__(self, repo_name):
        self.ecr_repo = ECRRepo(repo_name)

class Fargate(ECS):

    def __init__(self, repo_name):
        super().__init__(repo_name)