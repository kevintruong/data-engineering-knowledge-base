#### Question  60


**A Solutions Architect is designing a static website that will use the zone apex of a DNS domain (e.g. example.com).

The Architect wants to use the Amazon Route 53 service. Which steps should the Architect take to implement a scalable

and cost-effective solution? (Select TWO)**


1: Create a Route 53 hosted zone, and set the NS records of the domain to use Route 53 name servers


2: Serve the website from an Amazon S3 bucket, and map a Route 53 Alias record to the website endpoint


3: Host the website on an Amazon EC2 instance, and map a Route 53 Alias record to the public IP address of the EC2

instance


4: Host the website using AWS Elastic Beanstalk, and map a Route 53 Alias record to the Beanstalk stack


5: Host the website on an Amazon EC2 instance with ELB and Auto Scaling, and map a Route 53 Alias record to the ELB

endpoint


Answer: 1,2


**Explanation:**


To use Route 53 for an existing domain the Architect needs to change the NS records to point to the Amazon Route 53 name

servers. This will direct name resolution to Route 53 for the domain name. The most cost- effective solution for hosting

the website will be to use an Amazon S3 bucket. To do this you create a bucket using the same name as the domain name (

e.g. example.com) and use a Route 53 Alias record to map to it.


- CORRECT "Create a Route 53 hosted zone, and set the NS records of the domain to use Route 53 name servers" is the

  correct answer.


- CORRECT "Serve the website from an Amazon S3 bucket, and map a Route 53 Alias record to the website endpoint" is the

  correct answer.


- INCORRECT "Host the website on an Amazon EC2 instance, and map a Route 53 Alias record to the public IP address of the

  EC2 instance" is incorrect.Using an EC2 instance instead of an S3 bucket would be more costly.


- INCORRECT "Host the website using AWS Elastic Beanstalk, and map a Route 53 Alias record to the Beanstalk stack" is

  incorrect. Elastic Beanstalk provisions EC2 instances so again this would be a more costly option.


- INCORRECT "Host the website on an Amazon EC2 instance with ELB and Auto Scaling, and map a Route 53 Alias record to

  the ELB endpoint" is incorrect. Using an EC2 instance instead of an S3 bucket would be more costly.


**References:**


https://aws.amazon.com/premiumsupport/knowledge-center/cloudfront-serve-static-website/


**Save time with our exam-specific cheat sheets:**


https://docs.aws.amazon.com/AmazonS3/latest/dev/website-hosting-custom-domain-walkthrough.html

