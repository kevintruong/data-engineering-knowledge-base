*

**Explanation:**

NAT gateways are managed for you by AWS. NAT gateways are highly available in each AZ into which they are deployed. They

are not associated with any security groups and can scale automatically up to 45Gbps

NAT instances are managed by you. They must be scaled manually and do not provide HA. NAT Instances can be used as

bastion hosts and can be assigned to security groups.

* ✅ :  "Managed for you by AWS" is a correct answer.

* ✅ :  "Highly available within each AZ" is also a correct answer.

* ❌ :  "Can be assigned to security groups" is incorrect as you cannot assign security groups to NAT gateways but

  you can to NAT instances.

* ❌ :  "Can be used as a bastion host" is incorrect, only a NAT instance can be used as a bastion host.

* ❌ :  "Can be scaled up manually" is incorrect, though automatic is better anyway!

**References:**

<https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-comparison.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content>-

delivery/amazon-vpc/

----
* #<https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-comparison.html> #nat_instances #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content>>- #nat_gateways #aws
