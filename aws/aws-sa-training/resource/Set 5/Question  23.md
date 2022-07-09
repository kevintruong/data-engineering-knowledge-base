#### Question  23


**An application is running on EC2 instances in a private subnet of an Amazon VPC. A Solutions Architect would like to

connect the application to Amazon API Gateway. For security reasons, it is necessary to ensure that no traffic traverses

the Internet and to ensure all traffic uses private IP addresses only.**


**How can this be achieved?**


1: Create a NAT gateway


2: Create a public VIF on a Direct Connect connection


3: Create a private API using an interface VPC endpoint


4: Add the API gateway to the subnet the EC2 instances are located in


**Answer: 3**


**Explanation:**


An Interface endpoint uses AWS PrivateLink and is an elastic network interface (ENI) with a private IP address that

serves as an entry point for traffic destined to a supported service. Using PrivateLink you can connect your VPC to

supported AWS services, services hosted by other AWS accounts (VPC endpoint services), and supported AWS Marketplace

partner services.


- CORRECT "Create a private API using an interface VPC endpoint" is the correct answer.


- INCORRECT "Create a NAT gateway" is incorrect. NAT Gateways are used to provide Internet access for EC2 instances in

  private subnets so are of no use in this solution.


- INCORRECT "Create a public VIF on a Direct Connect connection" is incorrect. You do not need to implement Direct

  Connect and create a public VIF. Public IP addresses are used in public VIFs and the question requests that only

  private addresses are used.


- INCORRECT "Add the API gateway to the subnet the EC2 instances are located in" is incorrect. You cannot add API

  Gateway to the subnet the EC2 instances are in, it is a public service with a public endpoint.


**References:**


https://aws.amazon.com/blogs/compute/introducing-amazon-api-gateway-private-endpoints/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-

delivery/amazon-vpc/

