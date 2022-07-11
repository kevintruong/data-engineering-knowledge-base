**Explanation:**

You can copy an Amazon Machine Image (AMI) within or across AWS Regions using the AWS Management Console, the AWS

Command Line Interface or SDKs, or the Amazon EC2 API, all of which support the CopyImage action.

Using the copied AMI the solutions architect would then be able to launch an instance from the same EBS volume in the

second Region.

**Note:** the AMIs are stored on Amazon S3, however you cannot view them in the S3 management console or work with them

programmatically using the S3 API.

- ✅ :  "Copy an Amazon Machine Image (AMI) of an EC2 instance and specify the second Region for the destination"

  is a correct answer.

- ✅ :  "Launch a new EC2 instance from an Amazon Machine Image (AMI) in the second Region" is also a correct answer.

- ❌ :  "Detach a volume on an EC2 instance and copy it to an Amazon S3 bucket in the second Region" is incorrect.

  You cannot copy EBS volumes directly from EBS to Amazon S3.

- ❌ :  "Launch a new EC2 instance in the second Region and copy a volume from Amazon S3 to the new instance" is

  incorrect. You cannot create an EBS volume directly from Amazon S3.

- ❌ :  "Copy an Amazon Elastic Block Store (Amazon EBS) volume from Amazon S3 and launch an EC2 instance in the

  second Region using that EBS volume" is incorrect. You cannot create an EBS volume directly from Amazon S3.

**References:**

<https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/CopyingAMIs.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ebs/>

----

- #aws_regions #ec2_instance #new_ec2_instance #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ebs/> #ebs_volumes
