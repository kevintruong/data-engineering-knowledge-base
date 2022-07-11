**Explanation:**

Both a NAT gateway or a NAT instance can be used for this use case. Both services enable internet access for instances

in private subnets. However, the NAT instance runs on an EC2 instance you must launch, configure and manage and

therefore involves more ongoing systems management effort.

- ✅ :  "Implement a NAT gateway" is the correct answer.

- ❌ :  "Launch a NAT instance" is incorrect as this service involves more ongoing systems management effort.

- ❌ :  "Create a Virtual Private Gateway" is incorrect. A VPG is used as part of a VPN connection (AWS side of the

  connection). It is not used to enable internet access.

- ❌ :  "Attach Elastic IP addresses" is incorrect. You cannot use Elastic IP addresses with instances in private

  subnets.

**References:**

<https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content>-

delivery/amazon-vpc/

----

- #ec2_instance #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content>>- #elastic_ip_addresses #nat_instance #aws_side
