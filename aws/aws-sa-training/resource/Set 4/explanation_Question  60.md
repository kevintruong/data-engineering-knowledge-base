*

**Explanation:**

Snapshots capture a point-in-time state of an instance. Snapshots of Amazon EBS volumes are stored on S3 by design so

you only need to take a snapshot and it will automatically be stored on Amazon S3.

* ✅ :  "Create a snapshot of the volume" is the correct answer.

* ❌ :  "Use SWF to automatically create a backup of your EBS volumes and then upload them to an S3 bucket" is

  incorrect. This is not a good use case for Amazon SWF.

* ❌ :  "You don’t need to do anything, EBS volumes are automatically backed up by default" is incorrect. Amazon EBS

  volumes are not automatically backed up using snapshots. You need to manually take a snapshot or you can use Amazon

  Data Lifecycle Manager (Amazon DLM) to automate the creation, retention, and deletion of snapshots.

* ❌ :  "Write a custom script to automatically copy your data to an S3 bucket" is incorrect as this is not the

  simplest solution available.

**References:**

<https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSSnapshots.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ebs/>

----
* #amazon_ebs_volumes #s3_bucket #ebs_volumes #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ebs/> #amazon_s3
