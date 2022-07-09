#### Question  25


**One of the applications you manage on RDS uses the MySQL DB and has been suffering from performance issues. You would

like to setup a reporting process that will perform queries on the database but you’re concerned that the extra load

will further impact the performance of the DB and may lead to poor customer experience.**


**What would be the best course of action to take so you can implement the reporting process?**


1: Configure Multi-AZ to setup a secondary database instance in another region


2: Deploy a Read Replica to setup a secondary read-only database instance


3: Deploy a Read Replica to setup a secondary read and write database instance


4: Configure Multi-AZ to setup a secondary database instance in another Availability Zone


**Answer: 2**


**Explanation:**


The reporting process will perform queries on the database but not writes. Therefore you can use a read replica which

will provide a secondary read-only database and configure the reporting process to use the read replica.


Multi-AZ is used for implementing fault tolerance. With Multi-AZ you can failover to a DB in another AZ within the

region in the event of a failure of the primary DB. However, you can only read and write to the primary DB so still need

a read replica to offload the reporting job


- CORRECT "Deploy a Read Replica to setup a secondary read-only database instance" is the correct answer.


- INCORRECT "Configure Multi-AZ to setup a secondary database instance in another region" is incorrect as described

  above.


- INCORRECT "Deploy a Read Replica to setup a secondary read and write database instance" is incorrect. Read replicas

  are for workload offloading only and do not provide the ability to write to the database.


- INCORRECT "Configure Multi-AZ to setup a secondary database instance in another Availability Zone" is incorrect as

  described above.


**References:**


https://aws.amazon.com/rds/features/read-replicas/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-rds/

