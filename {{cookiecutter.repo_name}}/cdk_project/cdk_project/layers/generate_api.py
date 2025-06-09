from aws_cdk import (
    aws_lambda as lambda_,
    Duration
)
from constructs import Construct
from ..config import LAMDA_PYTHON_VERSION

from typing import Tuple, Dict


def generate_api(scope: Construct,path: str, dependenciesLayer: lambda_.LayerVersion, env: Dict[str, str]) ->  lambda_.Function:

    fn = lambda_.Function(scope, "mobile-api-handler", runtime=LAMDA_PYTHON_VERSION,
      code =lambda_.Code.from_asset(path),
      handler="api.handler.handler",
      layers=[dependenciesLayer,  lambda_.LayerVersion.from_layer_version_arn(
               scope, "WebAdapterLayer",
               "arn:aws:lambda:us-east-1:753240598075:layer:LambdaAdapterLayerX86:25" # <-- Replace with actual ARN
           )], environment=env, timeout=Duration.seconds(30), memory_size=256)

    return fn
