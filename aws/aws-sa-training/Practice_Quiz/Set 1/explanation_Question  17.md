**Explanation:**

The Amazon EC2-based application must be highly available and elastically scalable. Auto Scaling can provide the

elasticity by dynamically launching and terminating instances based on demand. This can take place across availability

zones for high availability.

Incoming connections can be distributed to the instances by using an Application Load Balancer (ALB).

- ✅ :  "Configure an Application Load Balancer in front of an Auto Scaling group to deploy instances to multiple

  Availability Zones" is the correct answer.

- ❌ :  "Configure an Amazon API Gateway API in front of an Auto Scaling group to deploy instances to multiple

  Availability Zones" is incorrect as API gateway is not used for load balancing connections to Amazon EC2 instances.

- ❌ :  "Configure an Application Load Balancer in front of an Auto Scaling group to deploy instances to multiple

  Regions" is incorrect as you cannot launch instances in multiple Regions from a single Auto Scaling group.

- ❌ :  "Configure an Amazon CloudFront distribution in front of an Auto Scaling group to deploy instances to

  multiple Regions" is incorrect as you cannot launch instances in multiple Regions from a single Auto Scaling group.

**References:**

<https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html>

<https://aws.amazon.com/elasticloadbalancing/>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/aws-auto>- scaling/

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/elastic-load>-

balancing/

----

- #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/aws-auto>-_scaling/> #amazon_api_gateway_api #<https://aws.amazon.com/elasticloadbalancing/> #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/elastic-load>>- #application_load_balancer
