**Explanation:**

This is a great use case for Amazon Simple Queue Service (Amazon SQS). SQS is a web service that gives you access to

message queues that store messages waiting to be processed and offers a reliable, highly-scalable, hosted queue for

storing messages in transit between computers. SQS is used for distributed/decoupled applications. In this circumstance

SQS will reduce the risk of writes being dropped and it the best option presented.

- ✅ :  "Update the application to write data to an SQS queue and provision additional EC2 instances to process the

  data and write it to the database" is the correct answer.

- ❌ :  "Use RDS in a multi-AZ configuration to distribute writes across AZs" is incorrect. RDS in a multi- AZ

  configuration will not help as writes are only made to the primary database.

- ❌ :  "Use CloudFront to cache the writes and configure the database as a custom origin" is incorrect. You cannot

  configure a database as a custom origin in CloudFront.

- ❌ :  "Update the application to write data to an S3 bucket and provision additional EC2 instances to process the

  data and write it to the database" is incorrect. Though writing data to an S3 bucket could potentially work, it is not

  the best option as SQS is recommended for decoupling application components.

**References:**

<https://aws.amazon.com/sqs/features/>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/application>-

integration/amazon-sqs/

----

- #amazon_simple_queue_service #amazon_sqs #cloudfront #sqs_queue #multi_-_az_configuration
