#### Question  54


**An application in an Amazon VPC uses an Auto Scaling Group that spans 3 AZs and there are currently 4 Amazon EC2

instances running in the group. What actions will Auto Scaling take, by default, if it needs to terminate an EC2

instance?**


1: Randomly select one of the 3 AZs, and then terminate an instance in that AZ


2: Terminate the instance with the least active network connections. If multiple instances meet this criterion, one will

be randomly selected


3: Send an SNS notification, if configured to do so


4 : Wait for the cooldown period and then terminate the instance that has been running the longest


5: Terminate an instance in the AZ which currently has 2 running EC2 instances


**Answer: 3,5**


**Explanation:**


Auto Scaling can perform rebalancing when it finds that the number of instances across AZs is not balanced. Auto Scaling

rebalances by launching new EC2 instances in the AZs that have fewer instances first, only then will it start

terminating instances in AZs that had more instances


Auto Scaling can be configured to send an SNS email when:


- An instance is launched.

- An instance is terminated.

- An instance fails to launch.

- An instance fails to terminate.


- CORRECT "Send an SNS notification, if configured to do so" is a correct answer.


- CORRECT "Terminate an instance in the AZ which currently has 2 running EC2 instances" is also a correct answer.


- INCORRECT "Terminate the instance with the least active network connections. If multiple instances meet this

  criterion, one will be randomly selected" is incorrect. Auto Scaling will only terminate an instance randomly after it

  has first gone through several other selection steps. Please see the AWS article below for detailed information on the

  process


- INCORRECT "Wait for the cooldown period and then terminate the instance that has been running the longest" is

  incorrect. Auto Scaling does not terminate the instance that has been running the longest.


- INCORRECT "Terminate an instance in the AZ which currently has 2 running EC2 instances" is incorrect as it will launch

  instances in that AZ before terminating.


**References:**


https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-instance-termination.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/aws-auto-

scaling/

