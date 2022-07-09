#### Question  34


**A membership website has become quite popular and is gaining members quickly. The website currently runs on Amazon EC2

instances with one web server instance and one database instance running MySQL. A Solutions Architect is concerned about

the lack of high-availability in the current architecture.**


**What can the Solutions Architect do to easily enable high availability without making major changes to the

architecture?**


1: Create a Read Replica in another availability zone


2: Enable Multi-AZ for the MySQL instance


3: Install MySQL on an EC2 instance in the same availability zone and enable replication


4: Install MySQL on an EC2 instance in another availability zone and enable replication


**Answer: 4**


**Explanation:**


If you are installing MySQL on an EC2 instance you cannot enable read replicas or multi-AZ. Instead you would need to

use Amazon RDS with a MySQL DB engine to use these features.


In this example a good solution is to use the native HA features of MySQL. You would want to place the second MySQL DB

instance in another AZ to enable high availability and fault tolerance.


Migrating to Amazon RDS may be a good solution but is not presented as an option.


- CORRECT "Install MySQL on an EC2 instance in another availability zone and enable replication" is the correct answer.


- INCORRECT "Create a Read Replica in another availability zone" is incorrect as described above.


- INCORRECT "Enable Multi-AZ for the MySQL instance" is incorrect as described above.


- INCORRECT "Install MySQL on an EC2 instance in the same availability zone and enable replication" is incorrect as

  described above.


**References:**


https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-increase-availability.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ec2/


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-rds/

