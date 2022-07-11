**Explanation:**

Amazon FSx for Windows File Server provides fully managed, highly reliable, and scalable file storage that is accessible

over the industry-standard Server Message Block (SMB) protocol. This is the most suitable destination for this use case.

AWS DataSync can be used to move large amounts of data online between on-premises storage and Amazon S3, Amazon EFS, or

Amazon FSx for Windows File Server. The source datastore can be Server Message Block

(SMB) file servers.

- ✅ :  "Migrate the data to Amazon FSx for Windows File Server using AWS DataSync" is the correct answer.

- ❌ :  "Migrate the data to Amazon EFS using the AWS Server Migration Service (SMS)" is incorrect. EFS is used for

  hosting filesystems accessed over NFS from Linux (not Windows). The SMS service is used for migrating virtual

  machines, not data.

- ❌ :  "Migrate the data to Amazon FSx for Lustre using AWS DataSync" is incorrect. Amazon FSx for Windows File

  Server should be used for hosting SMB shares.

- ❌ :  "Migrate the data to Amazon S3 using and AWS Snowball Edge device" is incorrect. Amazon S3 is an object

  store and unsuitable for hosting an SMB filesystem. Snowball is not required in this case as the data is not going to

  S3 and there are no time or bandwidth limitations mentioned in the scenario.

**References:**

<https://aws.amazon.com/fsx/windows/>

<https://aws.amazon.com/datasync/features/>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-fsx/>

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/migration/aws-datasync/>

----

- #<https://aws.amazon.com/datasync/features/> #aws_datasync #aws_server_migration_service #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-fsx/> #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/migration/aws-datasync/>
