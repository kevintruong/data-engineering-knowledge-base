#### Question  9


**A Solutions Architect must enable an application to download software updates from the internet. The application runs

on a series of EC2 instances in an Auto Scaling group running in a private subnet. The solution must involve minimal

ongoing systems management effort. How should the Solutions Architect proceed?**


1: Implement a NAT gateway


2: Launch a NAT instance


3: Create a Virtual Private Gateway


4: Attach Elastic IP addresses


Answer: 1


**Explanation:**


Both a NAT gateway or a NAT instance can be used for this use case. Both services enable internet access for instances

in private subnets. However, the NAT instance runs on an EC2 instance you must launch, configure and manage and

therefore involves more ongoing systems management effort.


- CORRECT "Implement a NAT gateway" is the correct answer.


- INCORRECT "Launch a NAT instance" is incorrect as this service involves more ongoing systems management effort.


- INCORRECT "Create a Virtual Private Gateway" is incorrect. A VPG is used as part of a VPN connection (AWS side of the

  connection). It is not used to enable internet access.


- INCORRECT "Attach Elastic IP addresses" is incorrect. You cannot use Elastic IP addresses with instances in private

  subnets.


**References:**


https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-

delivery/amazon-vpc/

