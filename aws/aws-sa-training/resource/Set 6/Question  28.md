#### Question  28


**A distribution method is required for some static files. The requests will mainly be GET requests and a high volume of

GETs is expected, often exceeding 2000 per second. The files are currently stored in an S3 bucket. According to AWS best

practices, how can performance be optimized?**


1: Use cross-region replication to spread the load across regions


2: Use ElastiCache to cache the content


3: Integrate CloudFront with S3 to cache the content


4: Use S3 Transfer Acceleration


**Answer: 3**


**Explanation:**


Amazon S3 automatically scales to high request rates. For example, your application can achieve at least 3,500

PUT/POST/DELETE and 5,500 GET requests per second per prefix in a bucket. There are no limits to the number of prefixes

in a bucket.


If your workload is mainly sending GET requests, in addition to the preceding guidelines, you should consider using

Amazon CloudFront for performance optimization. By integrating CloudFront with Amazon S3, you can distribute content to

your users with low latency and a high data transfer rate.


- CORRECT "Integrate CloudFront with S3 to cache the content" is the correct answer.


- INCORRECT "Use cross-region replication to spread the load across regions" is incorrect. Cross-region replication

  creates a replica copy in another region but should not be used for spreading read requests across regions. There will

  be 2 S3 endpoints and CRR is not designed for 2 way sync so this would not work well.


- INCORRECT "Use ElastiCache to cache the content" is incorrect. ElastiCache is used for caching database content not S3

  content.


- INCORRECT "Use S3 Transfer Acceleration" is incorrect. Transfer Acceleration is used to accelerate object **

  uploads** to S3 over long distances (latency).


**References:**


https://docs.aws.amazon.com/AmazonS3/latest/dev/request-rate-perf-considerations.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/

