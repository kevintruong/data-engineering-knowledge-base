*

**Explanation:**

When you create a new subnet, it is automatically associated with the main route table. Therefore, the EC2 instance will

not have a route to the Internet. The Architect should associate the new subnet with the custom route table.

* ✅ :  "The subnet has been automatically associated with the main route table which does not have a route to the

  Internet" is the correct answer.

* ❌ :  "The new subnet has not been associated with a route table" is incorrect. Subnets are always associated to a

  route table when created.

* ❌ :  "The Internet Gateway is experiencing connectivity problems" is incorrect. Internet Gateways are

  highly-available so it’s unlikely that IGW connectivity is the issue.

* ❌ :  "There is no NAT Gateway available in the new subnet so Internet connectivity is not possible" is incorrect.

  NAT Gateways are used for connecting EC2 instances in private subnets to the Internet. This is a valid reason for a

  private subnet to not have connectivity, however in this case the Architect is attempting to use an Internet Gateway.

**References:**

<https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content>-

delivery/amazon-vpc/

----
* #<https://docs.aws.amazon.com/vpc/latest/userguide/vpc_route_tables.html> #ec2_instance #ec2_instances #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content>>- #internet_gateways
