**Explanation:**

The lower threshold may be set too high. With the lower threshold if the metric falls below this number for the breach

duration, a scaling operation is triggered. If it’s set too high you may find that your Auto Scaling group does not

scale-in when required.

- ✅ :  "Modify the lower threshold settings on the ASG" is the correct answer.

- ❌ :  "Modify the upper threshold settings on the ASG" is incorrect. The upper threshold is the metric that, if

  the metric exceeds this number for the breach duration, a scaling operation is triggered. This would be adjusted when

  you need to change the behaviour of scale-out events.

- ❌ :  "Modify the scale down increment" is incorrect. The scale down increment defines the number of EC2 instances

  to remove when performing a scaling activity. This changes the number of instances that are removed but does not

  change the conditions in which they are removed which is the problem we need to solve here.

- ❌ :  "Modify the scaling settings on the ELB" is incorrect. You do not change scaling settings on an ELB, you

  change them on the Auto Scaling group.

**References:**

<https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environments-cfg-autoscaling-triggers.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/aws-auto>- scaling/

----

- #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/aws-auto>-_scaling/> #auto_scaling_group #scaling_activity #scaling_settings #breach_duration
