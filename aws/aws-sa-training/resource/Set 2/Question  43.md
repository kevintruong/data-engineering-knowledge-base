#### Question  43

**A company hosts a popular web application that connects to an Amazon RDS MySQL DB instance running in a private VPC

subnet that was created with default ACL settings. The web servers must be accessible only to customers on an SSL

connection. The database should only be accessible to web servers in a public subnet.**

**Which solution meets these requirements without impacting other running applications? (Select TWO)**

- [x] Create a DB server security group that allows MySQL port 3306 inbound and specify the source as a web server security

group

- [x] Create a web server security group that allows HTTPS port 443 inbound traffic from Anywhere (0.0.0.0/0)

and apply it to the web servers

- [ ] Create a network ACL on the web server's subnet, allow HTTPS port 443 inbound, and specify the source as 0.0.0.0/0

- [ ] Create a DB server security group that allows the HTTPS port 443 inbound and specify the source as a web server

security group

- [ ] Create a network ACL on the DB subnet, allow MySQL port 3306 inbound for web servers, and deny all outbound traffic

- hasExplain:: [[explanation_Question  43.md]]

# amazon_rds_mysql_db_instance #db_server_security_group #web_server_security_group #web_server_security #db_subnet
