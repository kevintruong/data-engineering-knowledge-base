*

**Explanation:**

This is a good use case for CloudFront which is a content delivery network (CDN) that caches content to improve

performance for users who are consuming the content. This will take the load off of the EC2 instances as CloudFront has

a cached copy of the video files.

An origin is the origin of the files that the CDN will distribute. Origins can be either an S3 bucket, an EC2 instance,

and Elastic Load Balancer, or Route 53 – can also be external (non-AWS).

* ✅ :  "Create a CloudFront distribution and configure a custom origin pointing at the EC2 instance" is the correct

  answer.

* ❌ :  "Use ElastiCache as the web front-end and forward connections to EC2 for cache misses" is incorrect.

  ElastiCache cannot be used as an Internet facing web front-end.

* ❌ :  "Create an ELB and place it in front of the EC2 instance" is incorrect. Placing an ELB in front of a single

  EC2 instance does not help to reduce load.

* ❌ :  "Create a CloudFront RTMP distribution and point it at the EC2 instance" is incorrect. For RTMP CloudFront

  distributions files must be stored in an S3 bucket.

**References:**

<https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_Origin.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content>-

delivery/amazon-cloudfront/

----
* #cloudfront #cloudfront_distribution #<https://docs.aws.amazon.com/cloudfront/latest/apireference/api_origin.html> #non_-_aws #cloudfront_rtmp_distribution
