**Explanation:**

In this case the data is frequently accessed so must be stored in standard for the first 90 days. After that the data is

still to be kept for compliance reasons but is rarely accessed so is a good use case for DEEP_ARCHIVE.

- ✅ :  "Store data in STANDARD for 90 days then transition the data to DEEP_ARCHIVE" is the correct answer.

- ❌ :  "Store data in INTELLIGENT_TIERING for 90 days then transition to STANDARD_IA" is incorrect. You cannot

  transition from INTELLIGENT_TIERING to STANDARD_IA.

- ❌ :  "Store data in STANDARD for 90 days then expire the data" is incorrect. Expiring the data is not possible as

  it must be retained for compliance.

- ❌ :  "Store data in STANDARD for 90 days then transition to REDUCED_REDUNDANCY" is incorrect. You cannot

  transition from any storage class to REDUCED_REDUNDANCY.

**References:**

<https://docs.aws.amazon.com/AmazonS3/latest/dev/lifecycle-transition-general-considerations.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/>

----

- #<https://docs.aws.amazon.com/amazons3/latest/dev/lifecycle-transition-general-considerations.html> #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/> #store_data #standard_ia #storage_class
