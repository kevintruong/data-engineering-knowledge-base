#### Question  3


**A company delivers content to subscribers distributed globally from an application running on AWS. The application

uses a fleet of Amazon EC2 instance in a private subnet behind an Application Load Balancer

(ALB). Due to an update in copyright restrictions, it is necessary to block access for specific countries.**


**What is the EASIEST method to meet this requirement?**


1: Modify the ALB security group to deny incoming traffic from blocked countries


2: Modify the security group for EC2 instances to deny incoming traffic from blocked countries


3: Use Amazon CloudFront to serve the application and deny access to blocked countries


4: Use a network ACL to block the IP address ranges associated with the specific countries


Answer: 3


**Explanation:**


When a user requests your content, CloudFront typically serves the requested content regardless of where the user is

located. If you need to prevent users in specific countries from accessing your content, you can use the CloudFront geo

restriction feature to do one of the following:


- Allow your users to access your content only if they're in one of the countries on a whitelist of approved countries.

- Prevent your users from accessing your content if they're in one of the countries on a blacklist of banned countries.


For example, if a request comes from a country where, for copyright reasons, you are not authorized to distribute your

content, you can use CloudFront geo restriction to block the request.


This is the easiest and most effective way to implement a geographic restriction for the delivery of content.


- CORRECT "Use Amazon CloudFront to serve the application and deny access to blocked countries" is the correct answer.


- INCORRECT "Use a Network ACL to block the IP address ranges associated with the specific countries" is incorrect as

  this would be extremely difficult to manage.


- INCORRECT "Modify the ALB security group to deny incoming traffic from blocked countries" is incorrect as security

  groups cannot block traffic by country.


- INCORRECT "Modify the security group for EC2 instances to deny incoming traffic from blocked countries" is incorrect

  as security groups cannot block traffic by country.


**References:**


https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/georestrictions.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-

delivery/amazon-cloudfront/

