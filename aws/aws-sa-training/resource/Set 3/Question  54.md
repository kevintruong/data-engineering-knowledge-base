#### Question  54


**A company is generating large datasets with millions of rows that must be summarized by column. Existing business

intelligence tools will be used to build daily reports.**


**Which storage service meets the requirements?**


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


1: Amazon DynamoDB


2: Amazon RDS


3: Amazon RedShift


4: Amazon ElastiCache


Answer: 3


**Explanation:**


Amazon Redshift is a fast, fully managed, petabyte-scale data warehouse service that makes it simple and cost- effective

to efficiently analyze all your data using your existing business intelligence tools. It is optimized for datasets

ranging from a few hundred gigabytes to a petabyte or more. Amazon RedShift uses columnar storage.


- CORRECT "Amazon RedShift" is the correct answer.


- INCORRECT "Amazon DynamoDB" is incorrect. Amazon DynamoDB is a fully managed NoSQL database service, it is not a

  columnar database.


- INCORRECT "Amazon RDS" is incorrect. Amazon RDS is more suited to OLTP workloads rather than analytics workloads.


- INCORRECT "Amazon ElastiCache" is incorrect. Amazon ElastiCache is an in-memory caching service.


**References:**


https://docs.aws.amazon.com/redshift/index.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-

redshift/

