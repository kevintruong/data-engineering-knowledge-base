#### Question  42


**A Solutions Architect is designing a three-tier web application that includes an Auto Scaling group of Amazon EC2

Instances running behind an Elastic Load Balancer. The security team requires that all web servers must be accessible

only through the Elastic Load Balancer and that none of the web servers are directly accessible from the Internet.**


**How should the Architect meet these requirements?**


1: Create an Amazon CloudFront distribution in front of the Elastic Load Balancer


2: Configure the web servers' security group to deny traffic from the Internet


3: Configure the web tier security group to allow only traffic from the Elastic Load Balancer


4: Install a Load Balancer on an Amazon EC2 instance


**Answer: 3**


**Explanation:**


The web servers must be kept private so they will be not have public IP addresses. The ELB is Internet-facing so it will

be publicly accessible via it’s DNS address (and corresponding public IP).


To restrict web servers to be accessible only through the ELB you can configure the web tier security group to allow

only traffic from the ELB. You would normally do this by adding the ELBs security group to the rule on the web tier

security group


- CORRECT "Configure the web tier security group to allow only traffic from the Elastic Load Balancer" is the correct

  answer.


- INCORRECT "Create an Amazon CloudFront distribution in front of the Elastic Load Balancer" is incorrect. CloudFront

  distributions are used for caching content to improve performance for users on the Internet. They are not security

  devices to be used for restricting access to EC2 instances.


- INCORRECT "Configure the web servers' security group to deny traffic from the Internet" is incorrect. You cannot

  create deny rules in security groups.


- INCORRECT "Install a Load Balancer on an Amazon EC2 instance" is incorrect. This scenario is using an Elastic Load

  Balancer and these cannot be installed on EC2 instances (at least not by you, in reality all ELBs are actually running

  on EC2 instances but these are transparent to the AWS end user).


**References:**


https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-update-security-

groups.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/elastic-load-

balancing/

