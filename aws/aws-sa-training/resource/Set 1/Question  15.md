#### Question  15


**A company runs a web application that serves weather updates. The application runs on a fleet of Amazon EC2 instances

in a Multi-AZ Auto scaling group behind an Application Load Balancer (ALB). The instances**


**store data in an Amazon Aurora database. A solutions architect needs to make the application more resilient to

sporadic increases in request rates.**


**Which architecture should the solutions architect implement? (Select TWO)**


1: Add and AWS WAF in front of the ALB


2: Add Amazon Aurora Replicas


3: Add an AWS Transit Gateway to the Availability Zones


4: Add an AWS Global Accelerator endpoint


5: Add an Amazon CloudFront distribution in front of the ALB


Answer: 2, 5


**Explanation:**


The architecture is already highly resilient but may be subject to performance degradation if there are sudden increases

in request rates. To resolve this situation Amazon Aurora Read Replicas can be used to serve read traffic which offloads

requests from the main database. On the frontend an Amazon CloudFront distribution can be placed in front of the ALB and

this will cache content for better performance and also offloads requests from the backend.


- CORRECT "Add Amazon Aurora Replicas" is the correct answer.


- CORRECT "Add an Amazon CloudFront distribution in front of the ALB" is the correct answer.


- INCORRECT "Add and AWS WAF in front of the ALB" is incorrect. A web application firewall protects applications from

  malicious attacks. It does not improve performance.


- INCORRECT "Add an AWS Transit Gateway to the Availability Zones" is incorrect as this is used to connect on- premises

  networks to VPCs.


- INCORRECT "Add an AWS Global Accelerator endpoint" is incorrect as this service is used for directing users to

  different instances of the application in different regions based on latency.


**References:**


https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Replication.html


https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-aurora/


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-

delivery/amazon-cloudfront/

