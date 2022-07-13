*

**Explanation:**

The reporting process will perform queries on the database but not writes. Therefore you can use a read replica which

will provide a secondary read-only database and configure the reporting process to use the read replica.

Multi-AZ is used for implementing fault tolerance. With Multi-AZ you can failover to a DB in another AZ within the

region in the event of a failure of the primary DB. However, you can only read and write to the primary DB so still need

a read replica to offload the reporting job

* ✅ :  "Deploy a Read Replica to setup a secondary read-only database instance" is the correct answer.

* ❌ :  "Configure Multi-AZ to setup a secondary database instance in another region" is incorrect as described

  above.

* ❌ :  "Deploy a Read Replica to setup a secondary read and write database instance" is incorrect. Read replicas

  are for workload offloading only and do not provide the ability to write to the database.

* ❌ :  "Configure Multi-AZ to setup a secondary database instance in another Availability Zone" is incorrect as

  described above.

**References:**

<https://aws.amazon.com/rds/features/read-replicas/>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-rds/>

----
* #configure_multi_-_az #secondary_database_instance #multi_-_az #availability_zone #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-rds/>
