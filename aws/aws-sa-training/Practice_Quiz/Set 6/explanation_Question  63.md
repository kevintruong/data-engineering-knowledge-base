*

**Explanation:**

Custom security groups do not have inbound allow rules (all inbound traffic is denied by default) whereas default

security groups do have inbound allow rules (allowing traffic from within the group). All outbound traffic is allowed by

default in both custom and default security groups.

Security groups act like a stateful firewall at the instance level. Specifically, security groups operate at the network

interface level of an EC2 instance. You can only assign permit rules in a security group, you cannot assign deny rules

and there is an implicit deny rule at the end of the security group. All rules are evaluated until a permit is

encountered or continues until the implicit deny. You can create ingress and egress rules.

* ✅ :  "There is an outbound rule that allows all traffic to all IP addresses" is the correct answer.

* ✅ :  "There are no inbound rules and traffic will be implicitly denied" is the correct answer.

* ❌ :  "There is an inbound rule allowing traffic from the Internet to port 22 for management" is incorrect. This

  is not true.

* ❌ :  "There are is an inbound rule that allows traffic from the Internet Gateway" is incorrect. There are no

  inbound allow rules by default.

* ❌ :  "There is an outbound rule allowing traffic to the Internet Gateway" is incorrect. There is an outbound

  allow rule but it allows traffic to anywhere, it does not specify the internet gateway.

**References:**

<https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content>-

delivery/amazon-vpc/

----
* #inbound_rules #ec2_instance #outbound_rule #inbound_rule #inbound_traffic
