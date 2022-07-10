#### Question  54


**An application in an Amazon VPC uses an Auto Scaling Group that spans 3 AZs and there are currently 4 Amazon EC2

instances running in the group. What actions will Auto Scaling take, by default, if it needs to terminate an EC2

instance?**


- [ ] Randomly select one of the 3 AZs, and then terminate an instance in that AZ


- [ ] Terminate the instance with the least active network connections. If multiple instances meet this criterion, one will

be randomly selected


- [ ] Send an SNS notification, if configured to do so


4 : Wait for the cooldown period and then terminate the instance that has been running the longest


- [ ] Terminate an instance in the AZ which currently has 2 running EC2 instances


*