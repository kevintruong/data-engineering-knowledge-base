**Explanation:**

```

Amazon Route 53

```

```

Name Type Value Health Record Type

failover.dctlabs.com A alb-pri ID Primary

failover.dctlabs.com A alb-sec Secondary

```

```

Region – ap-southeast- 2

```

```

Region – us-east- 1

```

```

Health Check

required on

Primary

```

```

DNS query

```

```

ALB

```

```

ALB

```

S3 Standard-IA is for data that is accessed less frequently, but requires rapid access when needed. S3 Standard-IA

offers the high durability, high throughput, and low latency of S3 Standard, with a low per GB storage price and per GB

retrieval fee. This combination of low cost and high performance make S3 Standard- IA ideal for long-term storage,

backups, and as a data store for disaster recovery files.

- ✅ :  "Store the files on Amazon S3 with a lifecycle policy that moves objects older than 2 years to S3 Standard

  Infrequent Access (S3 Standard-IA)" is the correct answer.

- ❌ :  "Store the files on Amazon Elastic File System (EFS) with a lifecycle policy that moves objects older than 2

  years to EFS Infrequent Access (EFS IA)" is incorrect. With EFS you can transition files to EFS IA after a file has

  not been accessed for a specified period of time with options up to 90 days. You cannot transition based on an age of

  2 years.

- ❌ :  "Store the files in Amazon Elastic Block Store (EBS) volumes. Schedule snapshots of the volumes. Use the

  snapshots to archive data older than 2 years" is incorrect. You cannot identify the age of data and archive snapshots

  in this way with EBS.

- ❌ :  "Store the files in Amazon Elastic Block Store (EBS) volumes. Create a lifecycle policy to move files older

  than 2 years to Amazon S3 Glacier" is incorrect. You cannot archive files from an EBS volume to Glacier using

  lifecycle policies.

**References:**

<https://aws.amazon.com/s3/storage-classes/>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/>

----

- #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/> #<https://aws.amazon.com/s3/storage-classes/> #amazon_elastic_file_system #amazon_s3 #s3_standard-_ia_ideal
