import json
from typing import Any, Dict, Optional, TypedDict
from aws_lambda_typing import context as context_, events, responses


class APIGatewayAuthorizerResponseSimpleV2(
    responses.api_gateway_authorizer.APIGatewayAuthorizerResponse,
    total=False,
):
    """
    Add simple Lambda function response for format 2.0
    https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-lambda-authorizer.html#http-api-lambda-authorizer.v2

    Attributes:
    ----------
    isAuthorized: bool
    """

    isAuthorized: bool


def handler(
    event: events.APIGatewayProxyEventV2, context: context_.Context
) -> APIGatewayAuthorizerResponseSimpleV2:
    """
    HTTP Api Authorizer
    """
    print(event)

    return {
        "isAuthorized": True,
    }
