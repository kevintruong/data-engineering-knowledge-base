#### Question  62


**An Amazon EC2 instance running a video on demand web application has been experiencing high CPU utilization. A

Solutions Architect needs to take steps to reduce the impact on the EC2 instance and improve performance for consumers.

Which of the steps below would help?**


1: Use ElastiCache as the web front-end and forward connections to EC2 for cache misses


2: Create a CloudFront distribution and configure a custom origin pointing at the EC2 instance


3: Create an ELB and place it in front of the EC2 instance


4: Create a CloudFront RTMP distribution and point it at the EC2 instance


**Answer: 2**


**Explanation:**


This is a good use case for CloudFront which is a content delivery network (CDN) that caches content to improve

performance for users who are consuming the content. This will take the load off of the EC2 instances as CloudFront has

a cached copy of the video files.


An origin is the origin of the files that the CDN will distribute. Origins can be either an S3 bucket, an EC2 instance,

and Elastic Load Balancer, or Route 53 – can also be external (non-AWS).


- CORRECT "Create a CloudFront distribution and configure a custom origin pointing at the EC2 instance" is the correct

  answer.


- INCORRECT "Use ElastiCache as the web front-end and forward connections to EC2 for cache misses" is incorrect.

  ElastiCache cannot be used as an Internet facing web front-end.


- INCORRECT "Create an ELB and place it in front of the EC2 instance" is incorrect. Placing an ELB in front of a single

  EC2 instance does not help to reduce load.


- INCORRECT "Create a CloudFront RTMP distribution and point it at the EC2 instance" is incorrect. For RTMP CloudFront

  distributions files must be stored in an S3 bucket.


**References:**


https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_Origin.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-

delivery/amazon-cloudfront/

