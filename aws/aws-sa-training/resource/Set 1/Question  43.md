#### Question  43


**A Solutions Architect needs to improve performance for a web application running on EC2 instances launched by an Auto

Scaling group. The instances run behind an ELB Application Load Balancer. During heavy use periods the ASG doubles in

size and analysis has shown that static content stored on the EC2 instances is being requested by users in a specific

geographic location.**


**How can the Solutions Architect reduce the need to scale and improve the application performance?**


1: Store the contents on Amazon EFS instead of the EC2 root volume


2: Implement Amazon Redshift to create a repository of the content closer to the users


3: Create an Amazon CloudFront distribution for the site and redirect user traffic to the distribution


4: Re-deploy the application in a new VPC that is closer to the users making the requests


Answer: 3


**Explanation:**


This is a good use case for CloudFront. CloudFront is a content delivery network (CDN) that caches content closer to

users. You can cache the static content on CloudFront using the EC2 instances as origins for the content. This will

improve performance (as the content is closer to the users) and reduce the need for the ASG to scale (as you don’t need

the processing power of the EC2 instances to serve the static content).


- CORRECT "Create an Amazon CloudFront distribution for the site and redirect user traffic to the distribution"

  is the correct answer.


- INCORRECT "Store the contents on Amazon EFS instead of the EC2 root volume" is incorrect. Using EFS instead of the EC2

  root volume does not solve either problem.


- INCORRECT "Implement Amazon Redshift to create a repository of the content closer to the users" is incorrect. RedShift

  cannot be used to create content repositories to get content closer to users, it’s a data warehouse used for

  analytics.


- INCORRECT "Re-deploy the application in a new VPC that is closer to the users making the requests" is incorrect.

  Re-deploying the application in a VPC closer to the users may reduce latency (and therefore improve performance), but

  it doesn’t solve the problem of reducing the need for the ASG to scale.


**References:**


https://aws.amazon.com/caching/cdn/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-

delivery/amazon-cloudfront/

