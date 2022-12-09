resource "aws_ecr_repository" "my_repo" {
  name = local.config.image_name
  force_delete = true
}

data "aws_ecr_repository" "my_repo_data" {
  name = local.config.image_name
}