*

**Explanation:**

If you are installing MySQL on an EC2 instance you cannot enable read replicas or multi-AZ. Instead you would need to

use Amazon RDS with a MySQL DB engine to use these features.

In this example a good solution is to use the native HA features of MySQL. You would want to place the second MySQL DB

instance in another AZ to enable high availability and fault tolerance.

Migrating to Amazon RDS may be a good solution but is not presented as an option.

* ✅ :  "Install MySQL on an EC2 instance in another availability zone and enable replication" is the correct answer.

* ❌ :  "Create a Read Replica in another availability zone" is incorrect as described above.

* ❌ :  "Enable Multi-AZ for the MySQL instance" is incorrect as described above.

* ❌ :  "Install MySQL on an EC2 instance in the same availability zone and enable replication" is incorrect as

  described above.

**References:**

<https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-increase-availability.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ec2/>

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-rds/>

----
* #mysql_instance #ec2_instance #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-rds/> #second_mysql_db #same_availability_zone
