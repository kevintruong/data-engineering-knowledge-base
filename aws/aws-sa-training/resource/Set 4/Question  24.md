#### Question  24


**A Solutions Architect attempted to restart a stopped EC2 instance and it immediately changed from a pending state to a

terminated state. What are the most likely explanations? (Select TWO)**


1: You've reached your EBS volume limit


2: An EBS snapshot is corrupt


3: AWS does not currently have enough available On-Demand capacity to service your request


4: You have reached the limit on the number of instances that you can launch in a region


5: The AMI is unsupported


**Answer: 1,2**


**Explanation:**


The following are a few reasons why an instance might immediately terminate:


- You’ve reached your EBS volume limit.

- An EBS snapshot is corrupt.

- The root EBS volume is encrypted and you do not have permissions to access the KMS key for decryption.

- The instance store-backed AMI that you used to launch the instance is missing a required part (an image.part.xx file).


- CORRECT "You've reached your EBS volume limit" is a correct answer.


- CORRECT "An EBS snapshot is corrupt" is also a correct answer.


- INCORRECT "AWS does not currently have enough available On-Demand capacity to service your request" is incorrect. If

  AWS does not have capacity available a InsufficientInstanceCapacity error will be generated when you try to launch a

  new instance or restart a stopped instance.


- INCORRECT "You have reached the limit on the number of instances that you can launch in a region" is incorrect. If

  you’ve reached the limit on the number of instances you can launch in a region you get an InstanceLimitExceeded error

  when you try to launch a new instance or restart a stopped instance.


- INCORRECT "The AMI is unsupported" is incorrect. It is possible that an instance type is not supported by an AMI and

  this can cause an “UnsupportedOperation” client error. However, in this case the instance was previously running (it

  is in a stopped state) so it is unlikely that this is the issue.


**References:**


https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/troubleshooting-launch.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ec2/

