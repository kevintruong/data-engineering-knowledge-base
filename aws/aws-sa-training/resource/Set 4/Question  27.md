#### Question  27


**A Solutions Architect needs to connect from an office location to a Linux instance that is running in a public subnet

in an Amazon VPC using the Internet. Which of the following items are required to enable this access? (Select TWO)**


1: A bastion host


2: A NAT Gateway


3: A Public or Elastic IP address on the EC2 instance


4: An Internet Gateway attached to the VPC and route table attached to the public subnet pointing to it


5: An IPSec VPN


**Answer: 3,4**


**Explanation:**


A public subnet is a subnet that has an Internet Gateway attached and “Enable auto-assign public IPv4 address” enabled.

Instances require a public IP or Elastic IP address. It is also necessary to have the subnet route table updated to

point to the Internet Gateway and security groups and network ACLs must be configured to allow the SSH traffic on port


22.


- CORRECT "A Public or Elastic IP address on the EC2 instance" is a correct answer.


- CORRECT "An Internet Gateway attached to the VPC and route table attached to the public subnet pointing to it" is also

  a correct answer.


- INCORRECT "A bastion host" is incorrect. A bastion host can be used to access instances in private subnets but is not

  required for instances in public subnets.


- INCORRECT "A NAT Gateway" is incorrect. A NAT Gateway allows instances in private subnets to access the Internet, it

  is not used for remote access.


- INCORRECT "An IPSec VPN" is incorrect. An IPSec VPN is not required to connect to an instance in a public subnet.


**References:**


https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstances.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-

delivery/amazon-vpc/

