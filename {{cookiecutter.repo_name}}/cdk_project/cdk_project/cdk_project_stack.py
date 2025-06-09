from aws_cdk import (
    Stack
)
from constructs import Construct

from .layers import generate_api, generate_dependencies

class CdkProjectStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)


        dep_layer = generate_dependencies.generate_dependencies_layer(self)
        generate_api.generate_api(self,"../api",dep_layer, {})
