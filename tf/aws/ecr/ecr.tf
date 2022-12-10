resource "aws_ecr_repository" "ecr_repository" {
  name = module.config.config.image_name
  force_delete = true
}

data "aws_ecr_repository" "ecr_repository_data" {
  name = module.config.config.image_name
}