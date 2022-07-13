*

**Explanation:**

When data is stored in an encrypted state it is referred to as encrypted “at rest” and when it is encrypted as it is

being transferred over a network it is referred to as encrypted “in transit”. You can securely upload/download your data

to Amazon S3 via SSL endpoints using the HTTPS protocol (In Transit – SSL/TLS).

You have the option of encrypting the data locally before it is uploaded or uploading using SSL/TLS so it is secure in

transit and encrypting on the Amazon S3 side using S3 managed keys. The S3 managed keys will be AES-256 (not AES-128)

bit keys

Uploading data using CloudFront with an EC2 origin or using an encrypted EBS volume attached to an EC2 instance is not a

solution to this problem as your company wants to backup these records onto S3 (not EC2/EBS).

* ✅ :  "Before uploading the data to S3 over HTTPS, encrypt the data locally using your own encryption keys" is a

  correct answer.

* ✅ :  "Enable Server Side Encryption with S3 managed keys on an S3 bucket using AES-256" is also a correct answer.

* ❌ :  "Enable Server Side Encryption with S3 managed keys on an S3 bucket using AES-128" is incorrect as AES 256

  should be used.

* ❌ :  "Attach an encrypted EBS volume to an EC2 instance" is incorrect as explained above.

* ❌ :  "Upload the data using CloudFront with an EC2 origin" is incorrect as explained above.

**References:**

<https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingEncryption.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/>

----
* #<https://docs.aws.amazon.com/amazons3/latest/dev/usingencryption.html> #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/> #s3_bucket #amazon_s3 #amazon_s3_side
