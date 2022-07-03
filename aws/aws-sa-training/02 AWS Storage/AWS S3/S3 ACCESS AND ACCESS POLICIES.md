---
date created: 2022-07-03 10:56
---

### **S3 ACCESS AND ACCESS POLICIES**

**There are four mechanisms for controlling access to Amazon S3 resources:**

- IAM policies.
- Bucket policies.
- Access Control Lists (ACLs).
- Query string authentication (URL to an Amazon S3 object which is only valid for a limited time).

Access auditing can be configured by configuring an Amazon S3 bucket to create access log records for all requests made against it.

For capturing IAM/user identity information in logs configure AWS CloudTrail Data Events.

By default, a bucket, its objects, and related sub-resources are all private.

By default, only a resource owner can access a bucket.

The resource owner refers to the AWS account that creates the resource.

With IAM the account owner rather than the IAM user is the owner.

Within an IAM policy you can grant either programmatic access or AWS Management Console access to Amazon S3 resources.

Amazon Resource Names (ARN) are used for specifying resources in a policy.

---

- up:: [[Amazon S3]]
- relateTo:: [[AWS IAM]]
