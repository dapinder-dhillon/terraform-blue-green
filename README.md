# Blue Green Deployment Using Terraform - Fully automated

The project automatically scans all template files(`*.j2`) through the current directory and generates corresponding terraform files.
The generated .tf files are following a convention of getting suffix i.e. `-generated.tf` and the same is being git ignored. 
So git will never prompt you to check-in those files and they wont make it to the git.

### Pre-requisites
 - Python
 - pipenv
 
### Commands/Execution Flow
 - `pipenv install` (This will install all packages defined in Pipfile)
 - `pipenv shell` or `pipenv run {{COMMAND}}` (To start your virtual env or run command against it)
 - `python jinja2_template_load.py` (execute your python code, this will create .tf)
 - `cd terraform`
 - `terraform init`
 - `terraform plan`
 - `terraform apply`
 
 The VERSION is currently specified as a variable in `jinja2_template_load.py` but can always be externalized.