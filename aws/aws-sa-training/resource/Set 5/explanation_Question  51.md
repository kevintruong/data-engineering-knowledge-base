*

**Explanation:**

You can attach one or more Target Groups to your ASG to include instances behind an ALB and the ELBs must be in the same

region. Once you do this any EC2 instance existing or added by the ASG will be automatically registered with the ASG

defined ELBs. If adding an instance to an ASG would result in exceeding the maximum capacity of the ASG the request will

fail.

* ✅ :  "Adding the 10 EC2 instances to the ASG would exceed the maximum capacity configured" is the correct answer.

* ❌ :  "One or more of the instances are unhealthy" is incorrect. After the load balancer enters the InService

  state, Amazon EC2 Auto Scaling terminates and replaces any instances that are reported as unhealthy. However, in this

  case the request immediately failed so having one or more unhealthy instances is not the issue.

* ❌ :  "ASGs cannot be edited once defined, you would need to recreate it" is incorrect. Auto Scaling Groups can be

  edited once created (however launch configurations cannot be edited).

* ❌ :  "You cannot attach running EC2 instances to an ASG" is incorrect. You can attach running EC2 instances to an

  ASG.

**References:**

<https://docs.aws.amazon.com/autoscaling/ec2/userguide/attach-load-balancer-asg.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/aws-auto>- scaling/

----
* #<https://docs.aws.amazon.com/autoscaling/ec2/userguide/attach-load-balancer-asg.html> #amazon_ec2_auto_scaling #ec2_instances #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/aws-auto>-_scaling/> #ec2_instance
