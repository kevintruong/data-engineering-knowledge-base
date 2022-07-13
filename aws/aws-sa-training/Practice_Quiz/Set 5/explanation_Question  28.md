*

**Explanation:**

DynamoDB best practices include:

* Keep item sizes small.

* If you are storing serial data in DynamoDB that will require actions based on data/time use separate tables for days,

  weeks, months.

* Store more frequently and less frequently accessed data in separate tables.

* If possible compress larger attribute values.

* Store objects larger than 400KB in S3 and use pointers (S3 Object ID) in DynamoDB.

* ✅ :  "Store objects larger than 400KB in S3 and use pointers in DynamoDB" is the correct answer.

* ✅ :  "Store more frequently and less frequently accessed data in separate tables" is the correct answer.

* ❌ :  "Use separate local secondary indexes for each item" is incorrect as this is not a best practice.

* ❌ :  "Use for BLOB data use cases" is incorrect as this is not a best practice.

* ❌ :  "Use large files" is incorrect as this is not a best practice.

**References:**

<https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/best-practices.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon>- dynamodb/

----
* #dynamodb #<https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/best-practices.html> #blob_data_use_cases #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon>>- #store_objects
