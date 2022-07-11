**Explanation:**

Amazon ElastiCache in-transit encryption is an optional feature that allows you to increase the security of your data at

its most vulnerable points—when it is in transit from one location to another. Because there is some processing needed

to encrypt and decrypt the data at the endpoints, enabling in-transit encryption can have some performance impact. You

should benchmark your data with and without in-transit encryption to determine the performance impact for your use

cases.

ElastiCache in-transit encryption implements the following features:

- **Encrypted connections** —both the server and client connections are Secure Socket Layer (SSL) encrypted.

- **Encrypted replication—** data moving between a primary node and replica nodes is encrypted.

- **Server authentication** —clients can authenticate that they are connecting to the right server.

- **Client authentication** —using the Redis AUTH feature, the server can authenticate the clients.

- ✅ :  "Enable in-transit encryption" is the correct answer.

- ❌ :  "Issue a Redis AUTH command" is incorrect. This is used when using a password to access the database.

- ❌ :  "Enable at-rest encryption" is incorrect. ElastiCache for Redis at-rest encryption is an optional feature to

  increase data security by encrypting on-disk data. This does not encrypt the data in-transit when it is being

  replicated between nodes.

- ❌ :  "Set up MFA and API logging" is incorrect. Neither multi-factor authentication or API logging is going to

  assist with encrypting data.

**References:**

<https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/at-rest-encryption.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon>- elasticache/

----

- #<https://docs.aws.amazon.com/amazonelasticache/latest/red-ug/at-rest-encryption.html> #amazon_elasticache #transit_encryption #rest_encryption #elasticache
