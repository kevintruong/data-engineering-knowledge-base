##### Question 1 answer: A


Explanation:


```

This is a great use case for Amazon Simple Queue Service (Amazon SQS). SQS is a web service

that gives you access to message queues that store messages waiting to be processed and offers

a reliable, highly-scalable, hosted queue for storing messages in transit between computers. SQS

is used for distributed/decoupled applications. In this circumstance SQS will reduce the risk of

writes being dropped and it the best option presented.

RDS in a multi-AZ configuration will not help as writes are only made to the primary database.

Though writing data to an S3 bucket could potentially work, it is not the best option as SQS is

recommended for decoupling application components.

The CloudFront option is bogus as you cannot configure a database as a custom origin in

CloudFront.

```

