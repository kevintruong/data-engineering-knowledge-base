#### Question  51


**A company is serving videos to their customers from us-east-1 from an Amazon S3 bucket. The company’s customers are

located around the world and there is high demand during peak hours. Customers in Asia complain about slow download

speeds during peak hours and customers in all locations have reported experiencing HTTP 500 errors.**


**How can a Solutions Architect address the issues?**


1: Use an Amazon Route 53 weighted routing policy for the CloudFront domain name to distribute GET requests between

CloudFront and the S3 bucket


2: Replicate the bucket in us-east-1 and use Amazon Route 53 failover routing to determine which bucket to serve the

content from


3: Cache the web content using Amazon CloudFront and use all Edge locations for content delivery


4: Place an Amazon ElastiCache cluster in front of the S3 bucket


Answer: 3


**Explanation:**


The most straightforward solution is to use CloudFront to cache the content in the Edge locations around the world that

are close to users. This is easy to implement and will solve the issues reported.


CloudFront has many edge locations around the world for caching the content as can be seen in the graphic below:


- CORRECT "Cache the web content using Amazon CloudFront and use all Edge locations for content delivery" is the correct

  answer.


- INCORRECT "Use an Amazon Route 53 weighted routing policy for the CloudFront domain name to distribute GET requests

  between CloudFront and the S3 bucket" is incorrect. Route 53 weighted policies are used to direct traffic

  proportionally to different sites not based on latency or geography.


- INCORRECT "Replicate the bucket in us-east-1 and use Amazon Route 53 failover routing to determine which bucket to

  serve the content from" is incorrect. You could replicate the data in the buckets and use latency based routing to

  direct clients to the closest bucket but this option isn’t presented. Failover routing is used for high availability

  and would not assist here.


- INCORRECT "Place an Amazon ElastiCache cluster in front of the S3 bucket" is incorrect. ElastiCache is a database

  caching service, it does not cache content from S3 buckets.


**References:**


https://aws.amazon.com/cloudfront/features/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-

delivery/amazon-cloudfront/

