**Explanation:**

The solution must use NFS file shares to access the migrated data without code modification. This means you can use

either Amazon EFS or AWS Storage Gateway – File Gateway. Both of these can be mounted using NFS from on-premises

applications.

However, EFS is the wrong answer as the solution asks to maximize availability and durability. The File Gateway backs

off of Amazon S3 which has much higher availability and durability than EFS which is why it is the best solution for

this scenario.

- ✅ :  "AWS Storage Gateway – File Gateway" is the correct answer.

- ❌ :  "Amazon Elastic Block Store" is incorrect. Amazon EBS is not a suitable solution as it is a block- based (

  not file-based like NFS) storage solution that you mount to EC2 instances in the cloud – not from on- premises

  applications.

- ❌ :  "Amazon Simple Storage Service" is incorrect. Amazon S3 does not offer an NFS interface.

- ❌ :  "Amazon Elastic File System" is incorrect as explained above.

**References:**

<https://docs.aws.amazon.com/storagegateway/latest/userguide/CreatingAnNFSFileShare.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-efs/>

----

- #aws_storage_gateway #amazon_elastic_file_system #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-efs/> #amazon_simple_storage_service #amazon_efs
