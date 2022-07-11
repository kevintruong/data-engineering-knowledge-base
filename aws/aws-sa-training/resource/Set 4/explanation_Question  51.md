*

**Explanation:**

The failover routing policy is used for active/passive configurations. Alias records can be used to map the domain

apex (example.com) to the Elastic Load Balancers.

Failover routing lets you route traffic to a resource when the resource is healthy or to a different resource when the

first resource is unhealthy. The primary and secondary records can route traffic to anything from an Amazon S3 bucket

that is configured as a website to a complex tree of records.

* ✅ :  "Use a Failover Routing Policy" is a correct answer.

* ✅ :  "Connect the ELBs using Alias records" is also a correct answer.

* ❌ :  "Set Evaluate Target Health to “No” for the primary" is incorrect. For Evaluate Target Health choose Yes for

  your primary record and choose No for your secondary record. For your primary record choose Yes for Associate with

  Health Check. Then for Health Check to Associate select the health check that you created for your primary resource.

* ❌ :  "Use a Weighted Routing Policy" is incorrect. Weighted routing is not an active/passive routing policy. All

  records are active and the traffic is distributed according to the weighting.

* ❌ :  "Connect the ELBs using CNAME records" is incorrect. You cannot use CNAME records for the domain apex

  record, you must use Alias records.

**References:**

<https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-failover>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content>-

delivery/amazon-route-53/

----
* #elastic_load_balancers #<https://docs.aws.amazon.com/route53/latest/developerguide/routing-policy.html#routing-policy-failover> #failover_routing_policy #failover_routing #elbs
