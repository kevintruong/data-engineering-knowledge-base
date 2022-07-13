*

**Explanation:**

If using an ELB it is best to enable ELB health checks as otherwise EC2 status checks may show an instance as being

healthy that the ELB has determined is unhealthy. In this case the instance will be removed from service by the ELB but

will not be terminated by Auto Scaling

More information on ASG health checks:

* By default, uses EC2 status checks.

* Can also use ELB health checks and custom health checks.

* ELB health checks are in addition to the EC2 status checks.

* If any health check returns an unhealthy status the instance will be terminated.

* With ELB an instance is marked as unhealthy if ELB reports it as OutOfService

* A healthy instance enters the InService state.

* If an instance is marked as unhealthy it will be scheduled for replacement.

* If connection draining is enabled, Auto Scaling waits for in-flight requests to complete or timeout before terminating

  instances.

* The health check grace period allows a period of time for a new instance to warm up before performing a health check (

  300 seconds by default).

* ✅ :  "The ELB health check type has not been selected for the ASG and so it is unaware that the instance has been

  determined to be unhealthy by the ELB and has been removed from service" is the correct answer.

* ❌ :  "The ASG is waiting for the cooldown timer to expire before terminating the instance" is incorrect as the

  ASG does not wait for the cooldown time to expire.

* ❌ :  "Connection draining is enabled and the ASG is waiting for in-flight requests to complete" is incorrect.

  Connection draining is not the correct answer as the ELB has taken the instance out of service so there are no active

  connections.

* ❌ :  "The health check grace period has not yet expired" is incorrect. The health check grace period allows a

  period of time for a new instance to warm up before performing a health check.

**References:**

<https://docs.aws.amazon.com/autoscaling/ec2/userguide/AutoScalingGroupLifecycle.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/aws-auto>- scaling/

----
* #elb_health_checks #elb_health_check_type #elb #ec2_status_checks #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/aws-auto>-_scaling/>
