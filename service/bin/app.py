#!/usr/bin/env python3
import os
import sys
import aws_cdk as cdk


sys.path.append(
    os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
)

from lib.api_stack import ApiStack

app = cdk.App()

ApiStack(
    app,
    "ApiStack",
    env=cdk.Environment(
        account=os.getenv("CDK_DEFAULT_ACCOUNT"), region=os.getenv("CDK_DEFAULT_REGION")
    ),
)

app.synth()
