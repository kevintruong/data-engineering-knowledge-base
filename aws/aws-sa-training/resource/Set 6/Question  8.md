#### Question  8


```

Region

```


```

VPC

```


```

Availability Zone

Public subnet

```


```

Internet

gateway

```


```

Private subnet

```


```

Internet Client

HTTP, HTTPS

Availability Zone

Private subnet

```


```

Application

Load

Balancer

```


```

Auto Scaling

group

```


```

NAT gateway

```


```

Public subnet

```


**A company runs an application on premises that stores a large quantity of semi-structured data using key- value pairs.

The application code will be migrated to AWS Lambda and a highly scalable solution is required for storing the data.**


**Which datastore will be the best fit for these requirements?**


1: Amazon EFS


2: Amazon RDS MySQL


3: Amazon EBS


4: Amazon DynamoDB


Answer: 4


**Explanation:**


Amazon DynamoDB is a no-SQL database that stores data using key-value pairs. It is ideal for storing large amounts of

semi-structured data and is also highly scalable. This is the best solution for storing this data based on the

requirements in the scenario.


- CORRECT "Amazon DynamoDB" is the correct answer.


- INCORRECT "Amazon EFS" is incorrect. The Amazon Elastic File System (EFS) is not suitable for storing key- value

  pairs.


- INCORRECT "Amazon RDS MySQL" is incorrect. Amazon Relational Database Service (RDS) is used for structured data as it

  is an SQL type of database.


- INCORRECT "Amazon EBS" is incorrect. Amazon Elastic Block Store (EBS) is a block-based storage system. You attach

  volumes to EC2 instances. It is not used for key-value pairs or to be used by Lambda functions.


**References:**


https://aws.amazon.com/dynamodb/features/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-

dynamodb/

