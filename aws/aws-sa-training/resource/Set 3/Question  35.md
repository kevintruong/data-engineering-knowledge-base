#### Question  35


**You have created an application in a VPC that uses a Network Load Balancer (NLB). The application will be offered in a

service provider model for AWS principals in other accounts within the region to consume. Based on this model, what AWS

service will be used to offer the service for consumption?**


1: IAM Role Based Access Control


2: Route 53


3: VPC Endpoint Services using AWS PrivateLink


4: API Gateway


Answer: 3


**Explanation:**


An Interface endpoint uses AWS PrivateLink and is an elastic network interface (ENI) with a private IP address that

serves as an entry point for traffic destined to a supported service.


Using PrivateLink you can connect your VPC to supported AWS services, services hosted by other AWS accounts (VPC

endpoint services), and supported AWS Marketplace partner services.


- CORRECT "VPC Endpoint Services using AWS PrivateLink" is the correct answer.


- INCORRECT "IAM Role Based Access Control" is incorrect as this provides authorization.


- INCORRECT "Route 53" is incorrect as this service provides DNS resolution.


- INCORRECT "API Gateway" is incorrect as this service is used for hosting REST and Websocket APIs.


**References:**


https://docs.aws.amazon.com/vpc/latest/userguide/endpoint-service.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-

delivery/amazon-vpc/

