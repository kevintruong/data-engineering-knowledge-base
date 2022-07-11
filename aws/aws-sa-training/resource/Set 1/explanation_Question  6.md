**Explanation:**

A new version of the AWS Web Application Firewall was released in November 2019. With AWS WAF classic you create “IP

match conditions”, whereas with AWS WAF (new version) you create “IP set match statements”. Look out for wording on the

exam.

The IP match condition / IP set match statement inspects the IP address of a web request's origin against a set of IP

addresses and address ranges. Use this to allow or block web requests based on the IP addresses that the requests

originate from.

AWS WAF supports all IPv4 and IPv6 address ranges. An IP set can hold up to 10,000 IP addresses or IP address ranges to

check.

- ✅ :  "Modify the configuration of AWS WAF to add an IP match condition to block the malicious IP address" is the

  correct answer.

- ❌ :  "Modify the network ACL on the CloudFront distribution to add a deny rule for the malicious IP address"

  is incorrect as CloudFront does not sit within a subnet so network ACLs do not apply to it.

- ❌ :  "Modify the network ACL for the EC2 instances in the target groups behind the ALB to deny the malicious IP

  address" is incorrect as the source IP addresses of the data in the EC2 instances’ subnets will be the ELB IP

  addresses.

- ❌ :  "Modify the security groups for the EC2 instances in the target groups behind the ALB to deny the malicious

  IP address." is incorrect as you cannot create deny rules with security groups.

**References:**

<https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-ipset-match.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/security-identity>-

compliance/aws-waf-and-shield/

----

- #<https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-ipset-match.html_>> #aws_web_application_firewall #aws_waf #aws_waf_classic #aws
