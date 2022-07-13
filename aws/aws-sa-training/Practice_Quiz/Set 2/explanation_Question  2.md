**Explanation:**

All solutions presented are highly available. The key requirement that must be satisfied is that the solution should be

cost-effective and you must choose the most cost-effective option.

Therefore, it’s best to eliminate services such as Amazon EC2 and ELB as these require ongoing costs even when they’re

not used. Instead, a fully serverless solution should be used. AWS Lambda, Amazon S3 and CloudFront are the best

services to use for these requirements.

- ✅ :  "Use AWS Lambda to manipulate the original images to the requested customization. Store the original and

  manipulated images in Amazon S3. Configure an Amazon CloudFront distribution with the S3 bucket as the origin" is the

  correct answer.

- ❌ :  "Use Amazon EC2 instances to manipulate the original images into the requested customization. Store the

  original and manipulated images in Amazon S3. Configure an Elastic Load Balancer in front of the EC2 instances" is

  incorrect. This is not the most cost-effective option as the ELB and EC2 instances will incur costs even when not

  used.

- ❌ :  "Use AWS Lambda to manipulate the original images to the requested customization. Store the original images

  in Amazon S3 and the manipulated images in Amazon DynamoDB. Configure an Elastic Load Balancer in front of the Amazon

  EC2 instances" is incorrect. This is not the most cost-effective option as the ELB will incur costs even when not

  used. Also, Amazon DynamoDB will incur RCU/WCUs when running and is not the best choice for storing images.

- ❌ :  "Use Amazon EC2 instances to manipulate the original images into the requested customization. Store the

  original images in Amazon S3 and the manipulated images in Amazon DynamoDB. Configure an Amazon CloudFront

  distribution with the S3 bucket as the origin" is incorrect. This is not the most cost- effective option as the EC2

  instances will incur costs even when not used

**References:**

<https://aws.amazon.com/serverless/>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/>

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/aws-lambda/>

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content>-

delivery/amazon-cloudfront/

----

- #amazon_cloudfront #amazon_cloudfront_distribution #cloudfront #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/> #aws_lambda
