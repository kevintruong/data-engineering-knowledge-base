#### Question  49


**A Solutions Architect must design a solution that encrypts data in Amazon S3. Corporate policy mandates encryption

keys be generated and managed on premises. Which solution should the Architect use to meet the security requirements?**


1: SSE-C: Server-side encryption with customer-provided encryption keys


2: SSE-S3: Server-side encryption with Amazon-managed master key


3: SSE-KMS: Server-side encryption with AWS KMS managed keys


4: AWS CloudHSM


Answer: 1


**Explanation:**


Server-side encryption is about protecting data at rest. Server-side encryption encrypts only the object data, not

object metadata. Using server-side encryption with customer-provided encryption keys (SSE-C) allows you to set your own

encryption keys. With the encryption key you provide as part of your request, Amazon S3 manages the encryption as it

writes to disks and decryption when you access your objects. Therefore, you


don't need to maintain any code to perform data encryption and decryption. The only thing you do is manage the

encryption keys you provide.


When you upload an object, Amazon S3 uses the encryption key you provide to apply AES-256 encryption to your data and

removes the encryption key from memory. When you retrieve an object, you must provide the same encryption key as part of

your request. Amazon S3 first verifies that the encryption key you provided matches and then decrypts the object before

returning the object data to you.


- CORRECT "SSE-C: Server-side encryption with customer-provided encryption keys" is the correct answer.


- INCORRECT "SSE-S3: Server-side encryption with Amazon-managed master key" is incorrect. With SSE-S3, Amazon manage the

  keys for you, so this is incorrect.


- INCORRECT "SSE-KMS: Server-side encryption with AWS KMS managed keys" is incorrect. With SSE-KMS the keys are managed

  in the Amazon Key Management Service, so this is incorrect.


- INCORRECT "AWS CloudHSM" is incorrect. With AWS CloudHSM your keys are held in AWS in a hardware security module.

  Again, the keys are not on-premises they are in AWS, so this is incorrect.


**References:**


https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/

