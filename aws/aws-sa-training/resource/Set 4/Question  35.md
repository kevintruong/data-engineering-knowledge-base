#### Question  35


**A Solutions Architect has setup a VPC with a public subnet and a VPN-only subnet. The public subnet is associated with

a custom route table that has a route to an Internet Gateway. The VPN-only subnet is associated with the main route

table and has a route to a virtual private gateway.**


**The Architect has created a new subnet in the VPC and launched an EC2 instance in it. However, the instance cannot

connect to the Internet. What is the MOST likely reason?**


1: The subnet has been automatically associated with the main route table which does not have a route to the Internet


2: The new subnet has not been associated with a route table


3: The Internet Gateway is experiencing connectivity problems


4: There is no NAT Gateway available in the new subnet so Internet connectivity is not possible


**Answer: 1**


**Explanation:**


When you create a new subnet, it is automatically associated with the main route table. Therefore, the EC2 instance will

not have a route to the Internet. The Architect should associate the new subnet with the custom route table.


- CORRECT "The subnet has been automatically associated with the main route table which does not have a route to the

  Internet" is the correct answer.


- INCORRECT "The new subnet has not been associated with a route table" is incorrect. Subnets are always associated to a

  route table when created.


- INCORRECT "The Internet Gateway is experiencing connectivity problems" is incorrect. Internet Gateways are

  highly-available so it’s unlikely that IGW connectivity is the issue.


- INCORRECT "There is no NAT Gateway available in the new subnet so Internet connectivity is not possible" is incorrect.

  NAT Gateways are used for connecting EC2 instances in private subnets to the Internet. This is a valid reason for a

  private subnet to not have connectivity, however in this case the Architect is attempting to use an Internet Gateway.


**References:**


https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-

delivery/amazon-vpc/

