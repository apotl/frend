# Import the data from the YAML file
data "template_file" "config" {
  template = "${file(local.fullloc)}"
}

# Decode the YAML data and store it in a local
locals {
  fullloc = "../${var.config_file_location}"
  config = "${yamldecode(data.template_file.config.rendered)}"
}