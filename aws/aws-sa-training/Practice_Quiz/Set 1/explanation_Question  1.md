**Explanation:**

Amazon Elastic File System (Amazon EFS) provides a simple, scalable, fully managed elastic NFS file system for use with

AWS Cloud services and on-premises resources. It is built to scale on demand to petabytes without disrupting

applications, growing and shrinking automatically as you add and remove files, eliminating the need to provision and

manage capacity to accommodate growth.

Amazon EFS supports the Network File System version 4 (NFSv4.1 and NFSv4.0) protocol. Multiple Amazon EC2 instances can

access an Amazon EFS file system at the same time, providing a common data source for workloads and applications running

on more than one instance or server.

For this scenario, EFS is a great choice as it will provide a scalable file system that can be mounted by multiple EC2

instances and accessed simultaneously.

- ✅ :  "Store the data in an Amazon EFS filesystem. Mount the file system on the application instances" is the

  correct answer.

```

EC 2 Instance

```

```

Amazon Elastic File

System

```

```

File system

```

```

NFS v 1

```

```

/efs-mnt

```

```

EC 2 Instance

```

```

/efs-mnt

```

```

Availability Zone Availability Zone

```

```

Note: Linux only

```

```

Corporate data center

```

```

On-premises

client

```

- ❌ :  "Store the data in an Amazon EBS volume. Mount the EBS volume on the application instances" is incorrect.

  Though there is a new feature that allows (EBS multi-attach) that allows attaching multiple Nitro instances to a

  volume, this is not on the exam yet, and has some specific constraints.

- ❌ :  "Store the data in Amazon S3 Glacier. Update the vault policy to allow access to the application instances"

  is incorrect as S3 Glacier is not a suitable storage location for live access to data, it is used for archival.

- ❌ :  "Store the data in AWS Storage Gateway. Setup AWS Direct Connect between the Gateway appliance and the EC2

  instances" is incorrect. There is no reason to store the data on-premises in a Storage Gateway, using EFS is a much

  better solution.

**References:**

<https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-efs/>

----

- #amazon_elastic_file_system #amazon_efs_file_system #elastic_nfs_file_system #amazon_efs_filesystem #scalable_file_system
