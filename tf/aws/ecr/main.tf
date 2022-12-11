module "config" {
    source = "../../config"
}

locals {
  configdata = module.config.data.deployment.ecr
}