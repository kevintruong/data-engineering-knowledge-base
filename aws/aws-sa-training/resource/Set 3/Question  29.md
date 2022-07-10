#### Question  29

**A web application is running on a fleet of Amazon EC2 instances using an Auto Scaling Group. It is desired that the

CPU usage in the fleet is kept at 40%.**

**How should scaling be configured?**

- [ ] :  Use a simple scaling policy that launches instances when the average CPU hits 40%

- [x] :  Use a target tracking policy that keeps the average aggregate CPU utilization at 40%

- [ ] :  Use a step scaling policy that uses the PercentChangeInCapacity value to adjust the group size as required

- [ ] :  Use a custom CloudWatch alarm to monitor CPU usage and notify the ASG using Amazon SNS

----

- #step_scaling_policy #simple_scaling_policy #auto_scaling_group #average_aggregate_cpu_utilization #amazon_ec2_instances
- hasExplain:: [[explanation_Question  29.md]]
