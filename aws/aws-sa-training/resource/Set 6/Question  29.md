#### Question  29


**An Auto Scaling group of Amazon EC2 instances behind an Elastic Load Balancer (ELB) is running in an Amazon VPC.

Health checks are configured on the ASG to use EC2 status checks. The ELB has determined that an EC2 instance is

unhealthy and has removed it from service. A Solutions Architect noticed that the instance is still running and has not

been terminated by EC2 Auto Scaling.**


**What would be an explanation for this behavior?**


1: The ASG is waiting for the cooldown timer to expire before terminating the instance


2: Connection draining is enabled and the ASG is waiting for in-flight requests to complete


3: The ELB health check type has not been selected for the ASG and so it is unaware that the instance has been

determined to be unhealthy by the ELB and has been removed from service


4: The health check grace period has not yet expired


**Answer: 3**


**Explanation:**


If using an ELB it is best to enable ELB health checks as otherwise EC2 status checks may show an instance as being

healthy that the ELB has determined is unhealthy. In this case the instance will be removed from service by the ELB but

will not be terminated by Auto Scaling


More information on ASG health checks:


- By default, uses EC2 status checks.

- Can also use ELB health checks and custom health checks.

- ELB health checks are in addition to the EC2 status checks.

- If any health check returns an unhealthy status the instance will be terminated.

- With ELB an instance is marked as unhealthy if ELB reports it as OutOfService

- A healthy instance enters the InService state.

- If an instance is marked as unhealthy it will be scheduled for replacement.

- If connection draining is enabled, Auto Scaling waits for in-flight requests to complete or timeout before terminating

  instances.

- The health check grace period allows a period of time for a new instance to warm up before performing a health check (

  300 seconds by default).


- CORRECT "The ELB health check type has not been selected for the ASG and so it is unaware that the instance has been

  determined to be unhealthy by the ELB and has been removed from service" is the correct answer.


- INCORRECT "The ASG is waiting for the cooldown timer to expire before terminating the instance" is incorrect as the

  ASG does not wait for the cooldown time to expire.


- INCORRECT "Connection draining is enabled and the ASG is waiting for in-flight requests to complete" is incorrect.

  Connection draining is not the correct answer as the ELB has taken the instance out of service so there are no active

  connections.


- INCORRECT "The health check grace period has not yet expired" is incorrect. The health check grace period allows a

  period of time for a new instance to warm up before performing a health check.


**References:**


https://docs.aws.amazon.com/autoscaling/ec2/userguide/AutoScalingGroupLifecycle.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/aws-auto-

scaling/

