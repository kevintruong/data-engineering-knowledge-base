#### Question  61


**An application will gather data from a website hosted on an EC2 instance and write the data to an S3 bucket. The

application will use API calls to interact with the EC2 instance and S3 bucket.**


**Which Amazon S3 access control method will be the MOST operationally efficient? (Select TWO)**


1: Create a bucket policy


2: Grant programmatic access


3: Use key pairs


4: Grant AWS Management Console access


5: Create an IAM policy


**Answer: 2,5**


**Explanation:**


Policies are documents that define permissions and can be applied to users, groups and roles. Policy documents are

written in JSON (key value pair that consists of an attribute and a value).


Within an IAM policy you can grant either programmatic access or AWS Management Console access to Amazon S3 resources.


- CORRECT "Grant programmatic access" is a correct answer.


- CORRECT "Create an IAM policy" is also a correct answer.


- INCORRECT "Create a bucket policy" is incorrect as it is more efficient to use an IAM policy.


- INCORRECT "Use key pairs" is incorrect. Key pairs are used for access to EC2 instances; a bucket policy would not

  assist with access control with EC2 and granting management console access will not assist the application which is

  making API calls to the services.


- INCORRECT "Grant AWS Management Console access" is incorrect as programmatic access is required.


**References:**


https://aws.amazon.com/blogs/security/writing-iam-policies-how-to-grant-access-to-an-amazon-s3-bucket/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/security-identity-

compliance/aws-iam/


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/

