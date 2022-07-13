**Explanation:**

All objects by default are private. Only the object owner has permission to access these objects. However, the object

owner can optionally share objects with others by creating a presigned URL, using their own security credentials, to

grant time-limited permission to download the objects.

When you create a presigned URL for your object, you must provide your security credentials, specify a bucket name, an

object key, specify the HTTP method (GET to download the object) and expiration date and time. The presigned URLs are

valid only for the specified duration.

Anyone who receives the presigned URL can then access the object. For example, if you have a video in your bucket and

both the bucket and the object are private, you can share the video with others by generating a presigned URL.

- ✅ :  "Generate a pre-signed URL and distribute it to the consumers" is the correct answer.

- ❌ :  "Enable public read access for the S3 bucket" is incorrect. Enabling public read access does not restrict

  the content to authorized consumers.

- ❌ :  "Use CloudFront to distribute the files using authorization hash tags" is incorrect. You cannot use

  CloudFront as hash tags are not a CloudFront authentication mechanism.

- ❌ :  "Configure an allow rule in the Security Group for the IP addresses of the consumers" is incorrect. Security

  Groups do not apply to S3 buckets.

**References:**

<https://docs.aws.amazon.com/AmazonS3/latest/dev/ShareObjectPreSignedURL.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/>

----

- #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/> #cloudfront #s3_bucket #s3_buckets #cloudfront_authentication_mechanism
