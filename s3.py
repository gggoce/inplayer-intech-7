from aws_cdk import (
    aws_s3 as s3,
    core
)


class CdkWorkshopStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        
        bucket = s3.Bucket(self, 
            "MyFirstBucket",
            bucket_name="aws-wide-unique-name-CHANGE-THIS",
            versioned=True,
            removal_policy = core.RemovalPolicy.DESTROY,)

# The code that defines your stack goes here

# useful documentation:
# https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_s3/Bucket.html
# https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.core/RemovalPolicy.html#aws_cdk.core.RemovalPolicy
