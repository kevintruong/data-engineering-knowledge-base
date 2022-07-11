**Explanation:**

There are several security best practices for securing the root user account:

- Lock away root user access keys OR delete them if possible

- Use a strong password

- Enable multi-factor authentication (MFA)

The root user automatically has full privileges to the account and these privileges cannot be restricted so it is

extremely important to follow best practice advice about securing the root user account.

- ✅ :  "Ensure the root user uses a strong password" is the correct answer.

- ✅ :  "Enable multi-factor authentication to the root user" is the correct answer.

- ❌ :  "Store root user access keys in an encrypted Amazon S3 bucket" is incorrect as the best practice is to lock

  away or delete the root user access keys. An S3 bucket is not a suitable location for storing them, even if encrypted.

- ❌ :  "Add the root user to a group containing administrative permissions" is incorrect as this does not restrict

  access and is unnecessary.

- ❌ :  "Delete the root user account" is incorrect as you cannot delete the root user account.

**References:**

<https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/security-identity>-

compliance/aws-iam/

----

- #<https://docs.aws.amazon.com/iam/latest/userguide/best-practices.html> #root_user_access_keys_or #store_root_user_access_keys #root_user_access_keys #amazon_s3_bucket
