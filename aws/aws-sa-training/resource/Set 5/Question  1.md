#### Question  1


1: Setup an AWS Direct Connect connection


2: Configure a Virtual Private Gateway


3: Create an Amazon CloudFront distribution


4: Create an AWS Transit Gateway


Answer: 2


**Explanation:**


A virtual private gateway is a logical, fully redundant distributed edge routing function that sits at the edge of your

VPC. You must create a VPG in your VPC before you can establish an AWS Managed site-to-site VPN connection. The other

end of the connection is the customer gateway which must be established on the customer side of the connection.


- CORRECT "Configure a Virtual Private Gateway" is the correct answer.


- INCORRECT "Setup an AWS Direct Connect connection" is incorrect as this would take too long to provision.


- INCORRECT "Create an Amazon CloudFront distribution" is incorrect. This is not a solution for enabling connectivity

  using private addresses to an on-premises site. CloudFront is a content delivery network (CDN).


- INCORRECT "Create an AWS Transit Gateway" is incorrect. AWS Transit Gateway connects VPCs and on- premises networks

  through a central hub which is not a requirement of this solution.


**References:**


https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-

delivery/amazon-vpc/

