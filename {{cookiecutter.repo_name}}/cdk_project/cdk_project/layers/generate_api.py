from aws_cdk import (
    aws_apigatewayv2 as apigateway,
    aws_apigatewayv2_integrations as Integration,
    aws_lambda as lambda_,
    Duration
)
from constructs import Construct
from app.config import LAMDA_PYTHON_VERSION

from typing import Tuple, Dict


def generate_api(scope: Construct, dependenciesLayer: lambda_.LayerVersion, env: Dict[str, str]) -> Tuple[apigateway.HttpApi, lambda_.Function]:

    api = apigateway.HttpApi(scope, "mobile/v1")
    fn = lambda_.Function(scope, "mobile-api-handler", runtime=LAMDA_PYTHON_VERSION,
      code =lambda_.Code.from_asset("./lambda_layer/"),
      handler="api.handler.handler",
      layers=[dependenciesLayer,  lambda_.LayerVersion.from_layer_version_arn(
               scope, "WebAdapterLayer",
               "arn:aws:lambda:us-east-1:753240598075:layer:LambdaAdapterLayerX86:25" # <-- Replace with actual ARN
           )], environment=env, timeout=Duration.seconds(30), memory_size=256)

    api.add_routes(path="/mobile-api/{proxy+}", methods=[apigateway.HttpMethod.ANY],
                   integration=Integration.HttpLambdaIntegration("mobile-api-handler", handler = fn))
    return api,fn
