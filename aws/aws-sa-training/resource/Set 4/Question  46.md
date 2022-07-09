#### Question  46


**There is a problem with an EC2 instance that was launched by Amazon EC2 Auto Scaling. The EC2 status checks have

reported that the instance is “Impaired”. What action will EC2 Auto Scaling take?**


1: Auto Scaling will perform Availability Zone rebalancing


2: It will wait a few minutes for the instance to recover and if it does not it will mark the instance for termination,

terminate it, and then launch a replacement


3: Auto Scaling performs its own status checks and does not integrate with EC2 status checks


4: It will launch a new instance immediately and then mark the impaired one for replacement


**Answer: 2**


**Explanation:**


If any health check returns an unhealthy status the instance will be terminated. For the “impaired” status, the ASG will

wait a few minutes to see if the instance recovers before taking action. If the “impaired” status persists, termination

occurs. Unlike AZ rebalancing, termination of unhealthy instances happens first, then Auto Scaling attempts to launch

new instances to replace terminated instances.


- CORRECT "It will wait a few minutes for the instance to recover and if it does not it will mark the instance for

  termination, terminate it, and then launch a replacement" is the correct answer.


- INCORRECT "Auto Scaling will perform Availability Zone rebalancing" is incorrect. Auto Scaling will not perform

  Availability Zone rebalancing due to an impaired status check.


- INCORRECT "Auto Scaling performs its own status checks and does not integrate with EC2 status checks" is incorrect.

  Auto Scaling does integrate with EC2 status checks as well as having its own status checks.


- INCORRECT "It will launch a new instance immediately and then mark the impaired one for replacement" is incorrect.

  Auto Scaling will not launch a new instance immediately as it always terminates unhealthy instance before launching a

  replacement.


**References:**


https://aws.amazon.com/premiumsupport/knowledge-center/auto-scaling-terminate-instance/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/aws-auto-

scaling/

