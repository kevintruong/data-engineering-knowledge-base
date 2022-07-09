#### Question  39


**A Solutions Architect works for a systems integrator running a platform that stores medical records. The government

security policy mandates that patient data that contains personally identifiable information

(PII) must be encrypted at all times, both at rest and in transit. Amazon S3 is used to back up data into the AWS

cloud.**


**How can the Solutions Architect ensure the medical records are properly secured? (Select TWO)**


1: Before uploading the data to S3 over HTTPS, encrypt the data locally using your own encryption keys


2: Enable Server Side Encryption with S3 managed keys on an S3 bucket using AES- 128


3: Attach an encrypted EBS volume to an EC2 instance


4: Enable Server Side Encryption with S3 managed keys on an S3 bucket using AES- 256


5: Upload the data using CloudFront with an EC2 origin


**Answer: 1,4**


**Explanation:**


When data is stored in an encrypted state it is referred to as encrypted “at rest” and when it is encrypted as it is

being transferred over a network it is referred to as encrypted “in transit”. You can securely upload/download your data

to Amazon S3 via SSL endpoints using the HTTPS protocol (In Transit – SSL/TLS).


You have the option of encrypting the data locally before it is uploaded or uploading using SSL/TLS so it is secure in

transit and encrypting on the Amazon S3 side using S3 managed keys. The S3 managed keys will be AES-256 (not AES-128)

bit keys


Uploading data using CloudFront with an EC2 origin or using an encrypted EBS volume attached to an EC2 instance is not a

solution to this problem as your company wants to backup these records onto S3 (not EC2/EBS).


- CORRECT "Before uploading the data to S3 over HTTPS, encrypt the data locally using your own encryption keys" is a

  correct answer.


- CORRECT "Enable Server Side Encryption with S3 managed keys on an S3 bucket using AES-256" is also a correct answer.


- INCORRECT "Enable Server Side Encryption with S3 managed keys on an S3 bucket using AES-128" is incorrect as AES 256

  should be used.


- INCORRECT "Attach an encrypted EBS volume to an EC2 instance" is incorrect as explained above.


- INCORRECT "Upload the data using CloudFront with an EC2 origin" is incorrect as explained above.


**References:**


https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingEncryption.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/

