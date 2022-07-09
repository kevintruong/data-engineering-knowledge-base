#### Question  30


**A Solutions Architect would like to implement a method of automating the creation, retention, and deletion of backups

for the Amazon EBS volumes in an Amazon VPC. What is the easiest way to automate these tasks using AWS tools?**


1: Configure EBS volume replication to create a backup on Amazon S3


2: Use the EBS Data Lifecycle Manager (DLM) to manage snapshots of the volumes


3: Create a scheduled job and run the AWS CLI command “create-backup” to take backups of the EBS volumes


4: Create a scheduled job and run the AWS CLI command “create-snapshot” to take backups of the EBS volumes


**Answer: 2**


**Explanation:**


You backup EBS volumes by taking snapshots. This can be automated via the AWS CLI command “create- snapshot”. However

the question is asking for a way to automate not just the creation of the snapshot but the retention and deletion too.


The EBS Data Lifecycle Manager (DLM) can automate all of these actions for you and this can be performed centrally from

within the management console.


- CORRECT "Use the EBS Data Lifecycle Manager (DLM) to manage snapshots of the volumes" is the correct answer.


- INCORRECT "Configure EBS volume replication to create a backup on S3" is incorrect. You cannot configure volume

  replication for EBS volumes using AWS tools.


- INCORRECT "Create a scheduled job and run the AWS CLI command “create-backup” to take backups of the EBS volumes"

  is incorrect. This is the wrong command (use create-snapshot) and is not the easiest method.


- INCORRECT "Create a scheduled job and run the AWS CLI command “create-snapshot” to take backups of the EBS volumes"

  is incorrect. This is not the easiest method, DLM would be a much better solution.


**References:**


https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/snapshot-lifecycle.html


https://docs.aws.amazon.com/cli/latest/reference/ec2/create-snapshot.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ebs/

