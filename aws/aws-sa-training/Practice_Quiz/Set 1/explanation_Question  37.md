**Explanation:**

To manage your objects so that they are stored cost effectively throughout their lifecycle, configure their _Amazon S3

Lifecycle_. An_S3 Lifecycle configuration_ is a set of rules that define actions that Amazon S3 applies to a group of

objects. There are two types of actions:

- **Transition actions** —Define when objects transition to another storage class. For example, you might choose to

  transition objects to the S3 Standard-IA storage class 30 days after you created them, or archive objects to the S3

  Glacier storage class one year after creating them.

There are costs associated with the lifecycle transition requests.

- **Expiration actions** —Define when objects expire. Amazon S3 deletes expired objects on your behalf.

The lifecycle expiration costs depend on when you choose to expire objects.

The solutions architect can create a lifecycle action using the “expiration action element” which expires objects (

deletes them) at the specified time.

- ✅ :  "Store the files on Amazon S3, and create a lifecycle policy to remove the files after three months"

  is the correct answer.

- ❌ :  "Store the files on Amazon EBS, and create a lifecycle policy to remove the files after three months" is

  incorrect. There is no lifecycle policy available for deleting files on EBS. The Amazon Data Lifecycle Manager (DLM)

  feature automates the creation, retention, and deletion of EBS snapshots but not the individual files within an EBS

  volume.

- ❌ :  "Store the files on Amazon Glacier, and create a lifecycle policy to remove the files after three months"

  is incorrect. S3 lifecycle actions apply to any storage class, including Glacier, however Glacier would not allow

  immediate download.

- ❌ :  "Store the files on Amazon EFS, and create a lifecycle policy to remove the files after three months" is

  incorrect. There is no lifecycle policy available for deleting files on EFS

**References:**

<https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/>

----

- #amazon_data_lifecycle_manager #s3_lifecycle_actions #<https://docs.aws.amazon.com/amazons3/latest/dev/object-lifecycle-mgmt.html> #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/> #**s3_lifecycle_configuration**
