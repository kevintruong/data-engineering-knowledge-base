#### Question  19


**The database layer of an on-premises web application is being migrated to AWS. The database uses a multi- threaded,

in-memory caching layer to improve performance for repeated queries. Which service would be the most suitable

replacement for the database cache?**


1: Amazon ElastiCache Redis


2: Amazon DynamoDB DAX


3: Amazon ElastiCache Memcached


4: Amazon RDS MySQL


Answer: 3


**Explanation:**


Amazon ElastiCache with the Memcached engine is an in-memory database that can be used as a database caching layer. The

memached engine supports multiple cores and threads and large nodes.


```

Data center

```


```

NFS or SMB

```


```

DataSyncsoftware

agent connects to

storage system

```


```

Scheduled, automated data

transfer with TLS encryption

```


```

NAS / File

Server AWS DataSync Amazon^ FSxfor^ Windows^ File^

Server

```


```

Amazon Simple Storage

Service

```


```

Amazon Elastic File System

```


```

Permissions

and metadata

are preserved

```


- CORRECT "Amazon ElastiCache Memcached" is the correct answer.


- INCORRECT "Amazon ElastiCache Redis" is incorrect. The Redis engine does not support multiple CPU cores or threads.


- INCORRECT "Amazon DynamoDB DAX" is incorrect. Amazon DynamoDB Accelerator (DAX) is a database cache that should be

  used with DynamoDB only.


- INCORRECT "Amazon RDS MySQL" is incorrect as this is not an example of an in-memory database that can be used as a

  database caching layer.


**References:**


https://aws.amazon.com/elasticache/redis-vs-memcached/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-

elasticache/

