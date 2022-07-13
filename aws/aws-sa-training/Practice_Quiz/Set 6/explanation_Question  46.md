*

**Explanation:**

Route 53 weighted routing policy is similar to simple but you can specify a weight per IP address. You create records

that have the same name and type and assign each record a relative weight which is a numerical value that favors one IP

over another (values must total 100). To stop sending traffic to a resource you can change the weight of the record to

0.

* ✅ :  "Use Route 53 with a weighted routing policy and configure the respective weights" is the correct answer.

* ❌ :  "Use Route 53 with a simple routing policy" is incorrect as this will not split traffic based on weights as

  required.

* ❌ :  "Use an Application Load Balancer to distribute traffic based on IP address" is incorrect. Application Load

  Balancer can distribute traffic to AWS and on-premise resources using IP addresses but cannot be used to distribute

  traffic in a weighted manner.

* ❌ :  "Use a Network Load Balancer to distribute traffic based on Instance ID" is incorrect. Network Load Balancer

  can distribute traffic to AWS and on-premise resources using IP addresses (not Instance IDs).

**References:**

<https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/elastic-load>-

balancing/

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content>-

delivery/amazon-route-53/

----
* #network_load_balancer #application_load_balancer #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/elastic-load>>- #weighted_manner #weights
