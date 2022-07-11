**Explanation:**

Typically, the nodes of an Internet-facing load balancer have public IP addresses and must therefore be in a public

subnet. To keep your back-end instances secure you can place them in a private subnet. To do this you must associate a

corresponding public and private subnet for each availability zone the ELB/instances are in).

For RDS, you create a DB subnet group which is a collection of subnets (typically private) that you create in a VPC and

that you then designate for your DB instances.

- ✅ :  "Create a private subnet for the Amazon EC2 instances and a private subnet for the Amazon RDS cluster" is the

  correct answer.

- ❌ :  "Create a public subnet for the Amazon EC2 instances and a public subnet for the Amazon RDS cluster" is

  incorrect as both tiers should be in private subnets.

- ❌ :  "Create a public subnet for the Amazon EC2 instances and a private subnet for the Amazon RDS cluster" is

  incorrect as both tiers should be in private subnets.

- ❌ :  "Create a private subnet for the Amazon EC2 instances and a public subnet for the Amazon RDS cluster" is

  incorrect as both tiers should be in private subnets.

**References:**

<https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/how-elastic-load-balancing-works.html>

<https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.htm>

l#USER_VPC.Subnets

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-rds/>

----

- #amazon_rds_cluster #amazon_ec2_instances #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-rds/> #<https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/how-elastic-load-balancing-works.html> #private_subnets
