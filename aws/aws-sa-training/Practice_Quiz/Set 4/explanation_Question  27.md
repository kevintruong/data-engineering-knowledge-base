*

**Explanation:**

A public subnet is a subnet that has an Internet Gateway attached and “Enable auto-assign public IPv4 address” enabled.

Instances require a public IP or Elastic IP address. It is also necessary to have the subnet route table updated to

point to the Internet Gateway and security groups and network ACLs must be configured to allow the SSH traffic on port

22.

* ✅ :  "A Public or Elastic IP address on the EC2 instance" is a correct answer.

* ✅ :  "An Internet Gateway attached to the VPC and route table attached to the public subnet pointing to it" is also

  a correct answer.

* ❌ :  "A bastion host" is incorrect. A bastion host can be used to access instances in private subnets but is not

  required for instances in public subnets.

* ❌ :  "A NAT Gateway" is incorrect. A NAT Gateway allows instances in private subnets to access the Internet, it

  is not used for remote access.

* ❌ :  "An IPSec VPN" is incorrect. An IPSec VPN is not required to connect to an instance in a public subnet.

**References:**

<https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstances.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content>-

delivery/amazon-vpc/

----
* #ec2_instance #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content>>- #private_subnets #public_subnets #bastion_host
