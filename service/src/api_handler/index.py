import json
from aws_lambda_typing import context as context_, events, responses


def handler(
    event: events.APIGatewayProxyEventV2, context: context_.Context
) -> responses.APIGatewayProxyResponseV2:
    """
    HTTP Api Proxy Handler
    """

    print(event)

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(event),
    }
