#### Question  9


**An application uses a MySQL database running on an Amazon EC2 instance. The application generates high I/O and

constant writes to a single table on the database. Which Amazon EBS volume type will provide the MOST consistent

performance and low latency?**


1: General Purpose SSD (gp2)


2: Provisioned IOPS SSD (io1)


3: Throughput Optimized HDD (st1)


4: Cold HDD (sc1)


Answer: 2


**Explanation:**


The Provisioned IOPS SSD (io1) volume type will offer the most consistent performance and can be configured with the

amount of IOPS required by the application. It will also provide the lowest latency of the options presented.


- CORRECT "Provisioned IOPS SSD (io1)" is the correct answer.


- INCORRECT "General Purpose SSD (gp2)" is incorrect. This is not the best solution for when you require high I/O,

  consistent performance and low latency.


- INCORRECT "Throughput Optimized HDD (st1)" is incorrect. This is a HDD type of disk and not suitable for low latency

  workloads that require consistent performance.


- INCORRECT "Cold HDD (sc1)" is incorrect. This is the lowest cost option and not suitable for frequently accessed

  workloads.


**References:**


https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ebs/

