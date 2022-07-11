**Explanation:**

Redis authentication tokens enable Redis to require a token (password) before allowing clients to execute commands,

thereby improving data security.

You can require that users enter a token on a token-protected Redis server. To do this, include the parameter -

- auth-token (API: AuthToken) with the correct token when you create your replication group or cluster. Also include it

  in all subsequent commands to the replication group or cluster.

- ✅ :  "Redis AUTH command" is the correct answer.

- ❌ :  "AWS Directory Service" is incorrect. This is a managed Microsoft Active Directory service and cannot add

  password protection to Redis.

- ❌ :  "AWS IAM Policy" is incorrect. You cannot use an IAM policy to enforce a password on Redis.

- ❌ :  "VPC Security Group" is incorrect. A security group protects at the network layer, it does not affect

  application authentication.

**References:**

<https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/auth.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon>- elasticache/

----

- #redis_authentication_tokens #<https://docs.aws.amazon.com/amazonelasticache/latest/red-ug/auth.html> #redis_server #redis #aws_iam_policy
