#### Question  20


**A new application you are designing will store data in an Amazon Aurora MySQL DB. You are looking for a way to enable

inter-region disaster recovery capabilities with fast replication and fast failover. Which of the following options is

the BEST solution?**


1: Use Amazon Aurora Global Database


2: Enable Multi-AZ for the Aurora DB


3: Create an EBS backup of the Aurora volumes and use cross-region replication to copy the snapshot


4: Create a cross-region Aurora Read Replica


**Answer: 1**


**Explanation:**


Amazon Aurora Global Database is designed for globally distributed applications, allowing a single Amazon Aurora

database to span multiple AWS regions. It replicates your data with no impact on database performance, enables fast

local reads with low latency in each region, and provides disaster recovery from region-wide outages.


Aurora Global Database uses storage-based replication with typical latency of less than 1 second, using dedicated

infrastructure that leaves your database fully available to serve application workloads. In the unlikely event of a

regional degradation or outage, one of the secondary regions can be promoted to full read/write capabilities in less

than 1 minute.


- CORRECT "Use Amazon Aurora Global Database" is the correct answer.


- INCORRECT "Enable Multi-AZ for the Aurora DB" is incorrect. Enabling Multi-AZ for the Aurora DB would provide AZ-level

  resiliency within the region not across regions.


- INCORRECT "Create an EBS backup of the Aurora volumes and use cross-region replication to copy the snapshot" is

  incorrect. Though you can take a DB snapshot and replicate it across regions, it does not provide an automated

  solution and it would not enable fast failover


- INCORRECT "Create a cross-region Aurora Read Replica" is incorrect. This solution would not provide the fast storage

  replication and fast failover capabilities of the Aurora Global Database and is therefore not the best option.


**References:**


https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Aurora.Replication.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-rds/

