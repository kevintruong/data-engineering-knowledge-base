#### Question  51


**An existing Auto Scaling group is running with eight Amazon EC2 instances. A Solutions Architect has attached an

Elastic Load Balancer (ELB) to the Auto Scaling group by connecting a Target Group. The ELB is in the same region and

already has ten EC2 instances running in the Target Group.**


**When attempting to attach the ELB the request immediately fails, what is the MOST likely cause?**


1: Adding the 10 EC2 instances to the ASG would exceed the maximum capacity configured


2: One or more of the instances are unhealthy


3: ASGs cannot be edited once defined, you would need to recreate it


4: You cannot attach running EC2 instances to an ASG


**Answer: 1**


**Explanation:**


You can attach one or more Target Groups to your ASG to include instances behind an ALB and the ELBs must be in the same

region. Once you do this any EC2 instance existing or added by the ASG will be automatically registered with the ASG

defined ELBs. If adding an instance to an ASG would result in exceeding the maximum capacity of the ASG the request will

fail.


- CORRECT "Adding the 10 EC2 instances to the ASG would exceed the maximum capacity configured" is the correct answer.


- INCORRECT "One or more of the instances are unhealthy" is incorrect. After the load balancer enters the InService

  state, Amazon EC2 Auto Scaling terminates and replaces any instances that are reported as unhealthy. However, in this

  case the request immediately failed so having one or more unhealthy instances is not the issue.


- INCORRECT "ASGs cannot be edited once defined, you would need to recreate it" is incorrect. Auto Scaling Groups can be

  edited once created (however launch configurations cannot be edited).


- INCORRECT "You cannot attach running EC2 instances to an ASG" is incorrect. You can attach running EC2 instances to an

  ASG.


**References:**


https://docs.aws.amazon.com/autoscaling/ec2/userguide/attach-load-balancer-asg.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/aws-auto-

scaling/

