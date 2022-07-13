**Explanation:**

The AWS Web Application Firewall (WAF) is available on the Application Load Balancer (ALB). You can use AWS WAF directly

on Application Load Balancers (both internal and external) in a VPC, to protect your websites and web services.

Attackers sometimes insert scripts into web requests in an effort to exploit vulnerabilities in web applications. You

can create one or more cross-site scripting match conditions to identify the parts of web requests, such as the URI or

the query string, that you want AWS WAF to inspect for possible malicious scripts.

- ✅ :  "Create an Application Load Balancer. Put the web layer behind the load balancer and enable AWS WAF" is the

  correct answer.

- ❌ :  "Create a Classic Load Balancer. Put the web layer behind the load balancer and enable AWS WAF" is incorrect

  as you cannot use AWS WAF with a classic load balancer.

- ❌ :  "Create a Network Load Balancer. Put the web layer behind the load balancer and enable AWS WAF" is incorrect

  as you cannot use AWS WAF with a network load balancer.

- ❌ :  "Create an Application Load Balancer. Put the web layer behind the load balancer and use AWS Shield

  Standard" is incorrect as you cannot use AWS Shield to protect against XSS attacks. Shield is used to protect against

  DDoS attacks.

**References:**

<https://docs.aws.amazon.com/waf/latest/developerguide/classic-web-acl-xss-conditions.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/security-identity>-

compliance/aws-waf-and-shield/

----

- #aws_waf #aws_web_application_firewall #aws #aws_shield #application_load_balancers
