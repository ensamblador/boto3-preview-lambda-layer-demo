
from aws_cdk import (Stack, Duration,  aws_iam as iam, aws_lambda as _lambda)
from constructs import Construct

from layers.layers import Boto3WithCases

BASE_LAMBDA_CONFIG = dict (
    timeout=Duration.seconds(8),       
    memory_size=256,
    tracing= _lambda.Tracing.ACTIVE)

PYTHON_LAMBDA_CONFIG = dict(
    runtime=_lambda.Runtime.PYTHON_3_8,
    handler = 'lambda_function.lambda_handler',
    **BASE_LAMBDA_CONFIG)

class Boto3PreviewLambdaLayerDemoStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)


        boto3_layer = Boto3WithCases(self, 'b3')

        self.lambda_function = _lambda.Function(
            self, "l", **PYTHON_LAMBDA_CONFIG, code=_lambda.Code.from_asset("./lambda"),
            layers= [boto3_layer.layer],
            description='testing Lambda')
        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "Boto3PreviewLambdaLayerDemoQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
