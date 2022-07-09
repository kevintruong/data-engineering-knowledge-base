#### Question  45


**A company has over 2000 users and is planning to migrate data into the AWS Cloud. Some of the data is user’s home

folders on an existing file share and the plan is to move this data to Amazon S3. Each user will have a folder in a

shared bucket under the folder structure:** **_bucket_** **/home/%username%.**


**What steps should a Solutions Architect take to ensure that each user can access their own home folder and no one

else’s? (Select TWO)**


1: Create a bucket policy that applies access permissions based on username


2: Create an IAM policy that applies folder-level permissions


3: Create an IAM policy that applies object-level S3 ACLs


4: Attach an S3 ACL sub-resource that grants access based on the %username% variable


5: Create an IAM group and attach the IAM policy, add IAM users to the group


**Answer: 2,5**


**Explanation:**


The AWS blog URL below explains how to construct an IAM policy for a similar scenario. Please refer to the article for

detailed instructions.


- CORRECT "Create an IAM policy that applies folder-level permissions" is a correct answer.


- CORRECT "Create an IAM group and attach the IAM policy, add IAM users to the group" is also a correct answer.


- INCORRECT "Create a bucket policy that applies access permissions based on username" is incorrect. An IAM policy

  rather than a bucket policy should be used.


- INCORRECT "Create an IAM policy that applies object-level S3 ACLs" is incorrect as this cannot be done through an IAM

  policy.


- INCORRECT "Attach an S3 ACL sub-resource that grants access based on the %username% variable" is incorrect as an IAM

  policy should be used to control access.


**References:**


https://aws.amazon.com/blogs/security/writing-iam-policies-grant-access-to-user-specific-folders-in-an-

amazon-s3-bucket/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/security-identity-

compliance/aws-iam/

