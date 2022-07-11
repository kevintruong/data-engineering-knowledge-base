*

**Explanation:**

To manage your objects so that they are stored cost effectively throughout their lifecycle, configure their Amazon S3

Lifecycle. An S3 Lifecycle configuration is a set of rules that define actions that Amazon S3 applies to a group of

objects. There are two types of actions:

* Transition actions—Define when objects transition to another storage class. For example, you might choose to

  transition objects to the S3 Standard-IA storage class 30 days after you created them, or archive objects to the S3

  Glacier storage class one year after creating them.

* Expiration actions—Define when objects expire. Amazon S3 deletes expired objects on your behalf.

* ✅ :  "Use an S3 lifecycle policy with object expiration configured to automatically remove objects that are more

  than 60 days old" is the correct answer.

* ❌ :  "Write a Ruby script that checks the age of objects and deletes any that are more than 60 days old" is

  incorrect as the automated method is to use object expiration.

* ❌ :  "Use an S3 bucket policy that deletes objects that are more than 60 days old" is incorrect as you cannot do

  this with bucket policies.

* ❌ :  "Use an S3 lifecycle policy to move the log files that are more than 60 days old to the GLACIER storage

  class" is incorrect. Moving logs to Glacier may save cost but the question requests that the files are permanently

  deleted.

**References:**

<https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/>

----
* #<https://docs.aws.amazon.com/amazons3/latest/dev/object-lifecycle-mgmt.html> #s3_lifecycle_policy #s3_lifecycle_configuration #s3_bucket_policy #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/>
