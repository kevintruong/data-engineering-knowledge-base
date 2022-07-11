**Explanation:**

To enable outbound connectivity for instances in private subnets a NAT gateway can be created. The NAT gateway is

created in a public subnet and a route must be created in the private subnet pointing to the NAT gateway for

internet-bound traffic. An internet gateway must be attached to the VPC to facilitate outbound connections.

You cannot directly connect to an instance in a private subnet from the internet. You would need to use a bastion/jump

host. Therefore, the application will not be exposed to inbound connection attempts.

- ✅ :  "Create a NAT gateway and attach an internet gateway to the VPC" is the correct answer.

- ❌ :  "Create a NAT gateway but do not create attach an internet gateway to the VPC" is incorrect. An internet

  gateway must be attached to the VPC for any outbound connections to work.

- ❌ :  "Attach an internet gateway to the private subnet and create a NAT gateway" is incorrect. You do not attach

  internet gateways to subnets, you attach them to VPCs.

- ❌ :  "Attach an internet gateway to the VPC but do not create a NAT gateway" is incorrect. Without a NAT gateway

  the instances in the private subnet will not be able to download updates from the internet.

**References:**

<https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content>-

delivery/amazon-vpc/

----

- #vpc #nat_gateway #vpc/ #vpcs #private_subnets
