**Explanation:**

Amazon CloudFront can be used to cache the files in edge locations around the world and this will improve the

performance of the webpages.

```

Producers capture and

send data to Kinesis

```

```

Shards

```

```

Stream Consumers (EC 2 ) Amazon^ S^3

Amazon DynamoDB

```

```

Amazon RedShift

```

```

Amazon EMR

Kinesis Firehose

```

```

Destinations

```

```

Data is captured and

stored for processing

```

```

Analytics Tools

```

To serve a static website hosted on Amazon S3, you can deploy a CloudFront distribution using one of these

configurations:

- Using a REST API endpoint as the origin with access restricted by an origin access identity (OAI)

- Using a website endpoint as the origin with anonymous (public) access allowed

- Using a website endpoint as the origin with access restricted by a Referer header

- ✅ :  "Use Amazon CloudFront with the S3 bucket as its origin" is the correct answer.

- ❌ :  "Generate presigned URLs for the files" is incorrect as this is used to restrict access which is not a

  requirement.

- ❌ :  "Use cross-Region replication to all Regions" is incorrect as this does not provide a mechanism for

  directing users to the closest copy of the static webpages.

- ❌ :  "Use the geoproximity feature of Amazon Route 53" is incorrect as this does not include a solution for

  having multiple copies of the data in different geographic lcoations.

**References:**

<https://aws.amazon.com/premiumsupport/knowledge-center/cloudfront-serve-static-website/>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content>-

delivery/amazon-cloudfront/

----

- #amazon_cloudfront #cloudfront_distribution #amazon_dynamodb #amazon_s3 #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content>>-
