#### Question  29


**An Auto Scaling group of Amazon EC2 instances behind an Elastic Load Balancer (ELB) is running in an Amazon VPC.

Health checks are configured on the ASG to use EC2 status checks. The ELB has determined that an EC2 instance is

unhealthy and has removed it from service. A Solutions Architect noticed that the instance is still running and has not

been terminated by EC2 Auto Scaling.**


**What would be an explanation for this behavior?**


- [ ] The ASG is waiting for the cooldown timer to expire before terminating the instance


- [ ] Connection draining is enabled and the ASG is waiting for in-flight requests to complete


- [x] The ELB health check type has not been selected for the ASG and so it is unaware that the instance has been

determined to be unhealthy by the ELB and has been removed from service


- [ ] The health check grace period has not yet expired


*

- hasExplain:: [[explanation_Question  29.md]]