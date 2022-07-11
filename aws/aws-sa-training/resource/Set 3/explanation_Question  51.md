**Explanation:**

The most straightforward solution is to use CloudFront to cache the content in the Edge locations around the world that

are close to users. This is easy to implement and will solve the issues reported.

CloudFront has many edge locations around the world for caching the content as can be seen in the graphic below:

- ✅ :  "Cache the web content using Amazon CloudFront and use all Edge locations for content delivery" is the correct

  answer.

- ❌ :  "Use an Amazon Route 53 weighted routing policy for the CloudFront domain name to distribute GET requests

  between CloudFront and the S3 bucket" is incorrect. Route 53 weighted policies are used to direct traffic

  proportionally to different sites not based on latency or geography.

- ❌ :  "Replicate the bucket in us-east-1 and use Amazon Route 53 failover routing to determine which bucket to

  serve the content from" is incorrect. You could replicate the data in the buckets and use latency based routing to

  direct clients to the closest bucket but this option isn’t presented. Failover routing is used for high availability

  and would not assist here.

- ❌ :  "Place an Amazon ElastiCache cluster in front of the S3 bucket" is incorrect. ElastiCache is a database

  caching service, it does not cache content from S3 buckets.

**References:**

<https://aws.amazon.com/cloudfront/features/>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content>-

delivery/amazon-cloudfront/

----

- #amazon_cloudfront #cloudfront #amazon_elasticache_cluster #<https://aws.amazon.com/cloudfront/features/_>> #cloudfront_domain_name
