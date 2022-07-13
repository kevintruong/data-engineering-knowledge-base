#### ACCESS AND ACCESS POLICIES

**There are four mechanisms for controlling access to Amazon S3 resources:**

- IAM policies.

- Bucket policies.

- Access Control Lists (ACLs).

- Query string authentication (URL to an Amazon S3 object which is only valid
  for a limited time).

Access auditing can be configured by configuring an Amazon S3 bucket to create
access log records for all requests made

against it.

For capturing IAM/user identity information in logs configure AWS CloudTrail
Data Events.

By default, a bucket, its objects, and related sub-resources are all private.

By default, only a resource owner can access a bucket.

The resource owner refers to the AWS account that creates the resource.

With IAM the account owner rather than the IAM user is the owner.

Within an IAM policy you can grant either programmatic access or AWS Management
Console access to Amazon S3 resources.

Amazon Resource Names (ARN) are used for specifying resources in a policy.

**The format for any resource on AWS is:**

arn:partition:service:region:namespace:relative-id.

**For S3 resources:**

- aws is a common partition name.

- s3 is the service.

- You don’t specify Region and namespace.

- For Amazon S3, it can be a bucket-name or a bucket-name/object-key. You can
  use wild card

**The format for S3 resources is:**

arn:aws:s3:::bucket_name.

arn:aws:s3:::bucket_name/key_name.

A bucket owner can grant cross-account permissions to another AWS account (or
users in an account) to upload objects.

The AWS account that uploads the objects owns them.

The bucket owner does not have permissions on objects that other accounts own,
however:

- The bucket owner pays the charges.

- The bucket owner can deny access to any objects regardless of ownership.

- The bucket owner can archive any objects or restore archived objects
  regardless of ownership.

**Access to buckets and objects can be granted to:**

- Individual users.

- AWS accounts.

- Everyone (public/anonymous).

- All authenticated users (AWS users).

Access policies define access to resources and can be associated with
resources (buckets and objects) and users.

You can use the AWS Policy Generator to create a bucket policy for your Amazon
S3 bucket.

The categories of policy are resource-based policies and user policies.

**Resource-based policies:**

- Attached to buckets and objects.

- ACL-based policies define permissions.

- ACLs can be used to grant read/write permissions to other accounts.

- Bucket policies can be used to grant other AWS accounts or IAM users
  permission to the bucket and objects.

**User policies:**

- Can use IAM to manage access to S3 resources.

- Using IAM you can create users, groups and roles and attach access policies to
  them granting them access to resources.

- You cannot grant anonymous permissions in an IAM user policy as the policy is
  attached to a user.

- User policies can grant permissions to a bucket and the objects in it.

**ACLs:**

- S3 ACLs enable you to manage access to buckets and objects.

- Each bucket and object has an ACL attached to it as a subresource.

- Bucket and object permissions are independent of each other.

- The ACL defines which AWS accounts (grantees) or pre-defined S3 groups are
  granted access and the type of access.

- A grantee can be an AWS account or one of the predefined Amazon S3 groups.

- When you create a bucket or an object, S3 creates a default ACL that grants
  the resource owner full control over the

  resource.

**Cross account access:**

- You grant permission to another AWS account using the email address or the
  canonical user ID.

- However, if you provide an email address in your grant request, Amazon S3
  finds the canonical user ID for that account

  and adds it to the ACL.

- Grantee accounts can then then delegate the access provided by other accounts
  to their individual users.

