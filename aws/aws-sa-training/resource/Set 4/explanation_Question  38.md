*

**Explanation:**

Athena allows you to easily query encrypted data stored in Amazon S3 and write encrypted results back to your S3 bucket.

Both, server-side encryption and client-side encryption are supported.

AWS IAM policies can be used to grant IAM users with fine-grained control to Amazon S3 buckets.

* ✅ :  "Use IAM policies to restrict access to the bucket" is a correct answer.

* ✅ :  "Use Athena for querying the data and writing the results back to the bucket" is also a correct answer.

* ❌ :  "Use AWS Glue to extract the data, analyze it, and load it back to the S3 bucket" is incorrect. AWS Glue is

  an ETL service and is not used for querying and analyzing data in S3.

* ❌ :  "Use bucket ACLs to restrict access to the bucket" is incorrect. With IAM policies, you can grant IAM users

  fine-grained control to your S3 buckets and is preferable to using bucket ACLs.

* ❌ :  "Use the AWS KMS API to query the encrypted data, and the S3 API for writing the results" is incorrect. The

  AWS KMS API can be used for encryption purposes; however it cannot perform analytics so is not suitable.

**References:**

<https://aws.amazon.com/athena/>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/security-identity>-

compliance/aws-iam/

----
* #s3_api #aws_kms_api #aws_iam_policies #amazon_s3_buckets #s3_bucket
