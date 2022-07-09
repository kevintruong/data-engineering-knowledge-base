#### Question  32


**You are looking for a method to distribute onboarding videos to your company’s numerous remote workers around the

world. The training videos are located in an S3 bucket that is not publicly accessible. Which of the options below would

allow you to share the videos?**


1: Use CloudFront and set the S3 bucket as an origin


2: Use a Route 53 Alias record the points to the S3 bucket


3: Use ElastiCache and attach the S3 bucket as a cache origin


4: Use CloudFront and use a custom origin pointing to an EC2 instance


Answer: 1


**Explanation:**


CloudFront uses origins which specify the origin of the files that the CDN will distribute. Origins can be either an S3

bucket, an EC2 instance, and Elastic Load Balancer, or Route 53 – can also be external (non-AWS). When using Amazon S3

as an origin you place all of your objects within the bucket.


- CORRECT "Use CloudFront and set the S3 bucket as an origin" is the correct answer.


- INCORRECT "Use a Route 53 Alias record the points to the S3 bucket" is incorrect. You cannot use a Route 53 Alias

  record to connect to an S3 bucket that is not publicly available.


- INCORRECT "Use ElastiCache and attach the S3 bucket as a cache origin" is incorrect. You cannot configure an origin

  with ElastiCache.


- INCORRECT "Use CloudFront and use a custom origin pointing to an EC2 instance" is incorrect. You can configure a

  custom origin pointing to an EC2 instance but as the training videos are located in an S3 bucket this would not be

  helpful.


**References:**


https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DownloadDistS3AndCustomOrigins. html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-

delivery/amazon-cloudfront/

