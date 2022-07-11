**Explanation:**

The only solution presented that actually works is to create a NAT gateway in the public subnet of each AZ. They must be

created in the public subnet as they gain public IP addresses and use an internet gateway for internet access.

The route tables in the private subnets must then be configured with a route to the NAT gateway and then the EC2

instances will be able to access the internet (subject to security group configuration).

- ✅ :  "Create a NAT gateway in the public subnet of each AZ. Update the route tables for each private subnet to

  direct internet-bound traffic to the NAT gateway" is the correct answer.

- ❌ :  "Create a NAT gateway and attach it to the VPC. Add a route to the gateway to each private subnet route

  table" is incorrect. You do not attach NAT gateways to VPCs, you add them to public subnets.

- ❌ :  "Configure an internet gateway. Add a route to the gateway to each private subnet route table" is incorrect.

  You cannot add a route to an internet gateway to a private subnet route table (private EC2 instances don’t even have

  public IP addresses).

- ❌ :  "Create a NAT instance in the private subnet of each AZ. Update the route tables for each private subnet to

  direct internet-bound traffic to the NAT instance" is incorrect. You do not create NAT instances in private subnets,

  they must be created in public subnets.

**References:**

<https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content>-

delivery/amazon-vpc/

----

- #private_ec2_instances #nat_gateways #private_subnet_route #private_subnet_route_table #nat_instances
