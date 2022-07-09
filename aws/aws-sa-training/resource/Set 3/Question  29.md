#### Question  29


**A web application is running on a fleet of Amazon EC2 instances using an Auto Scaling Group. It is desired that the

CPU usage in the fleet is kept at 40%.**


**How should scaling be configured?**


1: Use a simple scaling policy that launches instances when the average CPU hits 40%


2: Use a target tracking policy that keeps the average aggregate CPU utilization at 40%


3: Use a step scaling policy that uses the PercentChangeInCapacity value to adjust the group size as required


4: Use a custom CloudWatch alarm to monitor CPU usage and notify the ASG using Amazon SNS


Answer: 2


**Explanation:**


This is a perfect use case for a target tracking scaling policy. With target tracking scaling policies, you select a

scaling metric and set a target value. In this case you can just set the target value to 40% average aggregate CPU

utilization.


- CORRECT "Use a target tracking policy that keeps the average aggregate CPU utilization at 40%" is the correct answer.


- INCORRECT "Use a simple scaling policy that launches instances when the average CPU hits 40%" is incorrect. A simple

  scaling policy will add instances when 40% CPU utilization is reached, but it is not designed to maintain 40% CPU

  utilization across the group.


- INCORRECT "Use a step scaling policy that uses the PercentChangeInCapacity value to adjust the group size as required"

  is incorrect. The step scaling policy makes scaling adjustments based on a number of factors. The

  PercentChangeInCapacity value increments or decrements the group size by a specified percentage. This does not relate

  to CPU utilization.


- INCORRECT "Use a custom CloudWatch alarm to monitor CPU usage and notify the ASG using Amazon SNS" is incorrect. You

  do not need to create a custom Amazon CloudWatch alarm as the ASG can scale using a policy based on CPU utilization

  using standard configuration.


**References:**


https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html


https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-simple-step.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/aws-auto-

scaling/

