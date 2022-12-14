# Fully Ready Entity oN Discord

GPT3 chatbot + infrastructure to launch it on AWS.

## Dependencies

Make sure you have these installed on your system:

* Docker
* Python3
    * virtualenv (```pip install virtualenv```)
* Terraform
* .aws/config and .aws/credentials filled out with the access key, secret access key, and the region. This is needed for Terraform to function.
* "make", usually installed with the build-essentials package on Debian

## config.yml

Set these properties:

* ```cluster_name```: Name of the Fargate cluster that will be created
* ```image_name```: Name of the ECR repo and the Docker image.
* ```container_name```: Name of the container in the ECS task.
* ```discord_token```: Discord token. Get this from the developer portal
* ```openai_token```: Token from OpenAI
* ```nick```: Nickname the bot will set for itself upon guild join
* ```aws_access_key_id```: AWS access key ID, needed by build.py
* ```aws_secret_access_key```: AWS secret access key, needed by build.py
* ```region_name```: AWS region, needed by build.py
* ```completion_opts```: Request body per OpenAI docs (https://beta.openai.com/docs/api-reference/completions)
    * ```prompt``` property will process special substitutions:
        * ```{self}```: The bot's nickname
        * ```{message}```: The content of the message the bot is responding to
## tf/state.tf

Edit the properties to write the state file. Alternatively, remove this file if you would rather have your state file stored locally.

## Building and deploying

Clone the repo, configure config.yml above, then cd into the repo. Then run the following:

```
make init
make
```

If you configured everything correctly the bot will be connected to discord. Either before or after this step you can invite your bot to the desired guilds using the developer portal.

## Uninstallation

You can remove all the infrastructure and clean up your working directory by running:

```
make destroy
```

## Notes

* ```./build.sh``` is invoked by root because it invokes ```build.py```, which performs operations against the local Docker install. You can remove ```sudo``` from the Makefile if the system user building and deploying this project has permissions to use Docker.