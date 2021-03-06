*

**Explanation:**

To allow read access to the S3 video assets from the public-facing web application, you can add a bucket policy that

allows s3:GetObject permission with a condition, using the aws:referer key, that the get request must originate from

specific webpages. This is a good answer as it fully satisfies the objective of ensuring the that EC2 instance can

access the videos but direct access to the videos from other sources is prevented.

* ✅ :  "Use a bucket policy to only allow referrals from the main website URL" is the correct answer.

* ❌ :  "Launch the website Amazon EC2 instance using an IAM role that is authorized to access the videos" is

  incorrect. Launching the EC2 instance with an IAM role that is authorized to access the videos is only half a solution

  as you would also need to create a bucket policy that specifies that the IAM role is granted access.

* ❌ :  "Restrict access to the bucket to the public CIDR range of the company locations" is incorrect. Restricting

  access to the bucket to the public CIDR range of the company locations will stop third-parties from accessing the

  bucket however it will also stop the EC2 instance from accessing the bucket and the question states that the EC2

  instance is serving the files directly.

* ❌ :  "Use a bucket policy to only allow the public IP address of the Amazon EC2 instance hosting the customer

  website" is incorrect. You can use condition statements in a bucket policy to restrict access via IP address. However,

  using the referrer condition in a bucket policy is preferable as it is a best practice to use DNS names / URLs instead

  of hard-coding IPs whenever possible.

**References:**

<https://docs.aws.amazon.com/AmazonS3/latest/dev/example-bucket-policies.html#example-bucket-policies>- use-case- 4

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/>

----
* #s3_video_assets #website_amazon_ec2_instance #<https://docs.aws.amazon.com/amazons3/latest/dev/example-bucket-policies.html#example-bucket-policies>-_use> #aws #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/>
