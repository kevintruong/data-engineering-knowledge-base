#### Question  12


**A company runs a financial application using an Amazon EC2 Auto Scaling group behind an Application Load Balancer (

ALB). When running month-end reports on a specific day and time each month the application becomes unacceptably slow.

Amazon CloudWatch metrics show the CPU utilization hitting 100%.**


**What should a solutions architect recommend to ensure the application is able to handle the workload and avoid

downtime?**


1: Configure an Amazon CloudFront distribution in front of the ALB


2: Configure an EC2 Auto Scaling simple scaling policy based on CPU utilization


3: Configure an EC2 Auto Scaling scheduled scaling policy based on the monthly schedule


4: Configure Amazon ElastiCache to remove some of the workload from the EC2 instances


Answer: 3


**Explanation:**


Scheduled scaling allows you to set your own scaling schedule. In this case the scaling action can be scheduled to occur

just prior to the time that the reports will be run each month. Scaling actions are performed


automatically as a function of time and date. This will ensure that there are enough EC2 instances to serve the demand

and prevent the application from slowing down.


- CORRECT "Configure an EC2 Auto Scaling scheduled scaling policy based on the monthly schedule" is the correct answer.


- INCORRECT "Configure an Amazon CloudFront distribution in front of the ALB" is incorrect as this would be more

  suitable for providing access to global users by caching content.


- INCORRECT "Configure an EC2 Auto Scaling simple scaling policy based on CPU utilization" is incorrect as this would

  not prevent the slow-down from occurring as there would be a delay between when the CPU hits 100% and the metric being

  reported and additional instances being launched.


- INCORRECT "Configure Amazon ElastiCache to remove some of the workload from the EC2 instances" is incorrect as

  ElastiCache is a database cache, it cannot replace the compute functions of an EC2 instance.


**References:**


https://docs.aws.amazon.com/autoscaling/ec2/userguide/schedule_time.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/aws-auto-

scaling/

