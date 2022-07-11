*

**Explanation:**

The AWS blog URL below explains how to construct an IAM policy for a similar scenario. Please refer to the article for

detailed instructions.

* ✅ :  "Create an IAM policy that applies folder-level permissions" is a correct answer.

* ✅ :  "Create an IAM group and attach the IAM policy, add IAM users to the group" is also a correct answer.

* ❌ :  "Create a bucket policy that applies access permissions based on username" is incorrect. An IAM policy

  rather than a bucket policy should be used.

* ❌ :  "Create an IAM policy that applies object-level S3 ACLs" is incorrect as this cannot be done through an IAM

  policy.

* ❌ :  "Attach an S3 ACL sub-resource that grants access based on the %username% variable" is incorrect as an IAM

  policy should be used to control access.

**References:**

<https://aws.amazon.com/blogs/security/writing-iam-policies-grant-access-to-user-specific-folders-in-an>-

amazon-s3-bucket/

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/security-identity>-

compliance/aws-iam/

----
* #<https://aws.amazon.com/blogs/security/writing-iam-policies-grant-access-to-user-specific-folders-in-an>>- #s3_acl_sub_-_resource #level_s3_acls #bucket_policy #iam_policy
