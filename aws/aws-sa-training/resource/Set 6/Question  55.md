#### Question  55


**A Solutions Architect is launching an Amazon EC2 instance with multiple attached volumes by modifying the block device

mapping. Which block device can be specified in a block device mapping to be used with an EC2 instance? (Select TWO)**


1: EBS volume


2: EFS volume


3: Instance store volume


4: Snapshot


5: S3 bucket


**Answer: 1,3**


**Explanation:**


Each instance that you launch has an associated root device volume, either an Amazon EBS volume or an instance store

volume.


You can use block device mapping to specify additional EBS volumes or instance store volumes to attach to an instance

when it’s launched. You can also attach additional EBS volumes to a running instance.


You cannot use a block device mapping to specify a snapshot, EFS volume or S3 bucket.


- CORRECT "EBS volume" is a correct answer.


- CORRECT "Instance store volume" is also a correct answer.


- INCORRECT "EFS volume" is incorrect as described above.


- INCORRECT "Snapshot" is incorrect as described above.


- INCORRECT "S3 bucket" is incorrect as described above.


**References:**


https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-device-mapping-concepts.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ebs/

