**Explanation:**

A VPC endpoint enables you to privately connect your VPC to supported AWS services and VPC endpoint services powered by

AWS PrivateLink without requiring an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection.

Instances in your VPC do not require public IP addresses to communicate with resources in the service. Traffic between

your VPC and the other service does not leave the Amazon network.

With a gateway endpoint you configure your route table to point to the endpoint. Amazon S3 and DynamoDB use gateway

endpoints.

The table below helps you to understand the key differences between the two different types of VPC endpoint:

- ✅ :  "Create a gateway VPC endpoint and add an entry to the route table" is the correct answer.

- ❌ :  "Create an interface VPC endpoint in the VPC with an Elastic Network Interface (ENI)" is incorrect. This

  would be used for services that are supported by interface endpoints, not gateway endpoints.

- ❌ :  "Create a private Amazon DynamoDB endpoint and connect to it using an AWS VPN" is incorrect. You cannot

  create an Amazon DynamoDB private endpoint and connect to it over VPN. Private endpoints are VPC endpoints and are

  connected to by instances in subnets via route table entries or via ENIs (depending on which service).

- ❌ :  "Create a software VPN between DynamoDB and the application in the private subnet" is incorrect. You cannot

  create a software VPN between DynamoDB and an application.

**References:**

<https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content>-

delivery/amazon-vpc/

----

- #private_amazon_dynamodb_endpoint #<https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints.html> #aws_vpn #vpc_endpoint_services #gateway_vpc_endpoint
