#### AWS WAF AND AWS SHIELD GENERAL


AWS WAF and AWS Shield help protect your AWS resources from web exploits and DDoS attacks.


AWS WAF is a web application firewall service that helps protect your web apps from common exploits that could affect

app availability, compromise security, or consume excessive resources.


AWS Shield provides expanded DDoS attack protection for your AWS resources. Get 24/7 support from the DDoS response team

and detailed visibility into DDoS events.


We’ll now go into more detail on each service.


**AWS WEB APPLICATION FIREWALL (WAF)**


AWS WAF is a web application firewall that helps protect your web applications from common web exploits that could

affect application availability, compromise security, or consume excessive resources.


AWS WAF helps protect web applications from attacks by allowing you to configure rules that allow, block, or monitor (

count) web requests based on conditions that you define.


These conditions include IP addresses, HTTP headers, HTTP body, URI strings, SQL injection and cross-site scripting.


AWS WAF gives you control over which traffic to allow or block to your web applications by defining customizable web

security rules.


New rules can be deployed within minutes, letting you respond quickly to changing traffic patterns.


When AWS services receive requests for web sites, the requests are forwarded to AWS WAF for inspection against defined

rules.


Once a request meets a condition defined in the rules, AWS WAF instructs the underlying service to either block or allow

the request based on the action you define.


With AWS WAF you pay only for what you use.


AWS WAF pricing is based on how many rules you deploy and how many web requests your web application receives.


There are no upfront commitments.


AWS WAF is tightly integrated with Amazon CloudFront and the Application Load Balancer (ALB), services.


When you use AWS WAF on Amazon CloudFront, rules run in all AWS Edge Locations, located around the world close to end

users.


This means security doesn’t come at the expense of performance.


Blocked requests are stopped before they reach your web servers.


When you use AWS WAF on an Application Load Balancer, your rules run in region and can be used to protect

internet-facing as well as internal load balancers.

