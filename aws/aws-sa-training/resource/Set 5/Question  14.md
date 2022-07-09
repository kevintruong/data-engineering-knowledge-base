#### Question  14


**An application that is being installed on an Amazon EC2 instance requires a persistent block storage volume. The data

must be encrypted at rest and regular volume-level backups must be automated.**


**Which solution options should be used?**


1: Use an encrypted Amazon EBS volume and use Data Lifecycle Manager to automate snapshots


```

AWS Lambda

```


```

Region

```


```

Amazon API Gateway

```


```

Mobile

client

```


```

Service

```


```

Website

```


```

Internet

```


```

VPC

```


```

Any other AWS service

```


```

REST API over

HTTPS

```


```

Public subnet

```


```

Private subnet

```


```

Lambda function

```


```

EC 2 Instance

```


```

Application Load Balancer

```


```

EC 2 Instance

```


```

Any public endpoint

```


2: Use an encrypted Amazon EFS filesystem and use an Amazon CloudWatch Events rule to start a backup copy of data using

AWS Lambda


3: Use server-side encryption on an Amazon S3 bucket and use Cross-Region-Replication to backup on a schedule


4: Use an encrypted Amazon EC2 instance store and copy the data to another EC2 instance using a cron job and a batch

script


Answer: 1


**Explanation:**


For block storage the Solutions Architect should use either Amazon EBS or EC2 instance store. However, the instance

store is non-persistent so EBS must be used. With EBS you can encrypt your volume and automate volume-level backups

using snapshots that are run by Data Lifecycle Manager.


- CORRECT "Use an encrypted Amazon EBS volume and use Data Lifecycle Manager to automate snapshots" is the correct

  answer.


- INCORRECT "Use an encrypted Amazon EFS filesystem and use an Amazon CloudWatch Events rule to start a backup copy of

  data using AWS Lambda" is incorrect. EFS is not block storage, it is a file-level storage service.


- INCORRECT "Use server-side encryption on an Amazon S3 bucket and use Cross-Region-Replication to backup on a schedule"

  is incorrect. Amazon S3 is an object-based storage system not a block-based storage system.


- INCORRECT "Use an encrypted Amazon EC2 instance store and copy the data to another EC2 instance using a cron job and a

  batch script " is incorrect as the EC2 instance store is a non-persistent volume.


**References:**


https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volumes.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ebs/

