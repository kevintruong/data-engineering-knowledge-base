#### Question  33


**An application running in an on-premise data center writes data to a MySQL database. A Solutions Architect is

re-architecting the application and plans to move the database layer into the AWS cloud on Amazon RDS. The application

layer will run in the on-premise data center.**


**What must be done to connect the application to the RDS database via the Internet? (Select TWO)**


1: Configure a NAT Gateway and attach the RDS database


2: Choose to make the RDS instance publicly accessible and place it in a public subnet


3: Select a public IP within the DB subnet group to assign to the RDS instance


4: Create a security group allowing access from the on-premise public IP to the RDS instance and assign to the RDS

instance


5: Create a DB subnet group that is publicly accessible


**Answer: 2,4**


**Explanation:**


When you create the RDS instance, you need to select the option to make it publicly accessible. A security group will

need to be created and assigned to the RDS instance to allow access from the public IP address of your application (or

firewall).


- CORRECT "Choose to make the RDS instance publicly accessible and place it in a public subnet" is a correct answer.


- CORRECT "Create a security group allowing access from the on-premise public IP to the RDS instance and assign to the

  RDS instance" is also a correct answer.


- INCORRECT "Configure a NAT Gateway and attach the RDS database" is incorrect. NAT Gateways are used for enabling

  Internet connectivity for EC2 instances in private subnets.


- INCORRECT "Select a public IP within the DB subnet group to assign to the RDS instance" is incorrect. The RDS instance

  does not require a public IP.


- INCORRECT "Create a DB subnet group that is publicly accessible" is incorrect. A DB subnet group is a collection of

  subnets (typically private) that you create in a VPC and that you then designate for your DB instance. The DB subnet

  group cannot be made publicly accessible, even if the subnets are public subnets, it is the RDS DB that must be

  configured to be publicly accessible.


**References:**


https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.Scenarios.html#USER_VPC.Scenario4


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-rds/

