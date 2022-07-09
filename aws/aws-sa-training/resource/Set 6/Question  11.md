#### Question  11


**The Solutions Architect in charge of a critical application must ensure the Amazon EC2 instances are able to be

launched in another AWS Region in the event of a disaster.**


**What steps should the Solutions Architect take? (Select TWO)**


1: Launch instances in the second Region using the S3 API


2: Create AMIs of the instances and copy them to another Region


3: Enable cross-region snapshots for the Amazon EC2 instances


4: Launch instances in the second Region from the AMIs


5: Copy the snapshots using Amazon S3 cross-region replication


Answer: 2,4


**Explanation:**


You can create AMIs of the EC2 instances and then copy them across Regions. This provides a point-in-time copy of the

state of the EC2 instance in the remote Region.


Once you’ve created AMIs of EC2 instances and copied them to the second Region, you can then launch the EC2 instances

from the AMIs in that Region.


This is a good DR strategy as you have moved stateful EC2 instances to another Region.


- CORRECT "Create AMIs of the instances and copy them to another Region" is the correct answer.


- CORRECT "Launch instances in the second Region from the AMIs" is also a correct answer.


- INCORRECT "Launch instances in the second Region using the S3 API" is incorrect. Though snapshots (and EBS- backed

  AMIs) are stored on Amazon S3, you cannot actually access them using the S3 API. You must use the EC2 API.


- INCORRECT "Enable cross-region snapshots for the Amazon EC2 instances" is incorrect. You cannot enable “cross-region

  snapshots” as this is not a feature that currently exists.


- INCORRECT "Copy the snapshots using Amazon S3 cross-region replication" is incorrect. You cannot work with snapshots

  using Amazon S3 at all including leveraging the cross-region replication feature.


**References:**


https://aws.amazon.com/blogs/aws/ebs-snapshot-copy/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ec2/

