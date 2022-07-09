#### Question  30


**A company wishes to restrict access to their Amazon DynamoDB table to specific, private source IP addresses from their

VPC. What should be done to secure access to the table?**


1: Create an interface VPC endpoint in the VPC with an Elastic Network Interface (ENI)


2: Create a gateway VPC endpoint and add an entry to the route table


3: Create the Amazon DynamoDB table in the VPC


4: Create an AWS VPN connection to the Amazon DynamoDB endpoint


Answer: 2


**Explanation:**


There are two different types of VPC endpoint: interface endpoint, and gateway endpoint. With an interface endpoint you

use an ENI in the VPC. With a gateway endpoint you configure your route table to point to the endpoint. Amazon S3 and

DynamoDB use gateway endpoints. This solution means that all traffic will go through the VPC endpoint straight to

DynamoDB using private IP addresses.


- CORRECT "Create a gateway VPC endpoint and add an entry to the route table" is the correct answer.


- INCORRECT "Create an interface VPC endpoint in the VPC with an Elastic Network Interface (ENI)" is incorrect. As

  mentioned above, an interface endpoint is not used for DynamoDB, you must use a gateway endpoint.


- INCORRECT "Create the Amazon DynamoDB table in the VPC" is incorrect. You cannot create a DynamoDB table in a VPC, to

  connect securely using private addresses you should use a gateway endpoint instead.


- INCORRECT "Create an AWS VPN connection to the Amazon DynamoDB endpoint" is incorrect. You cannot create an AWS VPN

  connection to the Amazon DynamoDB endpoint.


**References:**


https://docs.amazonaws.cn/en_us/vpc/latest/userguide/vpc-endpoints-ddb.html


https://aws.amazon.com/premiumsupport/knowledge-center/iam-restrict-calls-ip-addresses/


https://aws.amazon.com/blogs/aws/new-vpc-endpoints-for-dynamodb/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-

delivery/amazon-vpc/

