**Explanation:**

The most cost-effective solution is to first store the data in S3 Standard-IA where it will be infrequently accessed for

the first three months. Then, after three months expires, transition the data to S3 Glacier where it can be stored at

lower cost for the remainder of the seven year period. Expedited retrieval can bring retrieval times down to 1-5

minutes.

- ✅ :  "Store the data in S3 Standard-IA for 3 months, then transition to S3 Glacier" is the correct answer.

- ❌ :  "Store the data in S3 Standard for 3 months, then transition to S3 Glacier" is incorrect. S3 Standard is

  more costly than S3 Standard-IA and the data is only accessed infrequently.

- ❌ :  "Store the data in S3 Standard for 3 months, then transition to S3 Standard-IA" is incorrect. Neither

  storage class in this answer is the most cost-effective option.

- ❌ :  "Store the data in S3 Intelligent Tiering for 3 months, then transition to S3 Standard-IA" is incorrect.

  Intelligent tiering moves data between tiers based on access patterns, this is more costly and better suited to use

  cases that are unknown or unpredictable.

**References:**

<https://aws.amazon.com/s3/storage-classes/>

<https://docs.aws.amazon.com/amazonglacier/latest/dev/downloading-an-archive-two-steps.html#api>-

downloading-an-archive-two-steps-retrieval-options

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/>

----

- #s3_glacier #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/> #<https://aws.amazon.com/s3/storage-classes/> #s3_standard #s3_intelligent
