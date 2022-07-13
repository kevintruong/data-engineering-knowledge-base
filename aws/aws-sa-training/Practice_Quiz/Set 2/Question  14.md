#### Question  14

**A company runs an internal browser-based application. The application runs on Amazon EC2 instances behind an

Application Load Balancer. The instances run in an Amazon EC2 Auto Scaling group across multiple Availability Zones. The

Auto Scaling group scales up to 20 instances during work hours, but scales down to 2 instances overnight. Staff are

complaining that the application is very slow when the day begins, although it runs well by midmorning.**

**How should the scaling be changed to address the staff complaints and keep costs to a minimum?**

- [ ] :  Implement a scheduled action that sets the desired capacity to 20 shortly before the office opens

- [ ] :  Implement a step scaling action triggered at a lower CPU threshold, and decrease the cooldown period

- [x] :  Implement a target tracking action triggered at a lower CPU threshold, and decrease the cooldown period

- [ ] :  Implement a scheduled action that sets the minimum and maximum capacity to 20 shortly before the office opens

----

- #amazon_ec2_auto_scaling_group #scaling #auto_scaling_group #application_load_balancer #amazon_ec2_instances
- hasExplain:: [[explanation_Question  14.md]]
