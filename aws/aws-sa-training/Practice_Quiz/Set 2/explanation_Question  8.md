**Explanation:**

The most cost-effective option is to migrate the website to an Amazon S3 bucket and configure that bucket for static

website hosting. To enable good performance for global users the solutions architect should then configure a CloudFront

distribution with the S3 bucket as the origin. This will cache the static content around the world closer to users.

- ✅ :  "Copy the website content to an Amazon S3 bucket. Configure the bucket to serve static webpage content.

  Configure Amazon CloudFront with the S3 bucket as the origin" is the correct answer.

- ❌ :  "Copy the website content to an Amazon S3 bucket. Configure the bucket to serve static webpage content.

  Replicate the S3 bucket to multiple AWS Regions" is incorrect as there is no solution here for directing users to the

  closest region. This could be a more cost-effective (though less elegant) solution if AWS Route 53 latency records are

  created.

- ❌ :  "Copy the website content to an Amazon EC2 instance. Configure Amazon Route 53 geolocation routing policies

  to select the closest origin" is incorrect as using Amazon EC2 instances is less cost-effective compared to hosting

  the website on S3. Also, geolocation routing does not achieve anything with only a single record.

- ❌ :  "Copy the website content to multiple Amazon EC2 instances in multiple AWS Regions. Configure AWS Route 53

  geolocation routing policies to select the closest region" is incorrect as using Amazon EC2 instances is less

  cost-effective compared to hosting the website on S3.

**References:**

<https://aws.amazon.com/premiumsupport/knowledge-center/cloudfront-serve-static-website/>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/>

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content>-

delivery/amazon-cloudfront/

----

- #configure_amazon_cloudfront #cloudfront #multiple_aws_regions #aws_route #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/>
