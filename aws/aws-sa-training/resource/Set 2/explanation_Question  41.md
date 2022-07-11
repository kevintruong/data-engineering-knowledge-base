**Explanation:**

You can passthrough encrypted traffic with an NLB and terminate the SSL on the EC2 instances, so this is a valid answer.

You can use a HTTPS listener with an ALB and install certificates on both the ALB and EC2 instances. This does not use

passthrough, instead it will terminate the first SSL connection on the ALB and then re-encrypt the traffic and connect

to the EC2 instances.

- ✅ :  "Use a Network Load Balancer (NLB) with a TCP listener, then terminate SSL on EC2 instances" is the correct

  answer.

- ✅ :  "Use an Application Load Balancer (ALB) with an HTTPS listener, then install SSL certificates on the ALB and

  EC2 instances" is the correct answer.

- ❌ :  "Use an Application Load Balancer (ALB) in passthrough mode, then terminate SSL on EC2 instances" is

  incorrect. You cannot use passthrough mode with an ALB and terminate SSL on the EC2 instances.

- ❌ :  "Use a Network Load Balancer (NLB) with an HTTPS listener, then install SSL certificates on the NLB and EC2

  instances" is incorrect. You cannot use a HTTPS listener with an NLB.

- ❌ :  "Use an Application Load Balancer (ALB) with a TCP listener, then terminate SSL on EC2 instances"

  is incorrect. You cannot use a TCP listener with an ALB.

**References:**

<https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/elastic-load>-

balancing/

----

- #ec2_instances #<https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html> #ec2 #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/elastic-load>>- #application_load_balancer
