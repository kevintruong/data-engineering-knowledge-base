**Explanation:**

Though this sounds like a good use case for scheduled actions, both answers using scheduled actions will have 20

instances running regardless of actual demand. A better option to be more cost effective is to use a target tracking

action that triggers at a lower CPU threshold.

With this solution the scaling will occur before the CPU utilization gets to a point where performance is affected. This

will result in resolving the performance issues whilst minimizing costs. Using a reduced cooldown period will also more

quickly terminate unneeded instances, further reducing costs.

- ✅ :  "Implement a target tracking action triggered at a lower CPU threshold, and decrease the cooldown period"

  is the correct answer.

- ❌ :  "Implement a scheduled action that sets the desired capacity to 20 shortly before the office opens" is

  incorrect as this is not the most cost-effective option. Note you can choose min, max, or desired for a scheduled

  action.

- ❌ :  "Implement a scheduled action that sets the minimum and maximum capacity to 20 shortly before the office

  opens" is incorrect as this is not the most cost-effective option. Note you can choose min, max, or desired for a

  scheduled action.

- ❌ :  "Implement a step scaling action triggered at a lower CPU threshold, and decrease the cooldown period" is

  incorrect as AWS recommend you use target tracking in place of step scaling for most use cases.

**References:**

<https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/aws-auto>- scaling/

----

- #scheduled_actions #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/aws-auto>-_scaling/> #lower_cpu_threshold #step_scaling #cpu_utilization
