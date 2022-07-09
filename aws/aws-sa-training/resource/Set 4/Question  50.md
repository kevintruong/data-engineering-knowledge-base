#### Question  50


**An Amazon RDS Multi-AZ deployment is running in an Amazon VPC. An outage occurs in the availability zone of the

primary RDS database instance. What actions will take place in this circumstance? (Select TWO)**


1: The failover mechanism automatically changes the DNS record of the DB instance to point to the standby DB instance


2: A failover will take place once the connection draining timer has expired


3: A manual failover of the DB instance will need to be initiated using Reboot with failover


4: The primary DB instance will switch over automatically to the standby replica


5: Due to the loss of network connectivity the process to switch to the standby replica cannot take place


**Answer: 1,4**


**Explanation:**


Multi-AZ RDS creates a replica in another AZ and synchronously replicates to it (DR only).


A failover may be triggered in the following circumstances:


- Loss of primary AZ or primary DB instance failure

- Loss of network connectivity on primary

- Compute (EC2) unit failure on primary

- Storage (EBS) unit failure on primary

- The primary DB instance is changed

- Patching of the OS on the primary DB instance

- Manual failover (reboot with failover selected on primary)


During failover RDS automatically updates configuration (including DNS endpoint) to use the second node.


- CORRECT "The failover mechanism automatically changes the DNS record of the DB instance to point to the standby DB

  instance" is a correct answer.


- CORRECT "The primary DB instance will switch over automatically to the standby replica" is also a correct answer.


- INCORRECT "A failover will take place once the connection draining timer has expired" is incorrect. Connection

  draining timers are applicable to ELBs not RDS.


- INCORRECT "A manual failover of the DB instance will need to be initiated using Reboot with failover" is incorrect.

  You do not need to manually failover the DB instance, multi-AZ has an automatic process as outlined above.


- INCORRECT "Due to the loss of network connectivity the process to switch to the standby replica cannot take place"

  is incorrect. The process to failover is not reliant on network connectivity as it is designed for fault tolerance.


**References:**


https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-rds/

