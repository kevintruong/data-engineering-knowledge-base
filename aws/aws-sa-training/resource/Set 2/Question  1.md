#### Question  1


**A development team needs to host a website that will be accessed by other teams. The website contents consist of HTML,

CSS, client-side JavaScript, and images. A Solutions Architect has been asked to recommend a solution for hosting the

website.**


**Which solution is the MOST cost-effective?**


1: Containerize the website and host it in AWS Fargate


2: Create an Amazon S3 bucket and host the website there


3: Deploy a web server on an Amazon EC2 instance to host the website


4: Configure an Application Load Balancer with an AWS Lambda target


Answer: 2


**Explanation:**


You can use Amazon S3 to host a static website. On a _static_ website, individual webpages include static content. They

might also contain client-side scripts.


To host a static website on Amazon S3, you configure an Amazon S3 bucket for website hosting and then upload your

website content to the bucket. When you configure a bucket as a static website, you must enable website hosting, set

permissions, and create and add an index document. Depending on your website requirements, you can also configure

redirects, web traffic logging, and a custom error document.


This use case can be well served by using an S3 static website and this will be the most cost-effective option.


- CORRECT "Create an Amazon S3 bucket and host the website there" is the correct answer.


- INCORRECT "Containerize the website and host it in AWS Fargate" is incorrect as this is not the most cost- effective

  option.


- INCORRECT "Deploy a web server on an Amazon EC2 instance to host the website" is incorrect as this is not the most

  cost-effective option.


- INCORRECT "Configure an Application Load Balancer with an AWS Lambda target" is incorrect as this is not the most

  cost-effective option and is an incomplete solution.


**References:**


https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/

