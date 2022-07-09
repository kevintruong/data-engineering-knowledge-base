#### Question  49


**A Solutions Architect just completed the implementation of a 2-tier web application for a client. The application uses

Amazon EC2 instances, Amazon ELB and Auto Scaling across two subnets. After deployment the Solutions Architect noticed

that only one subnet has EC2 instances running in it. What might be the cause of this situation?**


1: The ELB is configured as an internal-only load balancer


2: The Auto Scaling Group has not been configured with multiple subnets


3: Cross-zone load balancing is not enabled on the ELB


4: The AMI is missing from the ASG’s launch configuration


**Answer: 2**


**Explanation:**


You can specify which subnets Auto Scaling will launch new instances into. Auto Scaling will try to distribute EC2

instances evenly across AZs. If only one subnet has EC2 instances running in it the first thing to check is that you

have added all relevant subnets to the configuration.


- CORRECT "The Auto Scaling Group has not been configured with multiple subnets" is the correct answer.


- INCORRECT "The ELB is configured as an internal-only load balancer" is incorrect. The type of ELB deployed is not

  relevant here as Auto Scaling is responsible for launching instances into subnets whereas ELB is responsible for

  distributing connections to the instances.


- INCORRECT "Cross-zone load balancing is not enabled on the ELB" is incorrect. Cross-zone load balancing is an ELB

  feature and ELB is not the issue here as it is not responsible for launching instances into subnets.


- INCORRECT "The AMI is missing from the ASG’s launch configuration" is incorrect. If the AMI was missing from the

  launch configuration no instances would be running.


**References:**


https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-in-vpc.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/aws-auto-

scaling/

