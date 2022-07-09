#### Question  3


**A company has deployed an API in a VPC behind an internal Application Load Balancer (ALB). An application that

consumes the API as a client is deployed in a second account in private subnets.**


**Which architectural configurations will allow the API to be consumed without using the public Internet?

(Select TWO)**


1: Configure a VPC peering connection between the two VPCs. Access the API using the private address


2: Configure an AWS Direct Connect connection between the two VPCs. Access the API using the private address


3: Configure a ClassicLink connection for the API into the client VPC. Access the API using the ClassicLink address


4: Configure a PrivateLink connection for the API into the client VPC. Access the API using the PrivateLink address


5: Configure an AWS Resource Access Manager connection between the two accounts. Access the API using the private

address


Answer: 1,4


**Explanation:**


You can create your own application in your VPC and configure it as an AWS PrivateLink-powered service

(referred to as an _endpoint service_ ). Other AWS principals can create a connection from their VPC to your endpoint

service using an interface VPC endpoint. You are the _service provider_ , and the AWS principals that create connections

to your service are _service consumers_.


This configuration is powered by AWS PrivateLink and clients do not need to use an internet gateway, NAT device, VPN

connection or AWS Direct Connect connection, nor do they require public IP addresses.


Another option is to use a VPC Peering connection. A VPC peering connection is a networking connection between two VPCs

that enables you to route traffic between them using private IPv4 addresses or IPv6 addresses. Instances in either VPC

can communicate with each other as if they are within the same network. You can create a VPC peering connection between

your own VPCs, or with a VPC in another AWS account.


- CORRECT "Configure a VPC peering connection between the two VPCs. Access the API using the private address" is a

  correct answer.


- CORRECT "Configure a PrivateLink connection for the API into the client VPC. Access the API using the PrivateLink

  address" is also a correct answer.


- INCORRECT "Configure an AWS Direct Connect connection between the two VPCs. Access the API using the private address"

  is incorrect. Direct Connect is used for connecting from on-premises data centers into AWS. It is not used from one

  VPC to another.


- INCORRECT "Configure a ClassicLink connection for the API into the client VPC. Access the API using the ClassicLink

  address" is incorrect. ClassicLink allows you to link EC2-Classic instances to a VPC in your account, within the same

  Region. This is not relevant to sending data between two VPCs.


- INCORRECT "Configure an AWS Resource Access Manager connection between the two accounts. Access the API using the

  private address" is incorrect. AWS RAM lets you share resources that are provisioned and managed in other AWS

  services. However, APIs are not shareable resources with AWS RAM.


**References:**


https://docs.aws.amazon.com/vpc/latest/userguide/endpoint-service.html


https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-

delivery/amazon-vpc/

