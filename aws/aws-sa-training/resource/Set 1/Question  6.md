#### Question  6


**A website runs on Amazon EC2 instances in an Auto Scaling group behind an Application Load Balancer (ALB)

which serves as an origin for an Amazon CloudFront distribution. An AWS WAF is being used to protect against SQL

injection attacks. A review of security logs revealed an external malicious IP that needs to be blocked from accessing

the website.**


**What should a solutions architect do to protect the application?**


- [ ] Modify the network ACL on the CloudFront distribution to add a deny rule for the malicious IP address


- [x] Modify the configuration of AWS WAF to add an IP match condition to block the malicious IP address


- [ ] Modify the network ACL for the EC2 instances in the target groups behind the ALB to deny the malicious IP address


- [ ] Modify the security groups for the EC2 instances in the target groups behind the ALB to deny the malicious IP address



- hasExplain:: [[explanation_Question  6.md]]

#cloudfront #protect #aws #security #ec2 