import json
from constructs import Construct

from aws_cdk import (
    aws_lambda

)

class Boto3WithCases (Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #layer con beautiful soup y requests
        boto3_cases = aws_lambda.LayerVersion(
            self, "boto3_cases", code=aws_lambda.Code.from_asset("./boto3-preview-sdk/boto3-custom.zip"),
            compatible_runtimes = [aws_lambda.Runtime.PYTHON_3_8,aws_lambda.Runtime.PYTHON_3_7], 
            description = 'boto3 con cases sdk')

        
        self.layer = boto3_cases