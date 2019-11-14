#!/usr/bin/env/python
#
# Using the file system load
#
# We now assume we have a file in the same dir as this one called
# test_template.html
#

from jinja2 import Environment, FileSystemLoader
import os

# Capture our current directory
THIS_DIR = os.path.dirname(os.path.abspath(__file__))

TABLEAU_VERSION="v1"

def print_html_doc():
    # Create the jinja2 environment.
    # Notice the use of trim_blocks, which greatly helps control whitespace.
    j2_env = Environment(loader=FileSystemLoader(THIS_DIR),
                         trim_blocks=True)
    j2_env.get_template('ec2.tf.j2').stream( version=TABLEAU_VERSION).dump("terraform/ec2-generated.tf")

   # print j2_env.get_template('ec2.tf.j2').render(
    #    version='dapinder_100'
    #)

if __name__ == '__main__':
    print_html_doc()


