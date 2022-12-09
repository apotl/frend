# Create a new Fargate cluster
resource "aws_ecs_cluster" "fargate_cluster" {
  name = local.config["cluster_name"]
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
  family = local.config["image_name"]
  container_definitions = data.template_file.container_definitions.rendered
  requires_compatibilities = ["FARGATE"]
  execution_role_arn = aws_iam_role.ecs_execution_role.arn
  network_mode = "awsvpc"
  memory = 512
  cpu = 256
}

# Create a new Fargate service that will run the task on the cluster
resource "aws_ecs_service" "fargate_service" {
  name = local.config["image_name"]
  cluster = aws_ecs_cluster.fargate_cluster.id
  task_definition = aws_ecs_task_definition.fargate_task.arn
  desired_count = 1
  force_new_deployment = true
  launch_type = "FARGATE"
  network_configuration {
    subnets = [aws_subnet.fargate_subnet.id]
    security_groups = [aws_security_group.ecs_service.id]
    assign_public_ip = true
  }
}

data template_file "container_definitions" {
  template = "${file("${path.module}/container-definitions.json")}"
  vars = {
    image_name = data.aws_ecr_repository.my_repo_data.repository_url
    container_name = local.config["container_name"]
    image_tag = var.image_tag
    region = data.aws_region.current.name
  }
}