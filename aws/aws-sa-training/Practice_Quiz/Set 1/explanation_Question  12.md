**Explanation:**

None of the options present a good solution for specifying permissions required to write and modify objects so that

requirement needs to be taken care of separately. The other requirements are to prevent accidental deletion and the

ensure that all versions of the document are available.

The two solutions for these requirements are versioning and MFA delete. Versioning will retain a copy of each version of

the document and multi-factor authentication delete (MFA delete) will prevent any accidental deletion as you need to

supply a second factor when attempting a delete.

- ✅ :  "Enable versioning on the bucket" is a correct answer.

- ✅ :  "Enable MFA Delete on the bucket" is also a correct answer.

- ❌ :  "Set read-only permissions on the bucket" is incorrect as this will also prevent any writing to the bucket

  which is not desired.

- ❌ :  "Attach an IAM policy to the bucket" is incorrect as users need to modify documents which will also allow

  delete. Therefore, a method must be implemented to just control deletes.

- ❌ :  "Encrypt the bucket using AWS SSE-S3" is incorrect as encryption doesn’t stop you from deleting an object.

**References:**

<https://docs.aws.amazon.com/AmazonS3/latest/dev/Versioning.html>

<https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMFADelete.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/>

----

- #multi_-_factor_authentication_delete #mfa_delete #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/> #<https://docs.aws.amazon.com/amazons3/latest/dev/versioning.html> #aws_sse
