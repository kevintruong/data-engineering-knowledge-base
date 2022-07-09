#### Question  22


**A Solutions Architect is creating a design for a two-tier application with a MySQL RDS back-end. The performance

requirements of the database tier are hard to quantify until the application is running and the Architect is concerned

about right-sizing the database.**


**What methods of scaling are possible after the MySQL RDS database is deployed? (Select TWO)**


1: Vertical scaling for read and write by choosing a larger instance size


2: Horizontal scaling for write capacity by enabling Multi-AZ


3: Vertical scaling for read and write by using Transfer Acceleration


4: Horizontal scaling for read and write by enabling Multi-Master RDS DB


5: Horizontal scaling for read capacity by creating a read-replica


**Answer: 1,5**


**Explanation:**


To handle a higher load in your database, you can vertically scale up your master database with a simple push of a

button. In addition to scaling your master database vertically, you can also improve the performance of a read-heavy

database by using read replicas to horizontally scale your database.


- CORRECT "Vertical scaling for read and write by choosing a larger instance size" is a correct answer.


- CORRECT "Horizontal scaling for read capacity by creating a read-replica" is also a correct answer.


- INCORRECT "Horizontal scaling for write capacity by enabling Multi-AZ" is incorrect. You cannot scale write capacity

  by enabling Multi-AZ as only one DB is active and can be written to.


- INCORRECT "Vertical scaling for read and write by using Transfer Acceleration" is incorrect. Transfer Acceleration is

  a feature of S3 for fast uploads of objects.


- INCORRECT "Horizontal scaling for read and write by enabling Multi-Master RDS DB" is incorrect. There is no such thing

  as a Multi-Master MySQL RDS DB (there is for Aurora).


**References:**


https://aws.amazon.com/blogs/database/scaling-your-amazon-rds-instance-vertically-and-horizontally/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-rds/

