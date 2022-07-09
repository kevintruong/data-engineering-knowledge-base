#### Question  6


**A company runs an application on-premises that must consume a REST API running on Amazon API Gateway. The company has

an AWS Direct Connect connection to their Amazon VPC. The solutions architect wants all API calls to use private

addressing only and avoid the internet. How can this be achieved?**


1: Use a transit virtual interface and an AWS VPN to create a secure tunnel to Amazon API Gateway


2: Use a private virtual interface and create a VPC Endpoint for Amazon API Gateway


3: Use a hosted virtual interface and create a VPC Endpoint for Amazon API Gateway


4: Use a public virtual interface and an AWS VPN to create a secure tunnel to Amazon API Gateway


Answer: 2


**Explanation:**


The requirements are to avoid the internet and use private IP addresses only. The best solution is to use a private

virtual interface across the Direct Connect connection to connect to the VPC using private IP addresses. A VPC endpoint

for Amazon API Gateway can be created and this will provide access to API Gateway using private IP addresses and avoids

the internet completely.


- CORRECT "Use a private virtual interface and create a VPC Endpoint for Amazon API Gateway" is the correct answer.


- INCORRECT "Use a hosted virtual interface and create a VPC Endpoint for Amazon API Gateway" is incorrect. A hosted

  virtual interface is used to allow another account to access your Direct Connect link.


- INCORRECT "Use a transit virtual interface and an AWS VPN to create a secure tunnel to Amazon API Gateway" is

  incorrect. A transit virtual interface is used to access Amazon VPC Transit Gateways which are not included in the

  solution.


- INCORRECT "Use a public virtual interface and an AWS VPN to create a secure tunnel to Amazon API Gateway" is

  incorrect. This will use the public internet so it is not allowed in this scenario.


**References:**


https://docs.aws.amazon.com/directconnect/latest/UserGuide/WorkingWithVirtualInterfaces.html


https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-

delivery/amazon-vpc/

