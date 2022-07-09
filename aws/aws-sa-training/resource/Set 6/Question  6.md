#### Question  6


**A legacy application is being migrated into AWS. The application has a large amount of data that is rarely accessed.

When files are accessed, they are retrieved sequentially. The application will be migrated onto an Amazon EC2

instance.**


**What is the LEAST expensive EBS volume type for this use case?**


1: Cold HDD (sc1)


2: Provisioned IOPS SSD (io1)


3: General Purpose SSD (gp2)


4: Throughput Optimized HDD (st1)


Answer: 1


**Explanation:**


The cold HDD (sc1) EBS volume type is the lowest cost option that is suitable for this use case. The sc1 volume type is

suitable for infrequently accessed data and use cases that are oriented towards throughput like sequential data access.


- CORRECT "Cold HDD (sc1)" is the correct answer.


- INCORRECT "Provisioned IOPS SSD (io1)" is incorrect. This is the most expensive option and used for use cases that

  demand high IOPS.


- INCORRECT "General Purpose SSD (gp2)" is incorrect. This is a more expensive SSD volume type that is used for general

  use cases.


- INCORRECT "Throughput Optimized HDD (st1)" is incorrect. This is also used for throughput-oriented use cases however

  it is higher cost than sc1 and better for frequently accessed data.


**References:**


https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ec2/

