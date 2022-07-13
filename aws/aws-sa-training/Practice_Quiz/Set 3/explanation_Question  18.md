**Explanation:**

You can use Route 53 to check the health of your resources and only return healthy resources in response to DNS queries.

There are three types of DNS failover configurations:

1. Active-passive: Route 53 actively returns a primary resource. In case of failure, Route 53 returns the backup

   resource. Configured using a failover policy.

2. Active-active: Route 53 actively returns more than one resource. In case of failure, Route 53 fails back to the

   healthy resource. Configured using any routing policy besides failover.

3. Combination: Multiple routing policies (such as latency-based, weighted, etc.) are combined into a tree to configure

   more complex DNS failover.

In this case an alias already exists for the secondary ALB. Therefore, the solutions architect just needs to enable a

failover configuration with an Amazon Route 53 health check.

The configuration would look something like this:

- ✅ :  "Enable an Amazon Route 53 health check" is the correct answer.

- ❌ :  "Enable an ALB health check" is incorrect. The point of an ALB health check is to identify the health of

  targets (EC2 instances). It cannot redirect clients to another Region.

- ❌ :  "Create a CNAME record on Amazon Route 53 pointing to the ALB endpoint" is incorrect as an Alias record

  already exists and is better for mapping to an ALB.

- ❌ :  "Create a latency based routing policy on Amazon Route 53" is incorrect as this will only take into account

  latency, it is not used for failover.

**References:**

<https://aws.amazon.com/premiumsupport/knowledge-center/route>- 53 - dns-health-checks/

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content>-

delivery/amazon-route-53/

----

- #dns_failover_configurations #complex_dns_failover #failover_configuration #failover_policy #alb_health_check
