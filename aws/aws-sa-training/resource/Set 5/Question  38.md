#### Question  38


**A customer runs an application on-premise that stores large media files. The data is mounted to different servers

using either the SMB or NFS protocols. The customer is having issues with scaling the storage infrastructure on-premise

and is looking for a way to offload the data set into the cloud whilst retaining a local cache for frequently accessed

content.**


**Which of the following is the best solution?**


1: Use the AWS Storage Gateway File Gateway


2: Use the AWS Storage Gateway Volume Gateway in cached volume mode


3: Create a script that migrates infrequently used data to S3 using multi-part upload


4: Establish a VPN and use the Elastic File System (EFS)


**Answer: 1**


**Explanation:**


File gateway provides a virtual on-premises file server, which enables you to store and retrieve files as objects in

Amazon S3. It can be used for on-premises applications, and for Amazon EC2-resident applications that need file storage

in S3 for object based workloads. Used for flat files only, stored directly on S3. File gateway offers SMB or NFS-based

access to data in Amazon S3 with local caching.


- CORRECT "Use the AWS Storage Gateway File Gateway" is the correct answer.


- INCORRECT "Use the AWS Storage Gateway Volume Gateway in cached volume mode" is incorrect. The AWS Storage Gateway

  Volume Gateway in cached volume mode is a block-based (not file-based) solution so you cannot mount the storage with

  the SMB or NFS protocols With Cached Volume mode – the entire dataset is stored on S3 and a cache of the most

  frequently accessed data is cached on-site.


- INCORRECT "Create a script that migrates infrequently used data to S3 using multi-part upload" is incorrect. Creating

  a script the migrates infrequently used data to S3 is possible but that data would then not be indexed on the primary

  filesystem so you wouldn’t have a method of retrieving it without developing some code to pull it back from S3. This

  is not the best solution.


- INCORRECT "Establish a VPN and use the Elastic File System (EFS)" is incorrect. You could mount EFS over a VPN but it

  would not provide you a local cache of the data.


**References:**


https://aws.amazon.com/storagegateway/file/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/aws-storage-

gateway/

