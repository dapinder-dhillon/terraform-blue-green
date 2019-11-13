#--------------------------------------------------------------
# EC2 Instance
#--------------------------------------------------------------

data "aws_ami" "tio_centos7_most_recent_v1" {
  most_recent = true

  filter {
    name   = "name"
    values = ["*tio_base_centos7*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
  owners = ["702267635140"] # Canonical
}

resource "aws_instance" "ec2" {

  ami           = "${data.aws_ami.tio_centos7_most_recent_v1.id}"
  instance_type = "t2.micro"

  tags {
    Name            = "dhillon-test-terraform-blue-green_v1"
  }
  subnet_id     = "subnet-0a57f42061dab6bb2"
}