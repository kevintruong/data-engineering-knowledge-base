*

**Explanation:**

When you create the RDS instance, you need to select the option to make it publicly accessible. A security group will

need to be created and assigned to the RDS instance to allow access from the public IP address of your application (or

firewall).

* ✅ :  "Choose to make the RDS instance publicly accessible and place it in a public subnet" is a correct answer.

* ✅ :  "Create a security group allowing access from the on-premise public IP to the RDS instance and assign to the

  RDS instance" is also a correct answer.

* ❌ :  "Configure a NAT Gateway and attach the RDS database" is incorrect. NAT Gateways are used for enabling

  Internet connectivity for EC2 instances in private subnets.

* ❌ :  "Select a public IP within the DB subnet group to assign to the RDS instance" is incorrect. The RDS instance

  does not require a public IP.

* ❌ :  "Create a DB subnet group that is publicly accessible" is incorrect. A DB subnet group is a collection of

  subnets (typically private) that you create in a VPC and that you then designate for your DB instance. The DB subnet

  group cannot be made publicly accessible, even if the subnets are public subnets, it is the RDS DB that must be

  configured to be publicly accessible.

**References:**

<https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.Scenarios.html#USER_VPC.Scenario4>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-rds/>

----
* #rds_instance #rds_database #rds_db #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-rds/> #nat_gateways
