#### Question  28


**There is new requirement for a database that will store a large number of records for an online store. You are

evaluating the use of DynamoDB. Which of the following are AWS best practices for DynamoDB? (Select TWO)**


1: Use separate local secondary indexes for each item


2: Store objects larger than 400KB in S3 and use pointers in DynamoDB


3: Store more frequently and less frequently accessed data in separate tables


4: Use for BLOB data use cases


5: Use large files


**Answer: 2,3**


**Explanation:**


DynamoDB best practices include:


- Keep item sizes small.

- If you are storing serial data in DynamoDB that will require actions based on data/time use separate tables for days,

  weeks, months.

- Store more frequently and less frequently accessed data in separate tables.

- If possible compress larger attribute values.



- Store objects larger than 400KB in S3 and use pointers (S3 Object ID) in DynamoDB.


- CORRECT "Store objects larger than 400KB in S3 and use pointers in DynamoDB" is the correct answer.


- CORRECT "Store more frequently and less frequently accessed data in separate tables" is the correct answer.


- INCORRECT "Use separate local secondary indexes for each item" is incorrect as this is not a best practice.


- INCORRECT "Use for BLOB data use cases" is incorrect as this is not a best practice.


- INCORRECT "Use large files" is incorrect as this is not a best practice.


**References:**


https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/best-practices.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-

dynamodb/

