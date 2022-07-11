*

**Explanation:**

A public subnet is a subnet that's associated with a route table that has a route to an Internet gateway.

Public subnets are subnets that have:

* “Auto-assign public IPv4 address” set to “Yes”.

* The subnet route table has an attached Internet Gateway.

* ✅ :  "Check that the instance has a public IP address" is the correct answer.

* ✅ :  "Check that the route table associated with the subnet has an entry for an Internet Gateway" is the correct

  answer.

* ❌ :  "Check that there is a NAT Gateway configured for the subnet" is incorrect. A NAT Gateway is used for

  providing outbound Internet access for EC2 instances in private subnets.

* ❌ :  "Check that Security Group has a rule for outbound traffic" is incorrect. Security groups are stateful and

  do not need a rule for outbound traffic. For this solution you would only need to create an inbound rule that allows

  the relevant protocol.

* ❌ :  "Check that you can ping the instance from another subnet" is incorrect. Checking you can ping from another

  subnet does not relate to being able to access the instance remotely as it uses different protocols and a different

  network path.

**References:**

<https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Scenario2.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content>-

delivery/amazon-vpc/

----
* #public_subnet #nat_gateway #public_subnets #private_subnets #ec2_instances
