#### Question  46


**A bespoke application consisting of three tiers is being deployed in a VPC. You need to create three security groups.

You have configured the WebSG (web server) security group and now need to configure the AppSG

(application tier) and DBSG (database tier). The application runs on port 1030 and the database runs on 3306.**


**Which rules should be created according to security best practice? (Select TWO)**


1: On the DBSG security group, create a custom TCP rule for TCP 3306 and configure the AppSG security group as the

source


2: On the AppSG security group, create a custom TCP rule for TCP 1030 and configure the WebSG security group as the

source


3: On the AppSG security group, create a custom TCP rule for TCP 1030 and configure the DBSG security group as the

source


4: On the DBSG security group, create a custom TCP rule for TCP 3306 and configure the WebSG security group as the

source


5: On the WebSG security group, create a custom TCP rule for TCP 1030 and configure the AppSG security group as the

source


Answer: 1,2


**Explanation:**


With security groups rules are always allow rules. The best practice is to configure the source as another security

group which is attached to the EC2 instances that traffic will come from. In this case you need to configure a rule that

allows TCP 1030 and configure the source as the web server security group (WebSG).


This allows traffic from the web servers to reach the application servers. You then need to allow communications on port

3306 (MYSQL/Aurora) from the AppSG security group to enable access to the database from the application servers.


- CORRECT "On the DBSG security group, create a custom TCP rule for TCP 3306 and configure the AppSG security group as

  the source" is the correct answer.


- CORRECT "On the AppSG security group, create a custom TCP rule for TCP 1030 and configure the WebSG security group as

  the source" is the correct answer.


- INCORRECT "On the AppSG security group, create a custom TCP rule for TCP 1030 and configure the DBSG security group as

  the source" is incorrect as the app tier will receive traffic from the web tier.


- INCORRECT "On the DBSG security group, create a custom TCP rule for TCP 3306 and configure the WebSG security group as

  the source" is incorrect as the databases will be receiving traffic from the app servers.


- INCORRECT "On the WebSG security group, create a custom TCP rule for TCP 1030 and configure the AppSG security group

  as the source" is incorrect as the web service will be receiving traffic from internet, presumably on standard

  HTTP/HTTPS ports. This web server security group has already been configured.


**References:**


https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-

delivery/amazon-vpc/

