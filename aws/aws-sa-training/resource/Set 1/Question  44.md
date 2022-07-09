#### Question  44


A company needs to store data for 5 years. The company will need to have immediate and highly available access to the

data at any point in time but will not require frequent access.


Which lifecycle action should be taken to meet the requirements while reducing costs?


1: Transition objects from Amazon S3 Standard to the GLACIER storage class


2: Transition objects to expire after 5 years


3: Transition objects from Amazon S3 Standard to Amazon S3 Standard-Infrequent Access (S3 Standard-IA)


4: Transition objects from Amazon S3 Standard to Amazon S3 One Zone-Infrequent Access (S3 One Zone-IA)


Answer: 3


**Explanation:**


This is a good use case for S3 Standard-IA which provides immediate access and 99.9% availability.


- CORRECT "Transition objects from Amazon S3 Standard to Amazon S3 Standard-Infrequent Access (S3 Standard-IA)" is the

  correct answer.


- INCORRECT "Transition objects from Amazon S3 Standard to the GLACIER storage class" is incorrect. The Glacier storage

  class does not provide immediate access. You can retrieve within hours or minutes, but you do need to submit a job to

  retrieve the data.


- INCORRECT "Transition objects to expire after 5 years" is incorrect. Expiring the objects after 5 years is going to

  delete them at the end of the 5-year period, but you still need to work out the best storage solution to use before

  then, and this answer does not provide a solution.


- INCORRECT "Transition objects from Amazon S3 Standard to Amazon S3 One Zone-Infrequent Access (S3 One Zone-IA)" is

  incorrect. The S3 One Zone-IA tier provides immediate access, but the availability is lower at 99.5% so this is not

  the best option.


**References:**


https://aws.amazon.com/s3/storage-classes/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/

