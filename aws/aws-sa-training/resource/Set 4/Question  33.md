#### Question  33


**A Solutions Architect has been assigned the task of moving some sensitive documents into the AWS cloud. The security

of the documents must be maintained.**


**Which AWS features can help ensure that the sensitive documents cannot be read even if they are compromised? (Select

TWO)**


1: AWS IAM Access Policy


2: Amazon S3 Server-Side Encryption


3: Amazon EBS snapshots


4: Amazon S3 cross region replication


5: Amazon EBS encryption with Customer Managed Keys


**Answer: 2,5**


**Explanation:**


It is not specified what types of documents are being moved into the cloud or what services they will be placed on.

Therefore we can assume that options include S3 and EBS. To prevent the documents from being read if they are

compromised we need to encrypt them.


Both of these services provide native encryption functionality to ensure security of the sensitive documents. With EBS

you can use KMS-managed or customer-managed encryption keys. With S3 you can use client-side or server-side encryption.


- CORRECT "Amazon S3 Server-Side Encryption" is a correct answer.


- CORRECT "Amazon EBS encryption with Customer Managed Keys" is also a correct answer.


- INCORRECT "AWS IAM Access Policy" is incorrect. IAM access policies can be used to control access but if the documents

  are somehow compromised they will not stop the documents from being read. For this we need encryption, and IAM access

  policies are not used for controlling encryption.


- INCORRECT "Amazon EBS snapshots" is incorrect. EBS snapshots are used for creating a point-in-time backup or data.

  They do maintain the encryption status of the data from the EBS volume but are not used for actually encrypting the

  data in the first place.


- INCORRECT "Amazon S3 cross region replication" is incorrect. S3 cross-region replication can be used for fault

  tolerance but does not apply any additional security to the data.


**References:**


https://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-encryption.html


https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ebs/


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/

