#### Question  9


**A highly elastic application consists of three tiers. The application tier runs in an Auto Scaling group and processes

data and writes it to an Amazon RDS MySQL database. The Solutions Architect wants to restrict access to the database

tier to only accept traffic from the instances in the application tier. However, instances in the application tier are

being constantly launched and terminated.**


**How can the Solutions Architect configure secure access to the database tier?**


1: Configure the database security group to allow traffic only from the application security group


2: Configure the database security group to allow traffic only from port 3306


3: Configure a Network ACL on the database subnet to deny all traffic to ports other than 3306


4: Configure a Network ACL on the database subnet to allow all traffic from the application subnet


Answer: 1


**Explanation:**


The best option is to configure the database security group to only allow traffic that originates from the application

security group. You can also define the destination port as the database port. This setup will allow any instance that

is launched and attached to this security group to connect to the database.


- CORRECT "Configure the database security group to allow traffic only from the application security group" is the

  correct answer.


- INCORRECT "Configure the database security group to allow traffic only from port 3306" is incorrect. Port 3306 for

  MySQL should be the destination port, not the source.


- INCORRECT "Configure a Network ACL on the database subnet to deny all traffic to ports other than 3306" is incorrect.

  This does not restrict access specifically to the application instances.


- INCORRECT "Configure a Network ACL on the database subnet to allow all traffic from the application subnet"

  is incorrect. This does not restrict access specifically to the application instances.


**References:**


https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-

delivery/amazon-vpc/

