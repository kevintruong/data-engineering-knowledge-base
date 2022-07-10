#### Question  46

**A bespoke application consisting of three tiers is being deployed in a VPC. You need to create three security groups.

You have configured the WebSG (web server) security group and now need to configure the AppSG

(application tier) and DBSG (database tier). The application runs on port 1030 and the database runs on 3306.**

**Which rules should be created according to security best practice? (Select TWO)**

- [x] On the DBSG security group, create a custom TCP rule for TCP 3306 and configure the AppSG security group as the

source

- [x] On the AppSG security group, create a custom TCP rule for TCP 1030 and configure the WebSG security group as the

source

- [ ] On the AppSG security group, create a custom TCP rule for TCP 1030 and configure the DBSG security group as the

source

- [ ] On the DBSG security group, create a custom TCP rule for TCP 3306 and configure the WebSG security group as the

source

- [ ] On the WebSG security group, create a custom TCP rule for TCP 1030 and configure the AppSG security group as the

source

- hasExplain:: [[explanation_Question  46.md]]

# dbsg_security_group #database_tier #dbsg #websg_security_group #vpc
