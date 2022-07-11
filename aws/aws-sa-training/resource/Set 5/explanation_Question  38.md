*

**Explanation:**

File gateway provides a virtual on-premises file server, which enables you to store and retrieve files as objects in

Amazon S3. It can be used for on-premises applications, and for Amazon EC2-resident applications that need file storage

in S3 for object based workloads. Used for flat files only, stored directly on S3. File gateway offers SMB or NFS-based

access to data in Amazon S3 with local caching.

* ✅ :  "Use the AWS Storage Gateway File Gateway" is the correct answer.

* ❌ :  "Use the AWS Storage Gateway Volume Gateway in cached volume mode" is incorrect. The AWS Storage Gateway

  Volume Gateway in cached volume mode is a block-based (not file-based) solution so you cannot mount the storage with

  the SMB or NFS protocols With Cached Volume mode – the entire dataset is stored on S3 and a cache of the most

  frequently accessed data is cached on-site.

* ❌ :  "Create a script that migrates infrequently used data to S3 using multi-part upload" is incorrect. Creating

  a script the migrates infrequently used data to S3 is possible but that data would then not be indexed on the primary

  filesystem so you wouldn’t have a method of retrieving it without developing some code to pull it back from S3. This

  is not the best solution.

* ❌ :  "Establish a VPN and use the Elastic File System (EFS)" is incorrect. You could mount EFS over a VPN but it

  would not provide you a local cache of the data.

**References:**

<https://aws.amazon.com/storagegateway/file/>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/aws-storage>- gateway/

----
* #aws_storage_gateway_file_gateway #aws_storage_gateway #aws_storage_gateway_volume_gateway #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/aws-storage>>- #<https://aws.amazon.com/storagegateway/file/>
