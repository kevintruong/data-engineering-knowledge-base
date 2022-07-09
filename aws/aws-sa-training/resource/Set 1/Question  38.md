#### Question  38


**You are a Solutions Architect at Digital Cloud Training. A large multi-national client has requested a design for a

multi-region, multi-master database. The client has requested that the database be designed for fast, massively scaled

applications for a global user base. The database should be a fully managed service including the replication.**


**Which AWS service can deliver these requirements?**


1: DynamoDB with Global Tables and Multi-Region Replication


2: EC2 instances with EBS replication


3: S3 with Cross Region Replication


4: RDS with Multi-AZ


Answer: 1


**Explanation:**


Amazon DynamoDB global tables provide a fully managed solution for deploying a multiregion, multi-master database,

without having to build and maintain your own replication solution. With global tables you can specify the AWS Regions

where you want the table to be available. DynamoDB performs all of the necessary tasks to create identical tables in

these Regions and propagate ongoing data changes to all of them.


DynamoDB global tables are ideal for massively scaled applications with globally dispersed users. In such an

environment, users expect very fast application performance. Global tables provide automatic multi-master replication to

AWS Regions worldwide. They enable you to deliver low-latency data access to your users no matter where they are

located.


- CORRECT "DynamoDB with Global Tables and Multi-Region Replication" is the correct answer.


- INCORRECT "EC2 instances with EBS replication" is incorrect. There is no such thing as EBS replication. You could

  build your own database stack on EC2 with DB-level replication but that is not what is presented in the answer.


- INCORRECT "S3 with Cross Region Replication" is incorrect. S3 is an object store not a multi-master database.


- INCORRECT "RDS with Multi-AZ" is incorrect. RDS with Multi-AZ is not multi-master (only one DB can be written to at a

  time), and does not span regions.


**References:**


https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-

dynamodb/

