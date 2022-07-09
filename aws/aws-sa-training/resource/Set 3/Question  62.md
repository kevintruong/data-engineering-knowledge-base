#### Question  62


**A company runs a service on AWS to provide offsite backups for images on laptops and phones. The solution must support

millions of customers, with thousands of images per customer. Images will be retrieved infrequently but must be

available for retrieval immediately.**


**Which is the MOST cost-effective storage option that meets these requirements?**


1: Amazon Glacier with expedited retrievals


2: Amazon S3 Standard-Infrequent Access


3: Amazon EFS


4: Amazon S3 Standard


Answer: 2


**Explanation:**


S3 Standard-IA is for data that is accessed less frequently, but requires rapid access when needed. S3 Standard-IA

offers the high durability, high throughput, and low latency of S3 Standard, with a low per GB storage price and per GB

retrieval fee.


This combination of low cost and high performance make S3 Standard-IA ideal for long-term storage, backups, and as a

data store for disaster recovery files. S3 Storage Classes can be configured at the object level and a single bucket can

contain objects stored across S3 Standard, S3 Intelligent-Tiering, S3 Standard-IA, and S3 One Zone-IA.


You can also use S3 Lifecycle policies to automatically transition objects between storage classes without any

application changes.


Amazon S3 Standard-Infrequent Access is the most cost-effective choice.


- CORRECT "Amazon S3 Standard-Infrequent Access" is the correct answer.


- INCORRECT "Amazon Glacier with expedited retrievals" is incorrect. Amazon Glacier with expedited retrievals is fast (

  1-5 minutes) but not immediate.


- INCORRECT "Amazon EFS" is incorrect. Amazon EFS is a high-performance file system and not ideally suited to this

  scenario, it is also not the most cost-effective option.


- INCORRECT "Amazon S3 Standard" is incorrect. Amazon S3 Standard provides immediate retrieval but is not less

  cost-effective compared to Standard-Infrequent access.


**References:**


https://aws.amazon.com/s3/storage-classes/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/

