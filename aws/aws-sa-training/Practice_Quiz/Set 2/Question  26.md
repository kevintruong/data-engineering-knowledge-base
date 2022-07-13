#### Question  26

**An application is running on Amazon EC2 behind an Elastic Load Balancer (ELB). Content is being published using Amazon

CloudFront and you need to restrict the ability for users to circumvent CloudFront and access the content directly

through the ELB.**

**How can you configure this solution?**

- [ ] :  Create an Origin Access Identity (OAI) and associate it with the distribution

- [ ] :  Use signed URLs or signed cookies to limit access to the content

- [ ] :  Use a Network ACL to restrict access to the ELB

- [x] :  Create a VPC Security Group for the ELB and use AWS Lambda to automatically update the CloudFront internal service IP

addresses when they change

----

- #cloudfront #aws_lambda #elastic_load_balancer #amazon_ec2 #elb
- hasExplain:: [[explanation_Question  26.md]]
