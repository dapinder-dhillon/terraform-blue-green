terraform {
  backend "s3" {
    bucket  = "dhillonbtstraining"
    key     = "terraform/sit/terraform.tfstate"
    region  = "eu-west-1"
    profile = "aws-bts-training"
  }
  required_version = "= 0.11.7"
}

