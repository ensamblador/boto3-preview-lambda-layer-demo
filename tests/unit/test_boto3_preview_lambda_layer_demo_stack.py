import aws_cdk as core
import aws_cdk.assertions as assertions

from boto3_preview_lambda_layer_demo.boto3_preview_lambda_layer_demo_stack import Boto3PreviewLambdaLayerDemoStack

# example tests. To run these tests, uncomment this file along with the example
# resource in boto3_preview_lambda_layer_demo/boto3_preview_lambda_layer_demo_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Boto3PreviewLambdaLayerDemoStack(app, "boto3-preview-lambda-layer-demo")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
