#### Question  65


**A critical database runs in your VPC for which availability is a concern. Which RDS DB instance events may force the

DB to be taken offline during a maintenance window?**


1: Selecting the Multi-AZ feature


2: Security patching


3: Promoting a Read Replica


4: Updating DB parameter groups


Answer: 2


**Explanation:**


Periodically, Amazon RDS performs maintenance on Amazon RDS resources. Maintenance most often involves updates to the DB

instance's underlying hardware, underlying operating system (OS), or database engine version. Updates to the operating

system most often occur for security issues and should be done as soon as possible.


Some maintenance items require that Amazon RDS take your DB instance offline for a short time. Maintenance items that

require a resource to be offline include required operating system or database patching. Required patching is

automatically scheduled only for patches that are related to security and instance reliability. Such patching occurs

infrequently (typically once every few months) and seldom requires more than a fraction of your maintenance window.


Enabling Multi-AZ, promoting a Read Replica and updating DB parameter groups are not events that take place during a

maintenance window.


- CORRECT "Security patching" is the correct answer.


- INCORRECT "Selecting the Multi-AZ feature" is incorrect as explained above.


- INCORRECT "Promoting a Read Replica" is incorrect as explained above.


- INCORRECT "Updating DB parameter groups" is incorrect as explained above.


**References:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-rds/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-rds/

