#### Question  26


**An application is running on Amazon EC2 behind an Elastic Load Balancer (ELB). Content is being published using Amazon

CloudFront and you need to restrict the ability for users to circumvent CloudFront and access the content directly

through the ELB.**


**How can you configure this solution?**


1: Create an Origin Access Identity (OAI) and associate it with the distribution


2: Use signed URLs or signed cookies to limit access to the content


3: Use a Network ACL to restrict access to the ELB


4: Create a VPC Security Group for the ELB and use AWS Lambda to automatically update the CloudFront internal service IP

addresses when they change


Answer: 4


**Explanation:**


The only way to get this working is by using a VPC Security Group for the ELB that is configured to allow only the

internal service IP ranges associated with CloudFront. As these are updated from time to time, you can use AWS Lambda to

automatically update the addresses. This is done using a trigger that is triggered when AWS issues an SNS topic update

when the addresses are changed.


- CORRECT "Create a VPC Security Group for the ELB and use AWS Lambda to automatically update the CloudFront internal

  service IP addresses when they change" is the correct answer.


- INCORRECT "Create an Origin Access Identity (OAI) and associate it with the distribution" is incorrect. You can use an

  OAI to restrict access to content in Amazon S3 but not on EC2 or ELB.


- INCORRECT "Use signed URLs or signed cookies to limit access to the content" is incorrect. Signed cookies and URLs are

  used to limit access to files but this does not stop people from circumventing CloudFront and accessing the ELB

  directly.


- INCORRECT "Use a Network ACL to restrict access to the ELB" is incorrect. A Network ACL can be used to restrict access

  to an ELB but it is recommended to use security groups and this solution is incomplete as it does not account for the

  fact that the internal service IP ranges change over time.


**References:**


https://aws.amazon.com/blogs/security/how-to-automatically-update-your-security-groups-for-amazon-

cloudfront-and-aws-waf-by-using-aws-lambda/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-

delivery/amazon-cloudfront/

