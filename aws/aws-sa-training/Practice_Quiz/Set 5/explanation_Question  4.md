**Explanation:**

The destination filesystem should be Amazon FSx for Windows File Server. This supports DFSN and is the most suitable

storage solution for Microsoft filesystems. AWS DataSync supports migrating to the Amazon FSx and automates the process.

- ✅ :  "Use AWS DataSync to migrate to Amazon FSx for Windows File Server" is the correct answer.

- ❌ :  "Use the AWS Server Migration Service to migrate to Amazon FSx for Lustre" is incorrect. The server

  migration service is used to migrate virtual machines and FSx for Lustre does not support Windows filesystems.

- ❌ :  "Use AWS DataSync to migrate to an Amazon EFS filesystem" is incorrect. You can migrate data to EFS using

  DataSync but it is the wrong destination for a Microsoft filesystem (Linux only).

- ❌ :  "Use the AWS Server Migration Service to migrate to an Amazon S3 bucket" is incorrect. The server migration

  service is used to migrate virtual machines and Amazon S3 is an object-based storage system and unsuitable for hosting

  a Microsoft filesystem.

**References:**

<https://aws.amazon.com/blogs/storage/migrate-to-amazon-fsx-for-windows-file-server-using-aws-datasync/>

<https://docs.aws.amazon.com/fsx/latest/WindowsGuide/migrate-files-fsx.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-fsx/>

----

- #<https://aws.amazon.com/blogs/storage/migrate-to-amazon-fsx-for-windows-file-server-using-aws-datasync/> #<https://docs.aws.amazon.com/fsx/latest/windowsguide/migrate-files-fsx.html> #amazon_efs_filesystem #aws_server_migration_service #aws_datasync
