#!/bin/bash
export FRENDCONFIG="$1"
set -e

python3 -m venv venv
source ./venv/bin/activate
pip3 install docker pyyaml boto3

python3 ./main.py "${FRENDCONFIG}"

export AWS_SHARED_CREDENTIALS_FILE=$(readlink -f ~/.aws/credentials)
export AWS_CONFIG_FILE=$(readlink -f ~/.aws/config)

sudo --preserve-env=PATH,VIRTUAL_ENV,FRENDCONFIG,\
AWS_CONFIG_FILE,AWS_SHARED_CREDENTIALS_FILE\
    python3 ./main.py -d "${FRENDCONFIG}"