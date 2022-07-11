**Explanation:**

A _security group_ acts as a virtual firewall for your instance to control inbound and outbound traffic. When you launch

an instance in a VPC, you can assign up to five security groups to the instance. Security groups act at the instance

level, not the subnet level. Therefore, each instance in a subnet in your VPC can be assigned to a different set of

security groups.

- ✅ :  "Security group" is the correct answer.

- ❌ :  "AWS WAF" is incorrect. AWS WAF is a web application firewall and does not work at the instance level.

- ❌ :  "Route table" is incorrect. Route tables are not firewalls.

- ❌ :  "Network ACL" is incorrect. Network ACL’s function at the subnet level.

**References:**

<https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content>-

delivery/amazon-vpc/

----

- #aws_waf #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content>>- #**security_group** #security_group #security_groups
