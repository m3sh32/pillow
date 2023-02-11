from typing import cast
from pathlib import Path
from constructs import Construct
from aws_cdk import (
    Stack,
    CfnOutput,
    aws_lambda as _lambda,
    aws_lambda_python_alpha as pylambda,
    aws_apigatewayv2_alpha as apigw2,
    aws_apigatewayv2_integrations_alpha as integrations,
    aws_apigatewayv2_authorizers_alpha as auth,
)


class ApiStack(Stack):
    """
    Deploy a HTTP API with a Lambda Function Proxy Handler
    """

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:  # type: ignore
        super().__init__(scope, construct_id, **kwargs)

        handler_func = pylambda.PythonFunction(
            self,
            "MilestoneApiServiceProxyHandler",
            entry=str(
                Path(__file__).parents[1].joinpath("src").joinpath("api_handler")
            ),
            runtime=_lambda.Runtime.PYTHON_3_9,
            description="API handler",
        )

        integration = integrations.HttpLambdaIntegration(
            id="LambdaIntegration", handler=cast(_lambda.IFunction, handler_func)
        )

        api = apigw2.HttpApi(
            self,
            "MilestoneApi",
            default_integration=integration,
            description="Milestone Project API",
        )

        auth_func = pylambda.PythonFunction(
            self,
            "MilestoneApiServiceAuthHandler",
            entry=str(
                Path(__file__).parents[1].joinpath("src").joinpath("auth_handler")
            ),
            runtime=_lambda.Runtime.PYTHON_3_9,
            description="API authorizer",
        )

        api.add_routes(
            path="/secret",
            authorizer=auth.HttpLambdaAuthorizer(
                "LambdaAuthorizer",
                handler=cast(_lambda.IFunction, auth_func),
                response_types=[auth.HttpLambdaResponseType.SIMPLE],
            ),
            integration=integration,
        )

        CfnOutput(self, "ApiUrl", value=cast(str, api.url))
