**Explanation:**

With security groups rules are always allow rules. The best practice is to configure the source as another security

group which is attached to the EC2 instances that traffic will come from. In this case you need to configure a rule that

allows TCP 1030 and configure the source as the web server security group (WebSG).

This allows traffic from the web servers to reach the application servers. You then need to allow communications on port

3306 (MYSQL/Aurora) from the AppSG security group to enable access to the database from the application servers.

- ✅ :  "On the DBSG security group, create a custom TCP rule for TCP 3306 and configure the AppSG security group as

  the source" is the correct answer.

- ✅ :  "On the AppSG security group, create a custom TCP rule for TCP 1030 and configure the WebSG security group as

  the source" is the correct answer.

- ❌ :  "On the AppSG security group, create a custom TCP rule for TCP 1030 and configure the DBSG security group as

  the source" is incorrect as the app tier will receive traffic from the web tier.

- ❌ :  "On the DBSG security group, create a custom TCP rule for TCP 3306 and configure the WebSG security group as

  the source" is incorrect as the databases will be receiving traffic from the app servers.

- ❌ :  "On the WebSG security group, create a custom TCP rule for TCP 1030 and configure the AppSG security group

  as the source" is incorrect as the web service will be receiving traffic from internet, presumably on standard

  HTTP/HTTPS ports. This web server security group has already been configured.

**References:**

<https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content>-

delivery/amazon-vpc/

----

- #dbsg_security_group #ec2_instances #security_groups_rules #websg_security_group #web_server_security_group
