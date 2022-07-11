*

**Explanation:**

With NACLs you can have permit and deny rules. Network ACLs contain a numbered list of rules that are evaluated in order

from the lowest number until the explicit deny. Network ACLs have separate inbound and outbound rules and each rule can

allow or deny traffic.

* ✅ :  "Use a Network ACL rule that denies connections from the block of IP addresses" is the correct answer.

* ❌ :  "Use a Security Group rule that denies connections from the block of IP addresses" is incorrect. With

  Security Groups you can only assign permit rules, you cannot assign deny rules.

* ❌ :  "Use CloudFront’s DDoS prevention features" is incorrect. CloudFront does have DDoS prevention features but

  we don’t know that this is a DDoS style of attack and CloudFront can only help where the traffic is using the

  CloudFront service to access cached content.

* ❌ :  "Create a Bastion Host restrict all connections to the Bastion Host only" is incorrect. A bastion host is

  typically used for admin purposes, allowing access to a single endpoint in the AWS cloud for administration using

  SSH/RDP. From the bastion instance you then connect to other EC2 instances in your subnets. This is not used as a

  method of adding security to production systems and cannot stop traffic from hitting application ports.

**References:**

<https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content>-

delivery/amazon-vpc/

----
* #cloudfront_service #use_cloudfront #cloudfront #aws_cloud #ddos_prevention_features
