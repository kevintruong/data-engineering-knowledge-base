**Explanation:**

A VPC automatically comes with a modifiable default network ACL. By default, it allows all inbound and outbound IPv4

traffic. Custom network ACLs deny everything inbound and outbound by default but in this case a default network ACL is

being used.

Inbound connections to web servers will be coming in on port 443 from the Internet so creating a security group to allow

this port from 0.0.0.0/0 and applying it to the web servers will allow this traffic.

- ✅ :  "Create a DB server security group that allows MySQL port 3306 inbound and specify the source as a web server

  security group" is the correct answer.

- ✅ :  "Create a web server security group that allows HTTPS port 443 inbound traffic from Anywhere

  (0.0.0.0/0) and apply it to the web servers" is the correct answer.

- ❌ :  "Create a network ACL on the web server's subnet, allow HTTPS port 443 inbound, and specify the source as

  0.0.0.0/0" is incorrect as a default network ACL will already allow this traffic.

- ❌ :  "Create a DB server security group that allows the HTTPS port 443 inbound and specify the source as a web

  server security group" is incorrect. The MySQL DB will be listening on port 3306. Therefore, the security group that

  is applied to the DB servers should allow 3306 inbound from the web servers security group.

- ❌ :  "Create a network ACL on the DB subnet, allow MySQL port 3306 inbound for web servers, and deny all outbound

  traffic" is incorrect as a default network ACL will already allow this traffic.

**References:**

<https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content>-

delivery/amazon-vpc/

----

- #db_server_security_group #web_servers_security_group #web_server_security_group #mysql_port #server_security_group
