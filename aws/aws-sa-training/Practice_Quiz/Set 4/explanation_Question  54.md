*

**Explanation:**

Auto Scaling can perform rebalancing when it finds that the number of instances across AZs is not balanced. Auto Scaling

rebalances by launching new EC2 instances in the AZs that have fewer instances first, only then will it start

terminating instances in AZs that had more instances

Auto Scaling can be configured to send an SNS email when:

* An instance is launched.

* An instance is terminated.

* An instance fails to launch.

* An instance fails to terminate.

* ✅ :  "Send an SNS notification, if configured to do so" is a correct answer.

* ✅ :  "Terminate an instance in the AZ which currently has 2 running EC2 instances" is also a correct answer.

* ❌ :  "Terminate the instance with the least active network connections. If multiple instances meet this

  criterion, one will be randomly selected" is incorrect. Auto Scaling will only terminate an instance randomly after it

  has first gone through several other selection steps. Please see the AWS article below for detailed information on the

  process

* ❌ :  "Wait for the cooldown period and then terminate the instance that has been running the longest" is

  incorrect. Auto Scaling does not terminate the instance that has been running the longest.

* ❌ :  "Terminate an instance in the AZ which currently has 2 running EC2 instances" is incorrect as it will launch

  instances in that AZ before terminating.

**References:**

<https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-instance-termination.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/aws-auto>- scaling/

----
* #<https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-instance-termination.html> #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/aws-auto>-_scaling/> #ec2_instances #aws_article #auto_scaling
