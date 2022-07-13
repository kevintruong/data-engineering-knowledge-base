**Explanation:**

With target tracking scaling policies, you select a scaling metric and set a target value. Amazon EC2 Auto Scaling

creates and manages the CloudWatch alarms that trigger the scaling policy and calculates the scaling adjustment based on

the metric and the target value.

The scaling policy adds or removes capacity as required to keep the metric at, or close to, the specified target value.

In addition to keeping the metric close to the target value, a target tracking scaling policy also adjusts to the

changes in the metric due to a changing load pattern.

- ✅ :  "Use a target tracking policy to dynamically scale the Auto Scaling group" is the correct answer.

- ❌ :  "Use a simple scaling policy to dynamically scale the Auto Scaling group" is incorrect as target tracking is

  a better way to keep the aggregate CPU usage at around 40%

- ❌ :  "Use an AWS Lambda function to update the desired Auto Scaling group capacity" is incorrect as this can be

  done automatically.

- ❌ :  "Use scheduled scaling actions to scale up and scale down the Auto Scaling group" is incorrect as dynamic

  scaling is required to respond to changes in utilization.

**References:**

<https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/aws-auto>- scaling/

----

- #amazon_ec2_auto_scaling #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/aws-auto>-_scaling/> #auto_scaling_group_capacity #auto_scaling_group #simple_scaling_policy
