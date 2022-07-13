*

**Explanation:**

You can specify which subnets Auto Scaling will launch new instances into. Auto Scaling will try to distribute EC2

instances evenly across AZs. If only one subnet has EC2 instances running in it the first thing to check is that you

have added all relevant subnets to the configuration.

* ✅ :  "The Auto Scaling Group has not been configured with multiple subnets" is the correct answer.

* ❌ :  "The ELB is configured as an internal-only load balancer" is incorrect. The type of ELB deployed is not

  relevant here as Auto Scaling is responsible for launching instances into subnets whereas ELB is responsible for

  distributing connections to the instances.

* ❌ :  "Cross-zone load balancing is not enabled on the ELB" is incorrect. Cross-zone load balancing is an ELB

  feature and ELB is not the issue here as it is not responsible for launching instances into subnets.

* ❌ :  "The AMI is missing from the ASG’s launch configuration" is incorrect. If the AMI was missing from the

  launch configuration no instances would be running.

**References:**

<https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-in-vpc.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/aws-auto>- scaling/

----
* #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/aws-auto>>-_scaling/ #elb #ec2_instances #<https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-in-vpc.html> #cross_-_zone_load_balancing
