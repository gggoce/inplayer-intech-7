from aws_cdk import (
    aws_ec2 as ec2,
    core
)


class CdkWorkshopStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        
        vpc = ec2.Vpc(
            self, 
            "VPC",
            max_azs=1,
            nat_gateways=1,
            cidr="192.168.0.0/20",
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="public", cidr_mask=24, subnet_type=ec2.SubnetType.PUBLIC),
                ec2.SubnetConfiguration(
                    name="private", cidr_mask=24, subnet_type=ec2.SubnetType.PRIVATE)

    ])
        core.Tag.add(vpc, "Cost", "Testing")

 # The code that defines your stack goes here
 
 # useful documentation:        
 # https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_ec2/Vpc.html        
        
