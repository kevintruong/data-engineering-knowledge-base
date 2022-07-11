**Explanation:**

Kinesis Data Firehose is the easiest way to load streaming data into data stores and analytics tools. It captures,

transforms, and loads streaming data and you can deliver the data to “destinations” including Amazon S3 buckets for

later analysis

- ✅ :  "Create an Amazon Kinesis Firehose delivery stream to store the data in Amazon S3" is the correct answer.

- ❌ :  "Create an Amazon EC2 instance farm behind an ELB to store the data in Amazon EBS Cold HDD volumes" is

  incorrect. Storing the data in EBS wold be expensive and as EBS volumes cannot be shared by multiple instances you

  would have a bottleneck of a single EC2 instance writing the data.

- ❌ :  "Create an Amazon SQS queue, and have the machines write to the queue" is incorrect. Using an SQS queue to

  store the data is not possible as the data needs to be stored long-term and SQS queues have a maximum retention time

  of 14 days.

- ❌ :  "Create an Auto Scaling Group of Amazon EC2 instances behind ELBs to write data into Amazon RDS" is

  incorrect. Writing data into RDS via a series of EC2 instances and a load balancer is more complex and more expensive.

  RDS is also not an ideal data store for this data.

**References:**

<https://aws.amazon.com/kinesis/data-firehose/>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/analytics/amazon-kinesis/>

----

- #amazon_ec2_instance_farm #amazon_kinesis_firehose_delivery_stream #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/analytics/amazon-kinesis/> #amazon_ec2 #ec2_instances
