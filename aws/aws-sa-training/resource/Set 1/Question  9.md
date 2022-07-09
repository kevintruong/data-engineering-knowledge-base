#### Question  9


**A solutions architect needs to backup some application log files from an online ecommerce store to Amazon S3. It is

unknown how often the logs will be accessed or which logs will be accessed the most. The solutions architect must keep

costs as low as possible by using the appropriate S3 storage class.**


**Which S3 storage class should be implemented to meet these requirements?**


1: S3 Glacier


2: S3 Intelligent-Tiering


3: S3 Standard-Infrequent Access (S3 Standard-IA)


4: S3 One Zone-Infrequent Access (S3 One Zone-IA)


Answer: 2


**Explanation:**


The S3 Intelligent-Tiering storage class is designed to optimize costs by automatically moving data to the most

cost-effective access tier, without performance impact or operational overhead.


It works by storing objects in two access tiers: one tier that is optimized for frequent access and another lower-cost

tier that is optimized for infrequent access. This is an ideal use case for intelligent-tiering as the access patterns

for the log files are not known.


- CORRECT "S3 Intelligent-Tiering" is the correct answer.


- INCORRECT "S3 Standard-Infrequent Access (S3 Standard-IA)" is incorrect as if the data is accessed often retrieval

  fees could become expensive.


- INCORRECT "S3 One Zone-Infrequent Access (S3 One Zone-IA)" is incorrect as if the data is accessed often retrieval

  fees could become expensive.


- INCORRECT "S3 Glacier" is incorrect as if the data is accessed often retrieval fees could become expensive. Glacier

  also requires more work in retrieving the data from the archive and quick access requirements can add further costs.


**References:**


https://aws.amazon.com/s3/storage-classes/#Unknown_or_changing_access


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/

