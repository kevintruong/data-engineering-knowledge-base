#### Question  24


**An application requires a MySQL database which will only be used several times a week for short periods. The database

needs to provide automatic instantiation and scaling. Which database service is most suitable?**


1: Amazon RDS MySQL


2: Amazon EC2 instance with MySQL database installed


3: Amazon Aurora


4: Amazon Aurora Serverless


Answer: 4


**Explanation:**


Amazon Aurora Serverless is an on-demand, auto-scaling configuration for Amazon Aurora. The database automatically

starts up, shuts down, and scales capacity up or down based on application needs. This is an ideal database solution for

infrequently-used applications.


- CORRECT "Amazon Aurora Serverless" is the correct answer.


```

EC 2 Instance

```


```

EC 2 Instance

```


```

Corporate data center

On-premises

client

VPN or Direct

Connect connection

```


```

Availability Zone

```


```

Availability Zone

Public subnet

```


```

Public subnet

```


```

S 3 objects can be

viewed as files in FSx;

result data can be

S 3 Bucket written back to S 3

```


```

Amazon FSxfor Lustre

```


```

Use for cloud

bursting and data

migration

```


```

Region

```


- INCORRECT "Amazon RDS MySQL" is incorrect as this service requires an instance to be running all the time which is

  more costly.


- INCORRECT "Amazon EC2 instance with MySQL database installed" is incorrect as this service requires an instance to be

  running all the time which is more costly.


- INCORRECT "Amazon Aurora" is incorrect as this service requires an instance to be running all the time which is more

  costly.


**References:**


https://aws.amazon.com/rds/aurora/serverless/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-aurora/

