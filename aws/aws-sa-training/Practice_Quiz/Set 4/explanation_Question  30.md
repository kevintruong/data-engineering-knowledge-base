*

**Explanation:**

You backup EBS volumes by taking snapshots. This can be automated via the AWS CLI command “create- snapshot”. However

the question is asking for a way to automate not just the creation of the snapshot but the retention and deletion too.

The EBS Data Lifecycle Manager (DLM) can automate all of these actions for you and this can be performed centrally from

within the management console.

* ✅ :  "Use the EBS Data Lifecycle Manager (DLM) to manage snapshots of the volumes" is the correct answer.

* ❌ :  "Configure EBS volume replication to create a backup on S3" is incorrect. You cannot configure volume

  replication for EBS volumes using AWS tools.

* ❌ :  "Create a scheduled job and run the AWS CLI command “create-backup” to take backups of the EBS volumes"

  is incorrect. This is the wrong command (use create-snapshot) and is not the easiest method.

* ❌ :  "Create a scheduled job and run the AWS CLI command “create-snapshot” to take backups of the EBS volumes"

  is incorrect. This is not the easiest method, DLM would be a much better solution.

**References:**

<https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/snapshot-lifecycle.html>

<https://docs.aws.amazon.com/cli/latest/reference/ec2/create-snapshot.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ebs/>

----
* #configure_ebs_volume_replication #<https://docs.aws.amazon.com/cli/latest/reference/ec2/create-snapshot.html> #ebs_data_lifecycle_manager #aws_tools #ebs_volumes
