*

**Explanation:**

An inbound rule should be created for the relevant protocols (HTTP/HTTPS) and the source should be set to any address (

0.0.0.0/0).

The outbound rule should forward the relevant protocols (HTTP/HTTPS) and the destination should be set to the web server

security group.

Note that on the web server security group you’d want to add an Inbound rule allowing HTTP/HTTPS from the ELB security

group.

* ✅ :  "Add an Outbound rule that allows HTTP/HTTPS, and specify the destination as the web server security group"

  is a correct answer.

* ✅ :  "Add an Inbound rule that allows HTTP/HTTPS, and specify the source as 0.0.0.0/0" is also a correct answer.

* ❌ :  "Add an Outbound rule that allows ALL TCP, and specify the destination as the Internet Gateway"

  is incorrect as the relevant protocol should be specified and the destination should be the web server security group.

* ❌ :  "Add an Outbound rule that allows HTTP/HTTPS, and specify the destination as VPC CIDR" is incorrect. Using

  the VPC CIDR would not be secure and you cannot specify an Internet Gateway in a security group (not that you’d want

  to anyway).

* ❌ :  "Add an Inbound rule that allows HTTP/HTTPS, and specify the source as 0.0.0.0/32" is incorrect. The address

  0.0.0.0/32 is incorrect as the 32 mask means an exact match is required (0.0.0.0).

**References:**

<https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/elastic-load>-

balancing/

----
* #elb_security #web_server_security_group #vpc_cidr #outbound_rule #https
