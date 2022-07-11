**Explanation:**

A signed URL includes additional information, for example, an expiration date and time, that gives you more control over

access to your content. You can also specify the IP address or range of IP addresses of the users who can access your

content.

If you use CloudFront signed URLs (or signed cookies) to limit access to files in your Amazon S3 bucket, you may also

want to prevent users from directly accessing your S3 files by using Amazon S3 URLs. To achieve this you can create an

origin access identity (OAI), which is a special CloudFront user, and associate the OAI with your distribution.

You can then change the permissions either on your Amazon S3 bucket or on the files in your bucket so that only the

origin access identity has read permission (or read and download permission).

- ✅ :  "Configure CloudFront to require users to access the files using a signed URL, create an origin access

  identity (OAI) and restrict access to the files in the Amazon S3 bucket to the OAI" is the correct answer.

- ❌ :  "Configure CloudFront to require users to access the files using signed cookies, create an origin access

  identity (OAI) and instruct users to login with the OAI" is incorrect. Users cannot login with an OAI.

- ❌ :  "Configure CloudFront to require users to access the files using signed cookies, and move the files to an

  encrypted EBS volume" is incorrect. You cannot use CloudFront and an OAI when your S3 bucket is configured as a

  website endpoint.

- ❌ :  "Configure CloudFront to require users to access the files using a signed URL, and configure the S3 bucket

  as a website endpoint" is incorrect. You cannot use CloudFront to pull data directly from an EBS volume.

**References:**

<https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access>- to-s3.html

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/>

----

- #<https://docs.aws.amazon.com/amazoncloudfront/latest/developerguide/private-content-restricting-access>-_to-s3.html> #configure_cloudfront #special_cloudfront_user #cloudfront #amazon_s3_urls
