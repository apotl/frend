# Create a new Fargate cluster
resource "aws_ecs_cluster" "fargate_cluster" {
  name = local.configdata.cluster_name
}

resource "aws_ecs_cluster_capacity_providers" "capacity_providers" {
  cluster_name = aws_ecs_cluster.fargate_cluster.name

  capacity_providers = ["FARGATE"]

  default_capacity_provider_strategy {
    base              = 1
    weight            = 100
    capacity_provider = "FARGATE"
  }
}

# Define the task that will run on the Fargate cluster
resource "aws_ecs_task_definition" "fargate_task" {
  family = local.configdata.container_name
  container_definitions = data.template_file.container_definitions.rendered
  requires_compatibilities = ["FARGATE"]
  execution_role_arn = aws_iam_role.ecs_execution_role.arn
  network_mode = "awsvpc"
  memory = 512
  cpu = 256
}

# Create a new Fargate service that will run the task on the cluster
resource "aws_ecs_service" "fargate_service" {
  name = local.configdata.container_name
  cluster = aws_ecs_cluster.fargate_cluster.id
  task_definition = aws_ecs_task_definition.fargate_task.arn
  desired_count = 1
  force_new_deployment = true
  wait_for_steady_state = true
  deployment_minimum_healthy_percent = 0
  deployment_maximum_percent = 100
  launch_type = "FARGATE"
  network_configuration {
    subnets = [module.networking.subnet]
    security_groups = [module.networking.security_group]
    assign_public_ip = true
  }
}

data template_file "container_definitions" {
  template = "${file("${path.module}/container-definitions.json")}"
  vars = {
    image_name = module.ecr.repository_url
    container_name = local.configdata.container_name
    image_tag = var.image_tag
    region = data.aws_region.current.name
  }
}

data "aws_region" "current" {}