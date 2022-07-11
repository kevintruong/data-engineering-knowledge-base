**Explanation:**

When using S3 encryption your data is always encrypted at rest and you can choose to use KMS managed keys or

customer-provided keys. If you encrypt the data at the source and transfer it in an encrypted state it will also be

encrypted in-transit.

With client side encryption data is encrypted on the client side and transferred in an encrypted state and with

server-side encryption data is encrypted by S3 before it is written to disk (data is decrypted when it is downloaded).

- ✅ :  "Use AWS S3 server-side encryption with Key Management Service keys or Customer-provided keys" is the correct

  answer.

- ✅ :  "Encrypt the data at the source using the client's CMK keys before transferring it to S3" is the correct

  answer.

- ❌ :  "Make use of AWS S3 bucket policies to control access to the data at rest" is incorrect. You can use bucket

  policies to control encryption of data that is uploaded but use of encryption is not stated in the answer given.

  Simply using bucket policies to control access to the data does not meet the security mandate that data must be

  encrypted.

- ❌ :  "Use CloudHSM" is incorrect. CloudHSM can be used to encrypt data but as a dedicated service it is charged

  on an hourly basis and is less cost-efficient compared to S3 encryption or encrypting the data at the source.

- ❌ :  "Use Multipart upload with SSL" is incorrect. Multipart upload helps with uploading large files but does not

  encrypt your data.

**References:**

<https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingEncryption.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/>

----

- #s3_encryption #aws_s3_bucket_policies #<https://docs.aws.amazon.com/amazons3/latest/dev/usingencryption.html> #aws_s3_server #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/>
