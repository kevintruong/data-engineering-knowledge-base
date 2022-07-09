#### Question  38


**An application stores encrypted data in Amazon S3 buckets. A Solutions Architect needs to be able to query the

encrypted data using SQL queries and write the encrypted results back the S3 bucket. As the data is sensitive

fine-grained control must be implemented over access to the S3 bucket.**


**What combination of services represent the BEST options support these requirements? (Select TWO)**


1: Use AWS Glue to extract the data, analyze it, and load it back to the S3 bucket


2: Use bucket ACLs to restrict access to the bucket


3: Use IAM policies to restrict access to the bucket


4: Use Athena for querying the data and writing the results back to the bucket


5: Use the AWS KMS API to query the encrypted data, and the S3 API for writing the results


**Answer: 3,4**


**Explanation:**


Athena allows you to easily query encrypted data stored in Amazon S3 and write encrypted results back to your S3 bucket.

Both, server-side encryption and client-side encryption are supported.


AWS IAM policies can be used to grant IAM users with fine-grained control to Amazon S3 buckets.


- CORRECT "Use IAM policies to restrict access to the bucket" is a correct answer.


- CORRECT "Use Athena for querying the data and writing the results back to the bucket" is also a correct answer.


- INCORRECT "Use AWS Glue to extract the data, analyze it, and load it back to the S3 bucket" is incorrect. AWS Glue is

  an ETL service and is not used for querying and analyzing data in S3.


- INCORRECT "Use bucket ACLs to restrict access to the bucket" is incorrect. With IAM policies, you can grant IAM users

  fine-grained control to your S3 buckets and is preferable to using bucket ACLs.


- INCORRECT "Use the AWS KMS API to query the encrypted data, and the S3 API for writing the results" is incorrect. The

  AWS KMS API can be used for encryption purposes; however it cannot perform analytics so is not suitable.


**References:**


https://aws.amazon.com/athena/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/security-identity-

compliance/aws-iam/

