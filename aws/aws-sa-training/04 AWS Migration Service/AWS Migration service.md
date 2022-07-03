## AWS MIGRATION SERVICE

[[AWS Snowball]]

[[The SnowBall Family]]

[[AWS Database Migration Service]]

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

- [ ] . Snowball can import to S3 but cannot export from S3
- [x] . Uses a secure storage device for physical transportation
- [ ] C. Can be used with multipart upload
- [x] . Petabyte scale data transport solution for transferring data into or out of AWS
- [ ] . Snowball can be used for migration on-premise to on-premise
**Question 1 answer: B,D**

Explanation:

Snowball is a petabyte scale data transport solution for transferring data into or out of AWS. 
It uses a secure storage device for physical transportation.
The AWS Snowball Client is software that is installed on a local computer and is used to identify, compress, encrypt, and transfer data. It uses 256 - bit encryption (managed with the AWS KMS)
and tamper-resistant enclosures with TPM.
 Snowball can import to S3 or export from S3.
Snowball cannot be used with multipart upload.
You cannot use Snowball for migration between on-premise data centers. 