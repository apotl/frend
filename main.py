#!/usr/bin/env python3
import yaml
import os
import argparse

import buildtools.platform as platform
from buildtools.docker import Image

parser = argparse.ArgumentParser()
parser.add_argument('config_path', type=str,
    help="path to the config file.", default='config.yml')
parser.add_argument('-d', '--run-docker-routines',
    help="run Docker routines", action='store_true')
parser.add_argument('-P', '--no-run-platform-prep',
    help="do not run platform prep routines", action='store_true')

args = parser.parse_args()

with open(args.config_path) as configf:
    config = yaml.safe_load(configf)

"""
os.environ['AWS_ACCESS_KEY_ID']=config['aws_access_key_id']
os.environ['AWS_SECRET_ACCESS_KEY']=config['aws_secret_access_key']
os.environ['AWS_DEFAULT_REGION']=config['region_name']
"""

if not args.no_run_platform_prep:
    fargate = platform.aws.ecs.Fargate(config['deployment']['ecr']['image_name'])

if args.run_docker_routines:

    image = Image(args.config_path, fargate.ecr_repo.repo_uri)
    image.build()
    image.push(
        fargate.ecr_repo.registry_uri,
        login=platform.aws.ecr.get_docker_login()
    )
