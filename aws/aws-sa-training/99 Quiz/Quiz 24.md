## Quiz 24: The database tier of a web application is running on a Windows server on-premises. The database is a Microsoft SQL Server database. The application owner would like to migrate the database to an Amazon RDS instance.**

**How can the migration be executed with minimal administrative effort and downtime?**

- [ ] Use the AWS Server Migration Service (SMS) to migrate the server to Amazon EC2.Use AWS Database Migration Service (  DMS) to migrate the database to RDS
- [x] Use the AWS Database Migration Service (DMS) to directly migrate the database to RDS
- [ ] Use AWS DataSync to migrate the data from the database to Amazon S3. Use AWS Database Migration Service (DMS) to migrate the database to RDS
- [ ] Use the AWS Database Migration Service (DMS) to directly migrate the database to RDS. Use the Schema Conversion Tool (SCT) to enable conversion from Microsoft SQL Server to Amazon RDS

----
Answer:

- [x] Use the AWS Database Migration Service (DMS) to directly migrate the database to RDS
  **Explanation:**
  You can directly migrate Microsoft SQL Server from an on-premises server into Amazon RDS using the Microsoft SQL Server database engine. This can be achieved using the native Microsoft SQL Server tools, or using AWS DMS as depicted below:
  ![](aws-solution-architecture-practice-quiz-1641092708657.png)
- ✅: "Use the AWS Database Migration Service (DMS) to directly migrate the database to RDS" is the correct answer.

- ❌: "Use the AWS Server Migration Service (SMS) to migrate the server to Amazon EC2. Use AWS Database Migration Service (DMS) to migrate the database to RDS" is incorrect. You do not need to use the AWS SMS service to migrate the server into EC2 first. You can directly migrate the database online with minimal downtime.

- ❌: "Use AWS DataSync to migrate the data from the database to Amazon S3. Use AWS Database Migration Service (DMS) to migrate the database to RDS" is incorrect. AWS DataSync is used for migrating data, not databases.

- ❌: "Use the AWS Database Migration Service (DMS) to directly migrate the database to RDS. Use the Schema Conversion Tool (SCT) to enable conversion from Microsoft SQL Server to Amazon RDS" is incorrect. You do not need to use the SCT as you are migrating into the same destination database engine (RDS is just the platform).
  **References:**
  https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-on-premises-microsoft-sql- server-database-to-amazon-rds-for-sql-server.html
  https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.html
  https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.html
  https://aws.amazon.com/dms/schema-conversion-tool/


----
#quiz 
- relateTo:: [[Domain 4 Design Cost-Optimized Architectures]]