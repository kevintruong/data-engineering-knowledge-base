#### Question  65


**An application is hosted on the U.S west coast. Users there have no problems, but users on the east coast are

experiencing performance issues. The users have reported slow response times with the search bar autocomplete and

display of account listings.**


**How can you improve the performance for users on the east coast?**


1: Host the static content in an Amazon S3 bucket and distribute it using CloudFront


2: Setup cross-region replication and use Route 53 geolocation routing


3: Create a DynamoDB Read Replica in the U.S east region


4: Create an ElastiCache database in the U.S east region


Answer: 4


**Explanation:**


ElastiCache can be deployed in the U.S east region to provide high-speed access to the content. ElastiCache Redis has a

good use case for autocompletion (see links below).


- CORRECT "Create an ElastiCache database in the U.S east region" is the correct answer.


- INCORRECT "Host the static content in an Amazon S3 bucket and distribute it using CloudFront" is incorrect. This is

  not static content that can be hosted in an Amazon S3 bucket and distributed using CloudFront.


- INCORRECT "Setup cross-region replication and use Route 53 geolocation routing" is incorrect. Cross-region replication

  is an Amazon S3 concept and the dynamic data that is presented by this application is unlikely to be stored in an S3

  bucket.


- INCORRECT "Create a DynamoDB Read Replica in the U.S east region" is incorrect. There’s no such thing as a DynamoDB

  Read Replica (Read Replicas are an RDS concept).


**References:**


https://aws.amazon.com/blogs/database/creating-a-simple-autocompletion-service-with-redis-part-one-of-

two/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-

elasticache/

