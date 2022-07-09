#### Question  4


**A Solutions Architect is designing a migration strategy for a company moving to the AWS Cloud. The company use a

shared Microsoft filesystem that uses Distributed File System Namespaces (DFSN). What will be the MOST suitable

migration strategy for the filesystem?**


1: Use the AWS Server Migration Service to migrate to an Amazon S3 bucket


2: Use the AWS Server Migration Service to migrate to Amazon FSx for Lustre


3: Use AWS DataSync to migrate to an Amazon EFS filesystem


4: Use AWS DataSync to migrate to Amazon FSx for Windows File Server


Answer: 4


**Explanation:**


The destination filesystem should be Amazon FSx for Windows File Server. This supports DFSN and is the most suitable

storage solution for Microsoft filesystems. AWS DataSync supports migrating to the Amazon FSx and automates the process.


- CORRECT "Use AWS DataSync to migrate to Amazon FSx for Windows File Server" is the correct answer.


- INCORRECT "Use the AWS Server Migration Service to migrate to Amazon FSx for Lustre" is incorrect. The server

  migration service is used to migrate virtual machines and FSx for Lustre does not support Windows filesystems.


- INCORRECT "Use AWS DataSync to migrate to an Amazon EFS filesystem" is incorrect. You can migrate data to EFS using

  DataSync but it is the wrong destination for a Microsoft filesystem (Linux only).


- INCORRECT "Use the AWS Server Migration Service to migrate to an Amazon S3 bucket" is incorrect. The server migration

  service is used to migrate virtual machines and Amazon S3 is an object-based storage system and unsuitable for hosting

  a Microsoft filesystem.


**References:**


https://aws.amazon.com/blogs/storage/migrate-to-amazon-fsx-for-windows-file-server-using-aws-datasync/


https://docs.aws.amazon.com/fsx/latest/WindowsGuide/migrate-files-fsx.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-fsx/

