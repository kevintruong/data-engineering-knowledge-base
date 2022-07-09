#### Question  60


**A Solutions Architect would like to store a backup of an Amazon EBS volume on Amazon S3. What is the easiest way of

achieving this?**


1: Use SWF to automatically create a backup of your EBS volumes and then upload them to an S3 bucket


2: You don’t need to do anything, EBS volumes are automatically backed up by default


3: Write a custom script to automatically copy your data to an S3 bucket


4: Create a snapshot of the volume


**Answer: 4**


**Explanation:**


Snapshots capture a point-in-time state of an instance. Snapshots of Amazon EBS volumes are stored on S3 by design so

you only need to take a snapshot and it will automatically be stored on Amazon S3.


- CORRECT "Create a snapshot of the volume" is the correct answer.


- INCORRECT "Use SWF to automatically create a backup of your EBS volumes and then upload them to an S3 bucket" is

  incorrect. This is not a good use case for Amazon SWF.


- INCORRECT "You don’t need to do anything, EBS volumes are automatically backed up by default" is incorrect. Amazon EBS

  volumes are not automatically backed up using snapshots. You need to manually take a snapshot or you can use Amazon

  Data Lifecycle Manager (Amazon DLM) to automate the creation, retention, and deletion of snapshots.


- INCORRECT "Write a custom script to automatically copy your data to an S3 bucket" is incorrect as this is not the

  simplest solution available.


**References:**


https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSSnapshots.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ebs/

