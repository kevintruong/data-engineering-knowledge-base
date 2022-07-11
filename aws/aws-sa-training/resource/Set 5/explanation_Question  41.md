*

**Explanation:**

Alias records are used to map resource record sets in your hosted zone to Amazon Elastic Load Balancing load balancers,

API Gateway custom regional APIs and edge-optimized APIs, CloudFront Distributions, AWS Elastic Beanstalk environments,

Amazon S3 buckets that are configured as website endpoints, Amazon VPC interface endpoints, and to other records in the

same Hosted Zone.

* ✅ :  "CloudFront distribution" is the correct answer.

* ✅ :  "Elastic Beanstalk environment" is the correct answer.

* ❌ :  "ElastiCache cluster" is incorrect. You cannot use an Alias to point at an ElastiCache cluster or VPC

  endpoint.

* ❌ :  "EFS filesystems" is incorrect. You cannot use an Alias to point to an EFS filesystem.

* ❌ :  "On-premise web server" is incorrect. You cannot point an Alias record directly at an on-premises web

  server (you can point to another record in a hosted zone, which could point to an on-premises web server though I’m

  not sure if this is supported).

**References:**

<https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-choosing-alias-non>- alias.html

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content>-

delivery/amazon-route-53/

----
* #<https://docs.aws.amazon.com/route53/latest/developerguide/resource-record-sets-choosing-alias-non>-_alias.html> #elasticache_cluster #elastic_beanstalk_environment #elastic_beanstalk_environments #aws
