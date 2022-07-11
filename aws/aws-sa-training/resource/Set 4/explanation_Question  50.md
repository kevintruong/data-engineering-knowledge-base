*

**Explanation:**

Multi-AZ RDS creates a replica in another AZ and synchronously replicates to it (DR only).

A failover may be triggered in the following circumstances:

* Loss of primary AZ or primary DB instance failure

* Loss of network connectivity on primary

* Compute (EC2) unit failure on primary

* Storage (EBS) unit failure on primary

* The primary DB instance is changed

* Patching of the OS on the primary DB instance

* Manual failover (reboot with failover selected on primary)

During failover RDS automatically updates configuration (including DNS endpoint) to use the second node.

* ✅ :  "The failover mechanism automatically changes the DNS record of the DB instance to point to the standby DB

  instance" is a correct answer.

* ✅ :  "The primary DB instance will switch over automatically to the standby replica" is also a correct answer.

* ❌ :  "A failover will take place once the connection draining timer has expired" is incorrect. Connection

  draining timers are applicable to ELBs not RDS.

* ❌ :  "A manual failover of the DB instance will need to be initiated using Reboot with failover" is incorrect.

  You do not need to manually failover the DB instance, multi-AZ has an automatic process as outlined above.

* ❌ :  "Due to the loss of network connectivity the process to switch to the standby replica cannot take place"

  is incorrect. The process to failover is not reliant on network connectivity as it is designed for fault tolerance.

**References:**

<https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-rds/>

----
* #failover_rds #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-rds/> #failover_mechanism #failover #primary_db_instance_failure
