## MIGRATION

### AWS Snowball

**GENERAL**

Petabyte scale data transport solution for transferring data into or out of AWS.

Uses a secure storage device for physical transportation.

AWS Snowball Client is software that is installed on a local computer and is used to identify,
compress, encrypt, and transfer data.

Uses 256 - bit encryption (managed with the AWS KMS) and tamper-resistant enclosures with TPM.

Snowball must be ordered from and returned to the same region.

To speed up data transfer it is recommended to run simultaneous instances of the AWS Snowball
Client in multiple terminals and transfer small files as batches.

Snowball can import to S3 or export from S3.

**THE SNOWBALL FAMILY**

Several services are offered in the Snowball family.

The table below describes these at a high-level:

Snowball (80TB) (50TB model available only in the USA).

Snowball Edge (100TB) comes with onboard storage and compute capabilities.

Snowmobile – exabyte scale with up to 100PB per Snowmobile.

AWS Import/export is when you send your own disks into AWS – this is being deprecated in favour
of Snowball.


### AWS Database Migration Service

AWS Database Migration Service helps you migrate databases to AWS quickly and securely.

The source database remains fully operational during the migration, minimizing downtime to
applications that rely on the database.

The AWS Database Migration Service can migrate your data to and from most widely used
commercial and open-source databases.

Supported migration paths include:

- On-premises and EC2 databases to Amazon RDS or Amazon Aurora.
- Homogeneous migrations such as Oracle to Oracle.
- Heterogeneous migrations between different database platforms, such as Oracle or
    Microsoft SQL Server to Amazon Aurora.

With AWS Database Migration Service, you can continuously replicate your data with high
availability and consolidate databases into a petabyte-scale data warehouse by streaming data to
Amazon Redshift and Amazon S3.

When migrating databases to Amazon Aurora, Amazon Redshift, Amazon DynamoDB or Amazon
DocumentDB (with MongoDB compatibility) you can use DMS free for six months.

Use along with the Schema Conversion Tool (SCT) to migrate databases to AWS RDS or EC2-based
databases.

The source database remains fully operational during the migration, minimizing downtime to
applications that rely on the database.

The AWS Database Migration Service can migrate your data to and from most widely used
commercial and open-source databases.

Schema Conversion Tool can copy database schemas for homogenous migrations (same database)
and convert schemas for heterogeneous migrations (different database).

DMS is used for smaller, simpler conversions and also supports MongoDB and DynamoDB.

SCT is used for larger, more complex datasets like data warehouses.

DMS has replication functions for on-premise to AWS or to Snowball or S3.

### AWS DataSync

AWS DataSync makes it simple and fast to move large amounts of data online between on-premises
storage and Amazon S3 or Amazon Elastic File System (Amazon EFS).

Manual tasks related to data transfers can slow down migrations and burden IT operations.

DataSync eliminates or automatically handles many of these tasks, including scripting copy jobs,
scheduling and monitoring transfers, validating data, and optimizing network utilization.

The DataSync software agent connects to your Network File System (NFS) and Server Message Block
(SMB) storage, so you don’t have to modify your applications.


DataSync can transfer hundreds of terabytes and millions of files over the internet or AWS Direct
Connect links.

You can use DataSync to migrate active data sets or archives to AWS, transfer data to the cloud for
timely analysis and processing, or replicate data to AWS for business continuity.

DataSync can copy data between Network File System (NFS) or Server Message Block (SMB) file
servers, all Amazon Simple Storage Service (Amazon S3) storage classes, and Amazon Elastic File
System (Amazon EFS) file systems.

All data is encrypted in transit with Transport Layer Security (TLS).

DataSync supports using default encryption for S3 buckets using Amazon S3-Managed Encryption
Keys (SSE-S3), and Amazon EFS file system encryption of data at rest.

Task scheduling enables you to configure periodically executing a task, to detect and copy changes
from your source storage system to the destination.

You can schedule your tasks using the AWS DataSync Console or AWS Command Line Interface (CLI),
without needing to write and run scripts to manage repeated transfers.

The DataSync agent connects to your existing storage systems using the industry-standard NFS and
SMB protocols.

The agent transfers data rapidly and deposits it your designated Amazon S3 bucket or Amazon EFS
file system.

When copying data to Amazon S3, DataSync automatically converts each file to be a single S3 object
in a 1:1 relationship and preserves POSIX metadata as Amazon S3 object metadata.

When you copy objects that contain file system metadata back to file formats, the original file
metadata that DataSync copied to S3 is restored.

Similarly, when Amazon EFS is the destination for your data, DataSync preserves existing directory
structures and file metadata.

DataSync supports VPC endpoints (powered by AWS PrivateLink) in order to move files directly into
your Amazon VPC.


### Migration Quiz Question

**Question 1:**

The financial institution you are working for stores large amounts of historical transaction records.
There are over 25TB of records and your manager has decided to move them into the AWS Cloud.
You are planning to use Snowball as copying the data would take too long. Which of the statements
below are true regarding Snowball? (choose 2)

```
A. Snowball can import to S3 but cannot export from S3
B. Uses a secure storage device for physical transportation
C. Can be used with multipart upload
D. Petabyte scale data transport solution for transferring data into or out of AWS
E. Snowball can be used for migration on-premise to on-premise
```
**Question 1 answer: B,D**

Explanation:

```
Snowball is a petabyte scale data transport solution for transferring data into or out of AWS. It
uses a secure storage device for physical transportation.
The AWS Snowball Client is software that is installed on a local computer and is used to identify,
compress, encrypt, and transfer data. It uses 256 - bit encryption (managed with the AWS KMS)
and tamper-resistant enclosures with TPM.
Snowball can import to S3 or export from S3.
Snowball cannot be used with multipart upload.
You cannot use Snowball for migration between on-premise data centers.
```
