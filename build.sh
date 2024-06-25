#!/bin/bash
set -e

python3 -m venv venv
source ./venv/bin/activate
pip3 install docker pyyaml boto3 ollama discord.py requests pre-commit

python3 ./build.py
