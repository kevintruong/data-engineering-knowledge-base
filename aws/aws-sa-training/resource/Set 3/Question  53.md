#### Question  53


**You are designing a solution on AWS that requires a file storage layer that can be shared between multiple EC2

instances. The storage should be highly-available and should scale easily.**


**Which AWS service can be used for this design?**


1: Amazon S3


2: Amazon EC2 instance store


3: Amazon EFS


```

Amazon Simple Queue

Service

```


```

Queue

```


```

EC 2 instance

polls SQS

```


```

Web Tier

```


```

Auto Scaling Group

```


```

App Tier

```


```

Auto Scaling Group

Decoupled integration

```


4: Amazon EBS


Answer: 3


**Explanation:**


Amazon EFS provides file storage in the AWS Cloud. With Amazon EFS, you can create a file system, mount the file system

on an Amazon EC2 instance, and then read and write data to and from your file system.


You can mount an Amazon EFS file system in your VPC, through the Network File System versions 4.0 and 4.1

(NFSv4) protocol. We recommend using a current generation Linux NFSv4.1 client, such as those found in the latest Amazon

Linux, Redhat, and Ubuntu AMIs, in conjunction with the Amazon EFS Mount Helper.


- CORRECT "Amazon EFS" is the correct answer.


- INCORRECT "Amazon S3" is incorrect. Amazon S3 is an object storage system that is accessed via REST API not file-level

  protocols. It cannot be attached to EC2 instances.


- INCORRECT "Amazon EC2 instance store" is incorrect. An EC2 instance store is an ephemeral storage volume that is local

  to the server on which the instances runs and is not persistent. It is accessed via block protocols and also cannot be

  shared between instances.


- INCORRECT "Amazon EBS" is incorrect. An Amazon Elastic Block Store (EBS) volume can only be attached to a single

  instance and cannot be shared.


**References:**


https://docs.aws.amazon.com/efs/latest/ug/how-it-works.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-efs/

