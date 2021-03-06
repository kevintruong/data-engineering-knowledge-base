**Explanation:**

Some applications, such as media catalog updates require high frequency reads, and consistent throughput. For such

applications, customers often complement S3 with an in-memory cache, such as Amazon ElastiCache for Redis, to reduce the

S3 retrieval cost and to improve performance.

ElastiCache for Redis is a fully managed, in-memory data store that provides sub-millisecond latency performance with

high throughput. ElastiCache for Redis complements S3 in the following ways:

- Redis stores data in-memory, so it provides sub-millisecond latency and supports incredibly high requests per second.

- It supports key/value based operations that map well to S3 operations (for example, GET/SET =>

  GET/PUT), making it easy to write code for both S3 and ElastiCache.

- It can be implemented as an application side cache. This allows you to use S3 as your persistent store and benefit

  from its durability, availability, and low cost. Your applications decide what objects to cache, when to cache them,

  and how to cache them.

In this example the media catalog is pulling updates from S3 so the performance between these components is what needs

to be improved. Therefore, using ElastiCache to cache the content will dramatically increase the performance.

- ✅ :  "Update the application code to use an Amazon ElastiCache for Redis cluster" is the correct answer.

- ❌ :  "Implement Amazon CloudFront and cache the content at Edge Locations" is incorrect. CloudFront is good for

  getting media closer to users but in this case we’re trying to improve performance within the data center moving data

  from S3 to the media catalog server.

- ❌ :  "Update the application code to use an Amazon DynamoDB Accelerator cluster" is incorrect. DynamoDB

  Accelerator (DAX) is used with DynamoDB but is unsuitable for use with Amazon S3.

- ❌ :  "Implement an Instance store volume on the media catalog server" is incorrect. This will improve local disk

  performance but will not improve reads from Amazon S3.

**References:**

<https://aws.amazon.com/blogs/storage/turbocharge-amazon-s3-with-amazon-elasticache-for-redis/>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon>- elasticache/

----

- #<https://aws.amazon.com/blogs/storage/turbocharge-amazon-s3-with-amazon-elasticache-for-redis/> #amazon_elasticache #redis_stores_data #amazon_s3 #redis_complements_s3
