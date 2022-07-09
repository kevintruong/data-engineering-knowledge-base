#### Question  39


**A client has requested a design for a fault tolerant database that can failover between AZs. You have decided to use

RDS in a multi-AZ configuration. What type of replication will the primary database use to replicate to the standby

instance?**


1: Continuous replication


2: Asynchronous replication


3: Scheduled replication


4: Synchronous replication


**Answer: 4**


**Explanation:**


Multi-AZ RDS creates a replica in another AZ and synchronously replicates to it (DR only). Multi-AZ deployments for the

MySQL, MariaDB, Oracle and PostgreSQL engines utilize synchronous physical replication. Multi-AZ deployments for the SQL

Server engine use synchronous logical replication (SQL Server-native Mirroring technology).


```

AWS Storage Gateway

```


```

S 3 Standard

```


```

S 3 Standard IA

```


```

S 3 One Zone IA

```


```

Corporate AWS Cloud

data center

```


```

Server

```


```

The file system is

mounted using NFS

or SMB Can store data in

multiple S 3 storage

classes

```


```

Files are stored as objects

in S 3 , a local cache

provides low latency access

to recently used data

```


```

Virtual gateway appliance

runs on Hyper-V,

VMware, or EC 2

```


- CORRECT "Synchronous replication" is the correct answer.


- INCORRECT "Continuous replication" is incorrect. Continuous replication is not a replication type that is supported by

  RDS.


- INCORRECT "Asynchronous replication" is incorrect. Asynchronous replication is used by RDS for Read Replicas.


- INCORRECT "Scheduled replication" is incorrect. Scheduled replication is not a replication type that is supported by

  RDS.


**References:**


https://aws.amazon.com/rds/features/multi-az/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-rds/

