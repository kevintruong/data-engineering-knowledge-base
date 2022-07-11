**Explanation:**

Scheduled scaling allows you to set your own scaling schedule. In this case the scaling action can be scheduled to occur

just prior to the time that the reports will be run each month. Scaling actions are performed

automatically as a function of time and date. This will ensure that there are enough EC2 instances to serve the demand

and prevent the application from slowing down.

- ✅ :  "Configure an EC2 Auto Scaling scheduled scaling policy based on the monthly schedule" is the correct answer.

- ❌ :  "Configure an Amazon CloudFront distribution in front of the ALB" is incorrect as this would be more

  suitable for providing access to global users by caching content.

- ❌ :  "Configure an EC2 Auto Scaling simple scaling policy based on CPU utilization" is incorrect as this would

  not prevent the slow-down from occurring as there would be a delay between when the CPU hits 100% and the metric being

  reported and additional instances being launched.

- ❌ :  "Configure Amazon ElastiCache to remove some of the workload from the EC2 instances" is incorrect as

  ElastiCache is a database cache, it cannot replace the compute functions of an EC2 instance.

**References:**

<https://docs.aws.amazon.com/autoscaling/ec2/userguide/schedule_time.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/aws-auto>- scaling/

----

- #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/aws-auto>-_scaling/> #<https://docs.aws.amazon.com/autoscaling/ec2/userguide/schedule_time.html> #ec2_auto_scaling #configure_amazon_elasticache #own_scaling_schedule
