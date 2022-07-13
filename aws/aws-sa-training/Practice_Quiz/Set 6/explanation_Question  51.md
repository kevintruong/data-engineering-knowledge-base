*

**Explanation:**

An Application Load Balancer periodically sends requests to its registered targets to test their status. These tests are

called _health checks_.

Each load balancer node routes requests only to the healthy targets in the enabled Availability Zones for the load

balancer. Each load balancer node checks the health of each target, using the health check settings for the target

groups with which the target is registered. After your target is registered, it must pass one health check to be

considered healthy. After each health check is completed, the load balancer node closes the connection that was

established for the health check.

If a target group contains only unhealthy registered targets, the load balancer nodes route requests across its

unhealthy targets.

For an ALB the possible protocols are HTTP and HTTPS. The default is the HTTP protocol.

* ✅ :  "HTTP" is the correct answer.

* ✅ :  "HTTPS" is the correct answer.

* ❌ :  "SSL" is incorrect as this is not supported by the ALB.

* ❌ :  "TCP" is incorrect as this is not supported by the ALB.

* ❌ :  "ICMP" is incorrect as this is not supported by the ALB.

**References:**

<https://docs.aws.amazon.com/elasticloadbalancing/latest/network/target-group-health-checks.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/elastic-load>-

balancing/

----
* #<https://docs.aws.amazon.com/elasticloadbalancing/latest/network/target-group-health-checks.html> #load_balancer_node #application_load_balancer #load_balancer_nodes_route_requests #load_balancer_node_routes_requests
