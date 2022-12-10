# Configure the AWS provider
provider "aws" {
  region = "us-east-1"
}

module "fargate" {
  source = "./aws/fargate"
}