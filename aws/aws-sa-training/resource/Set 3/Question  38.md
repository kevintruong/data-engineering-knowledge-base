#### Question  38


**You need a service that can provide you with control over which traffic to allow or block to your web applications by

defining customizable web security rules. You need to block common attack patterns, such as SQL injection and cross-site

scripting, as well as creating custom rules for your own applications.**


**Which AWS service fits these requirements?**


1: Security Groups


2: AWS WAF


3: CloudFront


4: Route 53


Answer: 2


**Explanation:**


AWS WAF is a web application firewall that helps detect and block malicious web requests targeted at your web

applications. AWS WAF allows you to create rules that can help protect against common web exploits like SQL injection

and cross-site scripting. With AWS WAF you first identify the resource (either an Amazon


CloudFront distribution or an Application Load Balancer) that you need to protect. You then deploy the rules and filters

that will best protect your applications.


The other services listed do not enable you to create custom web security rules that can block known malicious attacks.


- CORRECT "AWS WAF" is the correct answer.


- INCORRECT "Security Groups" is incorrect as explained above.


- INCORRECT "CloudFront" is incorrect as explained above.


- INCORRECT "Route 53" is incorrect as explained above.


**References:**


https://aws.amazon.com/waf/details/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/security-identity-

compliance/aws-waf-and-shield/

