#### Question  6


**A website runs on Amazon EC2 instances behind an Application Load Balancer (ALB). The website has a mix of dynamic and

static content. Customers around the world are reporting performance issues with the website.**


**Which set of actions will improve website performance for users worldwide?**


1: Create an Amazon CloudFront distribution and configure the ALB as an origin. Then update the Amazon Route 53 record

to point to the CloudFront distribution


2: Create a latency-based Amazon Route 53 record for the ALB. Then launch new EC2 instances with larger instance sizes

and register the instances with the ALB


3: Launch new EC2 instances hosting the same web application in different Regions closer to the users. Use an AWS

Transit Gateway to connect customers to the closest region


4: Migrate the website to an Amazon S3 bucket in the Regions closest to the users. Then create an Amazon Route 53

geolocation record to point to the S3 buckets


Answer: 1


**Explanation:**


Amazon CloudFront is a content delivery network (CDN) that improves website performance by caching content at edge

locations around the world. It can serve both dynamic and static content. This is the best solution for improving the

performance of the website.


- CORRECT "Create an Amazon CloudFront distribution and configure the ALB as an origin. Then update the Amazon Route 53

  record to point to the CloudFront distribution" is the correct answer.


- INCORRECT "Create a latency-based Amazon Route 53 record for the ALB. Then launch new EC2 instances with larger

  instance sizes and register the instances with the ALB" is incorrect. Latency routing routes based on the latency

  between the client and AWS. There is no mention in the answer about creating the new instances in another region

  therefore the only advantage is in using larger instance sizes. For a dynamic site this adds complexity in keeping the

  instances in sync.


- INCORRECT "Launch new EC2 instances hosting the same web application in different Regions closer to the users. Use an

  AWS Transit Gateway to connect customers to the closest region" is incorrect as Transit Gateway is a service for

  connecting on-premises networks and VPCs to a single gateway.


- INCORRECT "Migrate the website to an Amazon S3 bucket in the Regions closest to the users. Then create an Amazon Route

  53 geolocation record to point to the S3 buckets" is incorrect as with S3 you can only host static websites, not

  dynamic websites.


**References:**


https://aws.amazon.com/cloudfront/dynamic-content/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-

delivery/amazon-cloudfront/

