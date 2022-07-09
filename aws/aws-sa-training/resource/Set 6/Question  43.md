#### Question  43


**A company runs a web-based application that uses Amazon EC2 instances for the web front-end and Amazon RDS for the

database back-end. The web application writes transaction log files to an Amazon S3**


**bucket and the quantity of files is becoming quite large. It is acceptable to retain the most recent 60 days of log

files and permanently delete the rest.**


**Which action can a Solutions Architect take to enable this to happen automatically?**


1: Use an S3 lifecycle policy with object expiration configured to automatically remove objects that are more than 60

days old


2: Write a Ruby script that checks the age of objects and deletes any that are more than 60 days old


3: Use an S3 bucket policy that deletes objects that are more than 60 days old


4: Use an S3 lifecycle policy to move the log files that are more than 60 days old to the GLACIER storage class


**Answer: 1**


**Explanation:**


To manage your objects so that they are stored cost effectively throughout their lifecycle, configure their Amazon S3

Lifecycle. An S3 Lifecycle configuration is a set of rules that define actions that Amazon S3 applies to a group of

objects. There are two types of actions:


- Transition actions—Define when objects transition to another storage class. For example, you might choose to

  transition objects to the S3 Standard-IA storage class 30 days after you created them, or archive objects to the S3

  Glacier storage class one year after creating them.

- Expiration actions—Define when objects expire. Amazon S3 deletes expired objects on your behalf.


- CORRECT "Use an S3 lifecycle policy with object expiration configured to automatically remove objects that are more

  than 60 days old" is the correct answer.


- INCORRECT "Write a Ruby script that checks the age of objects and deletes any that are more than 60 days old" is

  incorrect as the automated method is to use object expiration.


- INCORRECT "Use an S3 bucket policy that deletes objects that are more than 60 days old" is incorrect as you cannot do

  this with bucket policies.


- INCORRECT "Use an S3 lifecycle policy to move the log files that are more than 60 days old to the GLACIER storage

  class" is incorrect. Moving logs to Glacier may save cost but the question requests that the files are permanently

  deleted.


**References:**


https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/

