#### Question  51

**An existing Auto Scaling group is running with eight Amazon EC2 instances. A Solutions Architect has attached an

Elastic Load Balancer (ELB) to the Auto Scaling group by connecting a Target Group. The ELB is in the same region and

already has ten EC2 instances running in the Target Group.**

**When attempting to attach the ELB the request immediately fails, what is the MOST likely cause?**

- [x] :  Adding the 10 EC2 instances to the ASG would exceed the maximum capacity configured

- [ ] :  One or more of the instances are unhealthy

- [ ] :  ASGs cannot be edited once defined, you would need to recreate it

- [ ] :  You cannot attach running EC2 instances to an ASG

*----

- #ec2_instances #elastic_load_balancer #auto_scaling_group #amazon_ec2 #elb
- hasExplain:: [[explanation_Question  51.md]]
