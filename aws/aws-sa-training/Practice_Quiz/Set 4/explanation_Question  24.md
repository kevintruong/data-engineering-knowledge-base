*

**Explanation:**

The following are a few reasons why an instance might immediately terminate:

* You’ve reached your EBS volume limit.

* An EBS snapshot is corrupt.

* The root EBS volume is encrypted and you do not have permissions to access the KMS key for decryption.

* The instance store-backed AMI that you used to launch the instance is missing a required part (an image.part.xx file).

* ✅ :  "You've reached your EBS volume limit" is a correct answer.

* ✅ :  "An EBS snapshot is corrupt" is also a correct answer.

* ❌ :  "AWS does not currently have enough available On-Demand capacity to service your request" is incorrect. If

  AWS does not have capacity available a InsufficientInstanceCapacity error will be generated when you try to launch a

  new instance or restart a stopped instance.

* ❌ :  "You have reached the limit on the number of instances that you can launch in a region" is incorrect. If

  you’ve reached the limit on the number of instances you can launch in a region you get an InstanceLimitExceeded error

  when you try to launch a new instance or restart a stopped instance.

* ❌ :  "The AMI is unsupported" is incorrect. It is possible that an instance type is not supported by an AMI and

  this can cause an “UnsupportedOperation” client error. However, in this case the instance was previously running (it

  is in a stopped state) so it is unlikely that this is the issue.

**References:**

<https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/troubleshooting-launch.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ec2/>

----
* #ebs_snapshot #aws #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ec2/> #ami #ebs_volume_limit
