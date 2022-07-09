#### Question  41


**A Solutions Architect is creating an application design with several components that will be publicly addressable. The

Architect would like to use Alias records. Using Route 53 Alias records what targets can you specify? (Select TWO)**


1: CloudFront distribution


2: ElastiCache cluster


3: EFS filesystems


4: Elastic Beanstalk environment


5: On-premise web server


**Answer: 1,4**


**Explanation:**


Alias records are used to map resource record sets in your hosted zone to Amazon Elastic Load Balancing load balancers,

API Gateway custom regional APIs and edge-optimized APIs, CloudFront Distributions, AWS Elastic Beanstalk environments,

Amazon S3 buckets that are configured as website endpoints, Amazon VPC interface endpoints, and to other records in the

same Hosted Zone.


- CORRECT "CloudFront distribution" is the correct answer.


- CORRECT "Elastic Beanstalk environment" is the correct answer.


- INCORRECT "ElastiCache cluster" is incorrect. You cannot use an Alias to point at an ElastiCache cluster or VPC

  endpoint.


- INCORRECT "EFS filesystems" is incorrect. You cannot use an Alias to point to an EFS filesystem.


- INCORRECT "On-premise web server" is incorrect. You cannot point an Alias record directly at an on-premises web

  server (you can point to another record in a hosted zone, which could point to an on-premises web server though I’m

  not sure if this is supported).


**References:**


https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-choosing-alias-non-

alias.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-

delivery/amazon-route-53/

