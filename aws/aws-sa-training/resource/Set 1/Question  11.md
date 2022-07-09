#### Question  11


**A company's application is running on Amazon EC2 instances in a single Region. In the event of a disaster, a solutions

architect needs to ensure that the resources can also be deployed to a second Region.**


**Which combination of actions should the solutions architect take to accomplish this? (Select TWO)**


1: Detach a volume on an EC2 instance and copy it to an Amazon S3 bucket in the second Region


2: Launch a new EC2 instance from an Amazon Machine Image (AMI) in the second Region


3: Launch a new EC2 instance in the second Region and copy a volume from Amazon S3 to the new instance


4: Copy an Amazon Machine Image (AMI) of an EC2 instance and specify the second Region for the destination


5: Copy an Amazon Elastic Block Store (Amazon EBS) volume from Amazon S3 and launch an EC2 instance in the second Region

using that EBS volume


Answer: 2, 4


**Explanation:**


You can copy an Amazon Machine Image (AMI) within or across AWS Regions using the AWS Management Console, the AWS

Command Line Interface or SDKs, or the Amazon EC2 API, all of which support the CopyImage action.


Using the copied AMI the solutions architect would then be able to launch an instance from the same EBS volume in the

second Region.


**Note:** the AMIs are stored on Amazon S3, however you cannot view them in the S3 management console or work with them

programmatically using the S3 API.


- CORRECT "Copy an Amazon Machine Image (AMI) of an EC2 instance and specify the second Region for the destination"

  is a correct answer.


- CORRECT "Launch a new EC2 instance from an Amazon Machine Image (AMI) in the second Region" is also a correct answer.


- INCORRECT "Detach a volume on an EC2 instance and copy it to an Amazon S3 bucket in the second Region" is incorrect.

  You cannot copy EBS volumes directly from EBS to Amazon S3.


- INCORRECT "Launch a new EC2 instance in the second Region and copy a volume from Amazon S3 to the new instance" is

  incorrect. You cannot create an EBS volume directly from Amazon S3.


- INCORRECT "Copy an Amazon Elastic Block Store (Amazon EBS) volume from Amazon S3 and launch an EC2 instance in the

  second Region using that EBS volume" is incorrect. You cannot create an EBS volume directly from Amazon S3.


**References:**


https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/CopyingAMIs.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ebs/

