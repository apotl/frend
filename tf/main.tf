# Configure the AWS provider
provider "aws" {
  region = "us-east-1"
}

data "aws_region" "current" {}