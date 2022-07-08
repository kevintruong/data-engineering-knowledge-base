## Quiz 61: Your company shares some HR videos stored in an Amazon S3 bucket via CloudFront. You need to restrict access to the private content so users coming from specific IP addresses can access the videos and ensure direct access via the Amazon S3 bucket is not possible.**

**How can this be achieved?**

- [ ] Configure CloudFront to require users to access the files using signed cookies, create an origin access identity (

  OAI) and instruct users to login with the OAI

- [ ] Configure CloudFront to require users to access the files using a signed URL, create an origin access identity

  (OAI) and restrict access to the files in the Amazon S3 bucket to the OAI

- [ ] Configure CloudFront to require users to access the files using signed cookies, and move the files to an encrypted EBS volume

- [ ] Configure CloudFront to require users to access the files using a signed URL, and configure the S3 bucket as a website endpoint

----
Answer: 2
**Explanation:**
A signed URL includes additional information, for example, an expiration date and time, that gives you more control over access to your content. You can also specify the IP address or range of IP addresses of the users who can access your content. If you use CloudFront signed URLs (or signed cookies) to limit access to files in your Amazon S3 bucket, you may also want to prevent users from directly accessing your S3 files by using Amazon S3 URLs. To achieve this you can create an origin access identity (OAI), which is a special CloudFront user, and associate the OAI with your distribution. You can then change the permissions either on your Amazon S3 bucket or on the files in your bucket so that only the origin access identity has read permission (or read and download permission).
![](aws-solution-architecture-practice-quiz-1641093922014.png)

- ✅: "Configure CloudFront to require users to access the files using a signed URL, create an origin access identity (OAI) and restrict access to the files in the Amazon S3 bucket to the OAI" is the correct answer.

- ❌: "Configure CloudFront to require users to access the files using signed cookies, create an origin access identity (OAI) and instruct users to login with the OAI" is incorrect. Users cannot login with an OAI.

- ❌: "Configure CloudFront to require users to access the files using signed cookies, and move the files to an encrypted EBS volume" is incorrect. You cannot use CloudFront and an OAI when your S3 bucket is configured as a website endpoint.

- ❌: "Configure CloudFront to require users to access the files using a signed URL, and configure the S3 bucket as a website endpoint" is incorrect. You cannot use CloudFront to pull data directly from an EBS volume.
  **References:**
  https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html
