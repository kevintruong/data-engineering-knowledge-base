**Explanation:**

The architecture is already highly resilient but may be subject to performance degradation if there are sudden increases

in request rates. To resolve this situation Amazon Aurora Read Replicas can be used to serve read traffic which offloads

requests from the main database. On the frontend an Amazon CloudFront distribution can be placed in front of the ALB and

this will cache content for better performance and also offloads requests from the backend.

- ✅ :  "Add Amazon Aurora Replicas" is the correct answer.

- ✅ :  "Add an Amazon CloudFront distribution in front of the ALB" is the correct answer.

- ❌ :  "Add and AWS WAF in front of the ALB" is incorrect. A web application firewall protects applications from

  malicious attacks. It does not improve performance.

- ❌ :  "Add an AWS Transit Gateway to the Availability Zones" is incorrect as this is used to connect on- premises

  networks to VPCs.

- ❌ :  "Add an AWS Global Accelerator endpoint" is incorrect as this service is used for directing users to

  different instances of the application in different regions based on latency.

**References:**

<https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Replication.html>

<https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-aurora/>

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content>-

delivery/amazon-cloudfront/

----

- #aws_waf #amazon_cloudfront_distribution #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-aurora/_>> #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content>>- #aws_global_accelerator_endpoint
