**Explanation:**

```

Availability Zone Availability Zone Availability Zone

```

```

Primary

```

```

Data Copies Data Copies Data Copies

```

```

Replica Replica Replica

```

```

Reads Writes Writes Writes

```

```

Reads Reads Reads

```

```

Region

```

```

Single Logical Volume

```

```

Aurora Fault Tolerance

```

- Fault tolerance across 3 AZs

- Single logical volume

- Aurora Replicas scale-out read requests

- Up to 15 Aurora Replicas with sub- 10 ms replica lag

- Aurora Replicas are independent endpoints

- Can promote Aurora Replica to be a new primary or create new primary

- Set priority (tiers) on Aurora Replicas to control order of promotion

- Can use Auto Scaling to add replicas

Amazon CloudFront caches content closer to users at Edge locations around the world. This is the lowest latency option

for uploading content. API Gateway and AWS Lambda are present in all options. DynamoDB can be used for storing session

state data. This is a 100% serverless application.

- ✅ :  "Amazon CloudFront, API Gateway, Amazon S3, AWS Lambda, DynamoDB" is the correct answer.

- ❌ :  "Amazon CloudFront, API Gateway, Amazon S3, AWS Lambda, Amazon RDS" is incorrect. Amazon RDS is not a

  serverless service so this option can be ruled out.

- ❌ :  "Amazon S3, API Gateway, AWS Lambda, Amazon RDS" is incorrect. Amazon S3 alone will not provide the least

  latency for users around the world unless you have many buckets in different regions and a way of directing users to

  the closest bucket (such as Route 3 latency based routing). However, you would then need to manage replicating the

  data.

- ❌ :  "API Gateway, Amazon S3, AWS Lambda, DynamoDB" is incorrect. This answer does not offer a front-end for

  users to upload content to.

**References:**

<https://aws.amazon.com/blogs/aws/amazon-cloudfront-content-uploads-post-put-other-methods/>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content>-

delivery/amazon-cloudfront/

----

- #aws_lambda #dynamodb #aurora_fault_tolerance #aurora_replica #aurora_replicas
