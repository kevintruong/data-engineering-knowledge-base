**Explanation:**

SSE-KMS requires that AWS manage the data key but you manage the customer master key (CMK) in AWS KMS. You can choose a

customer managed CMK or the AWS managed CMK for Amazon S3 in your account.

_Customer managed CMKs_ are CMKs in your AWS account that you create, own, and manage. You have full control over these

CMKs, including establishing and maintaining their key policies, IAM policies, and grants, enabling and disabling them,

rotating their cryptographic material, adding tags, creating aliases that refer to the CMK, and scheduling the CMKs for

deletion.

For this scenario, the solutions architect should use SSE-KMS with a customer managed CMK. That way KMS will manage the

data key but the company can configure key policies defining who can access the keys.

- ✅ :  "Server-Side Encryption with AWS KMS-Managed Keys (SSE-KMS)" is the correct answer.

- ❌ :  "Server-Side Encryption with keys stored in an S3 bucket" is incorrect as you cannot store your keys in a

  bucket with server-side encryption

- ❌ :  "Server-Side Encryption with Customer-Provided Keys (SSE-C)" is incorrect as the company does not want to

  manage the keys.

- ❌ :  "Server-Side Encryption with Amazon S3-Managed Keys (SSE-S3)" is incorrect as the company needs to manage

  access control for the keys which is not possible when they’re managed by Amazon.

**References:**

<https://docs.aws.amazon.com/kms/latest/developerguide/services-s3.html#sse>

<https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/>

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/security-identity>-

compliance/aws-kms/

----

- #aws_kms #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/> #aws_account #aws #s3_bucket
