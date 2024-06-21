#!/usr/bin/env python3
import os

import aws_cdk

from cdk.frend import FrendStack
import yaml

CONFIG = yaml.safe_load(open("config.yml").read())
AWS_REGION = CONFIG["frend"]["deployment"]["aws"]["region"]

app = aws_cdk.App()
FrendStack(app, "FrendStack", env={"region": AWS_REGION})

app.synth()
