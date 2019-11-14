#!/usr/bin/env/python
#
# Using the file system load
#
# We now assume we have a file in the same dir as this one called `*.j2`
#

from jinja2 import Environment, FileSystemLoader
import os

# Capture our current directory
THIS_DIR = os.path.dirname(os.path.abspath(__file__))

TABLEAU_VERSION="v1"

def print_html_doc():
    # Create the jinja2 environment.
    # Notice the use of trim_blocks, which greatly helps control whitespace.
    for filename in os.listdir(THIS_DIR):
        if filename.endswith(".j2"):
            j2_env = Environment(loader=FileSystemLoader(THIS_DIR),
                                 trim_blocks=True)
            file_name_with_no_ext = filename[:-6] #removing last 6 chars i.e. .tf.j2
            generated_file_name = file_name_with_no_ext + "-generated.tf"
            j2_env.get_template(filename).stream( version=TABLEAU_VERSION).dump("terraform/"+generated_file_name)

if __name__ == '__main__':
    print_html_doc()


