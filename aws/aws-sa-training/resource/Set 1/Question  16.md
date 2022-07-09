#### Question  16


**An Amazon VPC contains several Amazon EC2 instances. The instances need to make API calls to Amazon DynamoDB. A

solutions architect needs to ensure that the API calls do not traverse the internet.**


**How can this be accomplished? (Select TWO)**


1: Create a route table entry for the endpoint


2: Create a gateway endpoint for DynamoDB


3: Create a new DynamoDB table that uses the endpoint


4: Create an ENI for the endpoint in each of the subnets of the VPC


5: Create a VPC peering connection between the VPC and DynamoDB


Answer: 1, 2


**Explanation:**


Amazon DynamoDB and Amazon S3 support gateway endpoints, not interface endpoints. With a gateway endpoint you create the

endpoint in the VPC, attach a policy allowing access to the service, and then specify the route table to create a route

table entry in.


- CORRECT "Create a route table entry for the endpoint" is a correct answer.


- CORRECT "Create a gateway endpoint for DynamoDB" is also a correct answer.


- INCORRECT "Create a new DynamoDB table that uses the endpoint" is incorrect as it is not necessary to create a new

  DynamoDB table.


- INCORRECT "Create an ENI for the endpoint in each of the subnets of the VPC" is incorrect as an ENI is used by an

  interface endpoint, not a gateway endpoint.


- INCORRECT "Create a VPC peering connection between the VPC and DynamoDB" is incorrect as you cannot create a VPC

  peering connection between a VPC and a public AWS service as public services are outside of VPCs.


**References:**


https://docs.aws.amazon.com/vpc/latest/userguide/vpce-gateway.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-

delivery/amazon-vpc/

