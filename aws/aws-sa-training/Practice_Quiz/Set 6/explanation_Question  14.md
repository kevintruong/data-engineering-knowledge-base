**Explanation:**

The AWS DMS service can be used to directly migrate the MySQL database to an Amazon RDS Multi-AZ deployment. The entire

process can be online and is managed for you. There is no need to perform schema translation between MySQL and RDS (

assuming you choose the MySQL RDS engine).

- ✅ :  "Use the AWS Database Migration Service (DMS) to directly migrate the database to an Amazon RDS MySQL Multi-AZ

  deployment" is the correct answer.

- ❌ :  "Use the AWS Database Migration Service (DMS) to directly migrate the database to an Amazon EC2 MySQL

  Multi-AZ deployment" is incorrect as there is no such thing as “multi-AZ” on Amazon EC2 with MySQL, you must use RDS.

- ❌ :  "Create a snapshot of the MySQL database server and use AWS DataSync to migrate the data Amazon S3. Launch a

  new Amazon RDS MySQL Multi-AZ deployment from the snapshot" is incorrect. You cannot create a snapshot of a MySQL

  database server running on-premises.

- ❌ :  "Use the AWS Database Migration Service (DMS) to directly migrate the database to Amazon RDS MySQL. Use the

  Schema Conversion Tool (SCT) to enable conversion from MySQL to Amazon RDS" is incorrect. There is no need to convert

  the schema when migrating from MySQL to Amazon RDS (MySQL engine).

```

Data center

```

```

Data center

```

```

Oracle

database

```

```

MySQL

database

```

```

Can be on-premises,

on EC 2 , or RDS

```

```

AWS Database Migration

Service

```

```

AWS Database Migration

Service

```

```

Amazon RedShift

```

```

Amazon Aurora

```

```

Destinations include Aurora,

RedShift DynamoDB, and

DocumentDB

```

```

DMS manages the entire

migration process

```

```

Use the Schema Conversion

Tool for heterogeneous

migrations

```

**References:**

<https://aws.amazon.com/rds/features/multi-az/>

<https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-rds/>

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/migration/aws-database>-

migration-service/

----

- #aws_database_migration_service #amazon_rds_multi_-_az_deployment #amazon_rds_mysql #mysql_rds_engine #aws_database_migration
