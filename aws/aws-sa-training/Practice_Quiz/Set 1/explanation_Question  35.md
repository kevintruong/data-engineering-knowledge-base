**Explanation:**

AWS Global Accelerator uses the vast, congestion-free AWS global network to route TCP and UDP traffic to a healthy

application endpoint in the closest AWS Region to the user.

This means it will intelligently route traffic to the closest point of presence (reducing latency). Seamless failover is

ensured as AWS Global Accelerator uses anycast IP address which means the IP does not change when failing over between

regions so there are no issues with client caches having incorrect entries that need to expire.

This is the only solution that provides deterministic failover.

- ✅ :  "Launch EC2 instances into multiple regions behind an NLB and use AWS Global Accelerator" is the correct

  answer.

- ❌ :  "Launch EC2 instances into multiple regions behind an NLB with a static IP address" is incorrect. An NLB

  with a static IP is a workable solution as you could configure a primary and secondary address in applications.

  However, this solution does not intelligently route traffic for lowest latency.

- ❌ :  "Launch EC2 instances into multiple regions behind an ALB and use a Route 53 failover routing policy" is

  incorrect. A Route 53 failover routing policy uses a primary and standby configuration. Therefore, it sends all

  traffic to the primary until it fails a health check at which time it sends traffic to the secondary. This solution

  does not intelligently route traffic for lowest latency.

- ❌ :  "Launch EC2 instances into multiple regions behind an ALB and use Amazon CloudFront with a pair of static IP

  addresses" is incorrect. Amazon CloudFront cannot be configured with “a pair of static IP addresses”.

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

- #aws_global_accelerator #closest_aws_region #seamless_failover #<https://aws.amazon.com/global-accelerator/_>> #aws
