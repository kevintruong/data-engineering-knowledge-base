#### Question  8


**A HR application stores employment records on Amazon S3. Regulations mandate the records are retained for seven years.

Once created the records are accessed infrequently for the first three months and then must be available within 10

minutes if required thereafter.**


**Which lifecycle action meets the requirements whilst MINIMIZING cost?**


1: Store the data in S3 Standard for 3 months, then transition to S3 Glacier


2: Store the data in S3 Standard-IA for 3 months, then transition to S3 Glacier


3: Store the data in S3 Standard for 3 months, then transition to S3 Standard-IA


4: Store the data in S3 Intelligent Tiering for 3 months, then transition to S3 Standard-IA


Answer: 2


**Explanation:**


The most cost-effective solution is to first store the data in S3 Standard-IA where it will be infrequently accessed for

the first three months. Then, after three months expires, transition the data to S3 Glacier where it can be stored at

lower cost for the remainder of the seven year period. Expedited retrieval can bring retrieval times down to 1-5

minutes.


- CORRECT "Store the data in S3 Standard-IA for 3 months, then transition to S3 Glacier" is the correct answer.


- INCORRECT "Store the data in S3 Standard for 3 months, then transition to S3 Glacier" is incorrect. S3 Standard is

  more costly than S3 Standard-IA and the data is only accessed infrequently.


- INCORRECT "Store the data in S3 Standard for 3 months, then transition to S3 Standard-IA" is incorrect. Neither

  storage class in this answer is the most cost-effective option.


- INCORRECT "Store the data in S3 Intelligent Tiering for 3 months, then transition to S3 Standard-IA" is incorrect.

  Intelligent tiering moves data between tiers based on access patterns, this is more costly and better suited to use

  cases that are unknown or unpredictable.


**References:**


https://aws.amazon.com/s3/storage-classes/


https://docs.aws.amazon.com/amazonglacier/latest/dev/downloading-an-archive-two-steps.html#api-

downloading-an-archive-two-steps-retrieval-options


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/

