#### Question  33


**A Solutions Architect is migrating a small relational database into AWS. The database will run on an EC2 instance and

the DB size is around 500 GB. The database is infrequently used with small amounts of**


**requests spread across the day. The DB is a low priority and the Architect needs to lower the cost of the solution.**


**What is the MOST cost-effective storage type?**


1: Amazon EBS Provisioned IOPS SSD


2: Amazon EFS


3: Amazon EBS Throughput Optimized HDD


4: Amazon EBS General Purpose SSD


Answer: 3


**Explanation:**


Throughput Optimized HDD is the most cost-effective storage option and for a small DB with low traffic volumes it may be

sufficient. Note that the volume must be at least 500 GB in size.


A breakdown of EBS volume types is provided below:


- CORRECT "Amazon EBS Throughput Optimized HDD" is the correct answer.


- INCORRECT "Amazon EBS Provisioned IOPS SSD" is incorrect.. Provisioned IOPS SSD provides high performance but at a

  higher cost.


- INCORRECT Amazon EFS"" is incorrect. The Amazon Elastic File System (EFS) is not an ideal storage solution for a

  database.


- INCORRECT "Amazon EBS General Purpose SSD" is incorrect. AWS recommend using General Purpose SSD rather than

  Throughput Optimized HDD for most use cases but it is more expensive.


**References:**


https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ebs/

