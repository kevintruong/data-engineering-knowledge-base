## Quiz 49: An application you manage uses Auto Scaling and a fleet of EC2 instances. You recently noticed that Auto Scaling is scaling the number of instances up and down multiple times in the same hour. You need to implement a remediation to reduce the amount of scaling events. The remediation must be cost-effective and preserve elasticity. What design changes would you implement? (Select TWO)**

- [x] Modify the CloudWatch alarm period that triggers your Auto Scaling scale down policy
- [ ] Modify the Auto Scaling group termination policy to terminate the newest instance first
- [ ] Modify the Auto Scaling group termination policy to terminate the oldest instance first
- [x] Modify the Auto Scaling group cool-down timers
- [ ] Modify the Auto Scaling policy to use scheduled scaling actions

----
Answer: 1,4
**Explanation:**
The cooldown period is a configurable setting for your Auto Scaling group that helps to ensure that it doesn’t launch or terminate additional instances before the previous scaling activity takes effect so this would help. After the Auto Scaling group dynamically scales using a simple scaling policy, it waits for the cooldown period to complete before resuming scaling activities. The CloudWatch Alarm Evaluation Period is the number of the most recent data points to evaluate when determining alarm state. This would help as you can increase the number of datapoints required to trigger an alarm.
---- 

- ✅: "Modify the CloudWatch alarm period that triggers your Auto Scaling scale down policy" is the correct answer.

- ✅: "Modify the Auto Scaling group cool-down timers" is the correct answer.

- ❌: "Modify the Auto Scaling group termination policy to terminate the newest instance first" is incorrect. The order in which Auto Scaling terminates instances is not the issue here, the problem is that the workload is dynamic and Auto Scaling is constantly reacting to change, and launching or terminating instances.

- ❌: "Modify the Auto Scaling group termination policy to terminate the oldest instance first" is incorrect. As per the previous explanation, the order of termination is not the issue here.

- ❌: "Modify the Auto Scaling policy to use scheduled scaling actions" is incorrect. Using scheduled scaling actions may not be cost-effective and also affects elasticity as it is less dynamic.
  **References:**
  https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarm-

evaluation scaling/
