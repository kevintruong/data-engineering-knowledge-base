#### Question  47


**A Solutions Architect needs to design a solution that will allow Website Developers to deploy static web content

without managing server infrastructure. All web content must be accessed over HTTPS with a custom domain name. The

solution should be scalable as the company continues to grow.**


**Which of the following will provide the MOST cost-effective solution?**


1: Amazon S3 with a static website


2: Amazon CloudFront with an Amazon S3 bucket origin


3: AWS Lambda function with Amazon API Gateway


4: Amazon EC2 instance with Amazon EBS


Answer: 2


**Explanation:**


You can create an Amazon CloudFront distribution that uses an S3 bucket as the origin. This will allow you to serve the

static content using the HTTPS protocol.


To serve a static website hosted on Amazon S3, you can deploy a CloudFront distribution using one of these

configurations:


- Using a REST API endpoint as the origin with access restricted by an origin access identity (OAI).

- Using a website endpoint as the origin with anonymous (public) access allowed.

- Using a website endpoint as the origin with access restricted by a Referer header.


- CORRECT "Amazon CloudFront with an Amazon S3 bucket origin" is the correct answer.


- INCORRECT "Amazon S3 with a static website" is incorrect. You can create a static website using Amazon S3 with a

  custom domain name. However, you cannot connect to an Amazon S3 static website using HTTPS (only HTTP) so this

  solution does not work.


- INCORRECT "AWS Lambda function with Amazon API Gateway" is incorrect. AWS Lambda and API Gateway are both serverless

  services however this combination does not provide a solution for serving static content over HTTPS.


- INCORRECT "Amazon EC2 instance with Amazon EBS" is incorrect. Amazon EC2 with EBS is not a suitable solution as you

  would need to manage the server infrastructure (which the question states is not desired).


**References:**


https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-

delivery/amazon-cloudfront/

