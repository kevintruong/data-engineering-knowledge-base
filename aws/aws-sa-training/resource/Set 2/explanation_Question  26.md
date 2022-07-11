**Explanation:**

The only way to get this working is by using a VPC Security Group for the ELB that is configured to allow only the

internal service IP ranges associated with CloudFront. As these are updated from time to time, you can use AWS Lambda to

automatically update the addresses. This is done using a trigger that is triggered when AWS issues an SNS topic update

when the addresses are changed.

- ✅ :  "Create a VPC Security Group for the ELB and use AWS Lambda to automatically update the CloudFront internal

  service IP addresses when they change" is the correct answer.

- ❌ :  "Create an Origin Access Identity (OAI) and associate it with the distribution" is incorrect. You can use an

  OAI to restrict access to content in Amazon S3 but not on EC2 or ELB.

- ❌ :  "Use signed URLs or signed cookies to limit access to the content" is incorrect. Signed cookies and URLs are

  used to limit access to files but this does not stop people from circumventing CloudFront and accessing the ELB

  directly.

- ❌ :  "Use a Network ACL to restrict access to the ELB" is incorrect. A Network ACL can be used to restrict access

  to an ELB but it is recommended to use security groups and this solution is incomplete as it does not account for the

  fact that the internal service IP ranges change over time.

**References:**

<https://aws.amazon.com/blogs/security/how-to-automatically-update-your-security-groups-for-amazon>-

cloudfront-and-aws-waf-by-using-aws-lambda/

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content>-

delivery/amazon-cloudfront/

----

- #cloudfront #aws_lambda #<https://aws.amazon.com/blogs/security/how-to-automatically-update-your-security-groups-for-amazon>>- #aws #amazon_s3
