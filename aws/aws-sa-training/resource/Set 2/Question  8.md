#### Question  8


**A static website currently runs in a company’s on-premises data center. The company plan to migrate the website to

AWS. The website must load quickly for global users and the solution must also be cost-effective.**


**What should a solutions architect do to accomplish this?**


1: Copy the website content to an Amazon S3 bucket. Configure the bucket to serve static webpage content. Replicate the

S3 bucket to multiple AWS Regions


2: Copy the website content to an Amazon S3 bucket. Configure the bucket to serve static webpage content. Configure

Amazon CloudFront with the S3 bucket as the origin


3: Copy the website content to an Amazon EC2 instance. Configure Amazon Route 53 geolocation routing policies to select

the closest origin


4: Copy the website content to multiple Amazon EC2 instances in multiple AWS Regions. Configure AWS Route 53 geolocation

routing policies to select the closest region


Answer: 2


**Explanation:**


The most cost-effective option is to migrate the website to an Amazon S3 bucket and configure that bucket for static

website hosting. To enable good performance for global users the solutions architect should then configure a CloudFront

distribution with the S3 bucket as the origin. This will cache the static content around the world closer to users.


- CORRECT "Copy the website content to an Amazon S3 bucket. Configure the bucket to serve static webpage content.

  Configure Amazon CloudFront with the S3 bucket as the origin" is the correct answer.


- INCORRECT "Copy the website content to an Amazon S3 bucket. Configure the bucket to serve static webpage content.

  Replicate the S3 bucket to multiple AWS Regions" is incorrect as there is no solution here for directing users to the

  closest region. This could be a more cost-effective (though less elegant) solution if AWS Route 53 latency records are

  created.


- INCORRECT "Copy the website content to an Amazon EC2 instance. Configure Amazon Route 53 geolocation routing policies

  to select the closest origin" is incorrect as using Amazon EC2 instances is less cost-effective compared to hosting

  the website on S3. Also, geolocation routing does not achieve anything with only a single record.


- INCORRECT "Copy the website content to multiple Amazon EC2 instances in multiple AWS Regions. Configure AWS Route 53

  geolocation routing policies to select the closest region" is incorrect as using Amazon EC2 instances is less

  cost-effective compared to hosting the website on S3.


**References:**


https://aws.amazon.com/premiumsupport/knowledge-center/cloudfront-serve-static-website/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-

delivery/amazon-cloudfront/

