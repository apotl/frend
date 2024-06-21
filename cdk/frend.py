from constructs import Construct
from aws_cdk import (
    App,
    Stack,
    aws_lambda,
    aws_apigatewayv2,
    aws_apigatewayv2_integrations,
)


class FrendStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        lambda_function = aws_lambda.Function(
            self,
            "lambda-function",
            code=aws_lambda.Code.from_asset("src/"),
            handler="handler.main",
            runtime=aws_lambda.Runtime.PYTHON_3_12,
        )

        api = aws_apigatewayv2.HttpApi(self, "api")

        api.add_routes(
            path="/event",
            integration=aws_apigatewayv2_integrations.HttpLambdaIntegration(
                "lambda-integration", lambda_function
            ),
            methods=[aws_apigatewayv2.HttpMethod.POST],
        )
