**Explanation:**

The requirements are to avoid the internet and use private IP addresses only. The best solution is to use a private

virtual interface across the Direct Connect connection to connect to the VPC using private IP addresses. A VPC endpoint

for Amazon API Gateway can be created and this will provide access to API Gateway using private IP addresses and avoids

the internet completely.

- ✅ :  "Use a private virtual interface and create a VPC Endpoint for Amazon API Gateway" is the correct answer.

- ❌ :  "Use a hosted virtual interface and create a VPC Endpoint for Amazon API Gateway" is incorrect. A hosted

  virtual interface is used to allow another account to access your Direct Connect link.

- ❌ :  "Use a transit virtual interface and an AWS VPN to create a secure tunnel to Amazon API Gateway" is

  incorrect. A transit virtual interface is used to access Amazon VPC Transit Gateways which are not included in the

  solution.

- ❌ :  "Use a public virtual interface and an AWS VPN to create a secure tunnel to Amazon API Gateway" is

  incorrect. This will use the public internet so it is not allowed in this scenario.

**References:**

<https://docs.aws.amazon.com/directconnect/latest/UserGuide/WorkingWithVirtualInterfaces.html>

<https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content>-

delivery/amazon-vpc/

----

- #amazon_vpc_transit_gateways #amazon_api_gateway #<https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints.html> #aws_vpn #api_gateway
