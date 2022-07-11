**Explanation:**

AWS Global Accelerator is a service that improves the availability and performance of applications with local or global

users. You can configure the ALB as a target and Global Accelerator will automatically route users to the closest point

of presence.

Failover is automatic and does not rely on any client side cache changes as the IP addresses for Global Accelerator are

static anycast addresses. Global Accelerator also uses the AWS global network which ensures consistent performance.

- ✅ :  "Configure AWS Global Accelerator and configure the ALBs as targets" is the correct answer.

- ❌ :  "Place an EC2 Proxy in front of the ALB and configure automatic failover" is incorrect. Placing an EC2 proxy

  in front of the ALB does not meet the requirements. This solution does not ensure deterministic routing the closest

  region and failover is happening within a region which does not protect against regional failure. Also, this

  introduces a potential bottleneck and lack of redundancy.

- ❌ :  "Create a Route 53 Alias record for each ALB and configure a latency-based routing policy" is incorrect. A

  Route 53 Alias record for each ALB with latency-based routing does provide routing based on latency and failover.

  However, the traffic will not traverse the AWS global network.

- ❌ :  "Use a CloudFront distribution with multiple custom origins in each region and configure for high

  availability" is incorrect. You can use CloudFront with multiple custom origins and configure for HA. However, the

  traffic will not traverse the AWS global network.

**References:**

<https://aws.amazon.com/global-accelerator/>

<https://aws.amazon.com/global-accelerator/faqs/>

<https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content>-

delivery/aws-global-accelerator/

```

Users in US Amazon Route 53

```

```

Resolve dctlabs.com

```

```

Answer:

51. 45. 2. 12

53. 58. 31. 89

```

```

dctlabs.comin

us-east- 1

```

```

Edge location

```

```

dctlabs.comin

eu-central- 1

```

```

Addresses:

51. 45. 2. 12

53. 58. 31. 89

```

```

Addresses:

51. 45. 2. 12

53. 58. 31. 89

```

```

Uses the AWS

global network

```

```

Static anycast IP

addresses

```

----

- #<https://aws.amazon.com/global-accelerator/_>> #aws #alb #albs #configure_aws
