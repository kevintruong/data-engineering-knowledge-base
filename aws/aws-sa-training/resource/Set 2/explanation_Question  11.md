**Explanation:**

Amazon FSx for Windows File Server provides fully managed, highly reliable file storage that is accessible over the

industry-standard Server Message Block (SMB) protocol. It is built on Windows Server, delivering a wide range of

administrative features such as user quotas, end-user file restore, and Microsoft Active Directory (AD)

integration. It offers single-AZ and multi-AZ deployment options, fully managed backups, and encryption of data at rest

and in transit.

This is the only solution presented that provides resilient storage for Windows instances.

- ✅ :  "Migrate the file share to Amazon FSx for Windows File Server" is the correct answer.

- ❌ :  "Migrate the file share to Amazon Elastic File System (Amazon EFS)" is incorrect as you cannot use Windows

  instances with Amazon EFS.

- ❌ :  "Migrate the file share to Amazon EBS" is incorrect as this is not a shared storage solution for multi-AZ

  deployments.

- ❌ :  "Migrate the file share to AWS Storage Gateway" is incorrect as with Storage Gateway replicated files end up

  on Amazon S3. The replacement storage solution should be a file share, not an object-based storage system.

**References:**

<https://aws.amazon.com/fsx/windows/>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/>

----

- #amazon_elastic_file_system #aws_storage_gateway #<https://aws.amazon.com/fsx/windows/> #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/> #amazon_efs
