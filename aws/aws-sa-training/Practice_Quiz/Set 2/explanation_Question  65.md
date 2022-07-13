**Explanation:**

ElastiCache can be deployed in the U.S east region to provide high-speed access to the content. ElastiCache Redis has a

good use case for autocompletion (see links below).

- ✅ :  "Create an ElastiCache database in the U.S east region" is the correct answer.

- ❌ :  "Host the static content in an Amazon S3 bucket and distribute it using CloudFront" is incorrect. This is

  not static content that can be hosted in an Amazon S3 bucket and distributed using CloudFront.

- ❌ :  "Setup cross-region replication and use Route 53 geolocation routing" is incorrect. Cross-region replication

  is an Amazon S3 concept and the dynamic data that is presented by this application is unlikely to be stored in an S3

  bucket.

- ❌ :  "Create a DynamoDB Read Replica in the U.S east region" is incorrect. There’s no such thing as a DynamoDB

  Read Replica (Read Replicas are an RDS concept).

**References:**

<https://aws.amazon.com/blogs/database/creating-a-simple-autocompletion-service-with-redis-part-one-of>- two/

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon>- elasticache/

----

- #amazon_s3_concept #cross_-_region_replication #<https://aws.amazon.com/blogs/database/creating-a-simple-autocompletion-service-with-redis-part-one-of>-_two/> #elasticache_database #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon>>-
