# Import the data from the YAML file
data "template_file" "config" {
  template = "${file("../config.yml")}"
}

# Decode the YAML data and store it in a local
locals {
  config = "${yamldecode(data.template_file.config.rendered)}"
}