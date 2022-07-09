#### Question  12


**A company is planning a migration for a high performance computing (HPC) application and associated data from an

on-premises data center to the AWS Cloud. The company uses tiered storage on premises with hot high-performance parallel

storage to support the application during periodic runs of the application, and more economical cold storage to hold the

data when the application is not actively running.**


**Which combination of solutions should a solutions architect recommend to support the storage needs of the

application? (Select TWO)**


1: Amazon S3 for cold data storage


2: Amazon EFS for cold data storage


3: Amazon S3 for high-performance parallel storage


```

EC 2 Instance

(Windows)

```


```

EC 2 Instance

(Windows)

```


```

Region

```


```

VPC

```


```

Corporate data center

```


```

On-premises

client (Windows)

```


```

VPN or Direct

Connect connection

```


```

Availability Zone

```


```

Availability Zone

```


```

Amazon FSx

```


```

AWS Managed

Microsoft AD

```


```

Public subnet

```


```

Public subnet

```


```

With multi-AZ a

standby can be

created in another

AZ

```


4: Amazon FSx for Lustre for high-performance parallel storage


5: Amazon FSx for Windows for high-performance parallel storage


Answer: 1,4


**Explanation:**


Amazon FSx for Lustre provides a high-performance file system optimized for fast processing of workloads such as machine

learning, high performance computing (HPC), video processing, financial modeling, and electronic design automation (EDA)

.


These workloads commonly require data to be presented via a fast and scalable file system interface, and typically have

data sets stored on long-term data stores like Amazon S3.


Amazon FSx works natively with Amazon S3, making it easy to access your S3 data to run data processing workloads. Your

S3 objects are presented as files in your file system, and you can write your results back to S3. This lets you run data

processing workloads on FSx for Lustre and store your long-term data on S3 or on- premises data stores.


Therefore, the best combination for this scenario is to use S3 for cold data and FSx for Lustre for the parallel HPC

job.


- CORRECT "Amazon S3 for cold data storage" is the correct answer.


- CORRECT "Amazon FSx for Lustre for high-performance parallel storage" is the correct answer.


- INCORRECT "Amazon EFS for cold data storage" is incorrect as FSx works natively with S3 which is also more economical.


- INCORRECT "Amazon S3 for high-performance parallel storage" is incorrect as S3 is not suitable for running

  high-performance computing jobs.


- INCORRECT "Amazon FSx for Windows for high-performance parallel storage" is incorrect as FSx for Lustre should be used

  for HPC use cases and use cases that require storing data on S3.


**References:**


https://aws.amazon.com/fsx/lustre/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-fsx/

