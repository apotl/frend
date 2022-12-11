resource "aws_ecr_repository" "ecr_repository" {
  name = local.configdata.image_name
  force_delete = true
}

data "aws_ecr_repository" "ecr_repository_data" {
  name = local.configdata.image_name
}