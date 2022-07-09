#### Question  1


**A company is deploying an Amazon ElastiCache for Redis cluster. To enhance security a password should be required to

access the database. What should the solutions architect use?**


1: AWS Directory Service


2: AWS IAM Policy


3: Redis AUTH command


4: VPC Security Group


Answer: 3


**Explanation:**


Redis authentication tokens enable Redis to require a token (password) before allowing clients to execute commands,

thereby improving data security.


You can require that users enter a token on a token-protected Redis server. To do this, include the parameter -


- auth-token (API: AuthToken) with the correct token when you create your replication group or cluster. Also include it

  in all subsequent commands to the replication group or cluster.


- CORRECT "Redis AUTH command" is the correct answer.


- INCORRECT "AWS Directory Service" is incorrect. This is a managed Microsoft Active Directory service and cannot add

  password protection to Redis.


- INCORRECT "AWS IAM Policy" is incorrect. You cannot use an IAM policy to enforce a password on Redis.


- INCORRECT "VPC Security Group" is incorrect. A security group protects at the network layer, it does not affect

  application authentication.


**References:**


https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/auth.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-

elasticache/

