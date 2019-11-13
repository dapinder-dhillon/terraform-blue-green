# Blue Green Deployment Using Terraform - Fully automated


Commands/Execution Flow
 - pipenv install (This will install all packages defined in Pipfile)
 - pipenv shell or pipenv run <<COMMAND>> (To start your virtual env or run command against it)
 - python jinja2_template_load.py (execute your python code, this will create .tf)
 - terraform init
 - terraform plan
 - terraform apply