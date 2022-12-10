module "ecr" {
    source = "../ecr"
  
}

module "networking" {
    source = "../networking"
}

module "config" {
    source = "../../config"
}