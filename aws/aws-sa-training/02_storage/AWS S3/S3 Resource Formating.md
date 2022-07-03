### S3 Resource Formating

**The format for any resource on AWS is:**

`arn:partition:service:region:namespace:relative-id.`

**For S3 resources:**

- aws is a common partition name.
- s3 is the service.
- You don’t specify Region and namespace.
- For Amazon S3, it can be a bucket-name or a bucket-name/object-key. You can use wild card

**The format for S3 resources is:**

arn:aws:s3:::bucket_name.

arn:aws:s3:::bucket_name/key_name.

A bucket owner can grant cross-account permissions to another AWS account (or users in an account) to upload objects.

The AWS account that uploads the objects owns them.

The bucket owner does not have permissions on objects that other accounts own, however:

- The bucket owner pays the charges.
- The bucket owner can deny access to any objects regardless of ownership.
- The bucket owner can archive any objects or restore archived objects regardless of ownership.

----
- up:: [[Amazon S3]]