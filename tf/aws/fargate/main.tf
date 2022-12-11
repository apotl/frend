module "ecr" {
    source = "../ecr"
  
}

module "networking" {
    source = "../networking"
}

module "config" {
    source = "../../config"
}

locals {
  configdata = module.config.data.deployment.ecs
}