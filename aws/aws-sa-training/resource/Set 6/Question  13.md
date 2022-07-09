#### Question  13


**A company has launched a multi-tier application architecture. The web tier and database tier run on Amazon EC2

instances in private subnets within the same Availability Zone.**


**Which combination of steps should a Solutions Architect take to add high availability to this architecture?

(Select TWO)**


1: Create new public subnets in the same AZ for high availability and move the web tier to the public subnets


2: Create an Amazon EC2 Auto Scaling group and Application Load Balancer (ALB) spanning multiple AZs


3: Add the existing web application instances to an Auto Scaling group behind an Application Load Balancer

(ALB)


4: Create new private subnets in the same VPC but in a different AZ. Create a database using Amazon EC2 in one AZ


5: Create new private subnets in the same VPC but in a different AZ. Migrate the database to an Amazon RDS multi-AZ

deployment


Answer: 2,5


**Explanation:**


The Solutions Architect can use Auto Scaling group across multiple AZs with an ALB in front to create an elastic and

highly available architecture. Then, migrate the database to an Amazon RDS multi-AZ deployment to create HA for the

database tier. This results in a fully redundant architecture that can withstand the failure of an availability zone.


- CORRECT "Create an Amazon EC2 Auto Scaling group and Application Load Balancer (ALB) spanning multiple AZs" is a

  correct answer.


- CORRECT "Create new private subnets in the same VPC but in a different AZ. Migrate the database to an Amazon RDS

  multi-AZ deployment" is also a correct answer.


- INCORRECT "Create new public subnets in the same AZ for high availability and move the web tier to the public subnets"

  is incorrect. If subnets share the same AZ they are not suitable for splitting your tier across them for HA as the

  failure of a an AZ will take out both subnets.


- INCORRECT "Add the existing web application instances to an Auto Scaling group behind an Application Load Balancer (

  ALB)" is incorrect. The instances are in a single AZ so the Solutions Architect should create a new auto scaling group

  and launch instances across multiple AZs.


- INCORRECT "Create new private subnets in the same VPC but in a different AZ. Create a database using Amazon EC2 in one

  AZ" is incorrect. A database in a single AZ will not be highly available.


**References:**


https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-increase-availability.html


https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ec2/


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-rds/

