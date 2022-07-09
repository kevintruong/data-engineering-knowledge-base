#### Question  41


**A manufacturing company captures data from machines running at customer sites. Currently, thousands of machines send

data every 5 minutes, and this is expected to grow to hundreds of thousands of machines in the near future. The data is

logged with the intent to be analyzed in the future as needed.**


**What is the SIMPLEST method to store this streaming data at scale?**


1: Create an Amazon EC2 instance farm behind an ELB to store the data in Amazon EBS Cold HDD volumes


2: Create an Amazon SQS queue, and have the machines write to the queue


3: Create an Amazon Kinesis Firehose delivery stream to store the data in Amazon S3


4: Create an Auto Scaling Group of Amazon EC2 instances behind ELBs to write data into Amazon RDS


Answer: 3


**Explanation:**


Kinesis Data Firehose is the easiest way to load streaming data into data stores and analytics tools. It captures,

transforms, and loads streaming data and you can deliver the data to “destinations” including Amazon S3 buckets for

later analysis


- CORRECT "Create an Amazon Kinesis Firehose delivery stream to store the data in Amazon S3" is the correct answer.


- INCORRECT "Create an Amazon EC2 instance farm behind an ELB to store the data in Amazon EBS Cold HDD volumes" is

  incorrect. Storing the data in EBS wold be expensive and as EBS volumes cannot be shared by multiple instances you

  would have a bottleneck of a single EC2 instance writing the data.


- INCORRECT "Create an Amazon SQS queue, and have the machines write to the queue" is incorrect. Using an SQS queue to

  store the data is not possible as the data needs to be stored long-term and SQS queues have a maximum retention time

  of 14 days.


- INCORRECT "Create an Auto Scaling Group of Amazon EC2 instances behind ELBs to write data into Amazon RDS" is

  incorrect. Writing data into RDS via a series of EC2 instances and a load balancer is more complex and more expensive.

  RDS is also not an ideal data store for this data.


**References:**


https://aws.amazon.com/kinesis/data-firehose/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/analytics/amazon-kinesis/

