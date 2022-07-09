#### Question  44


**A Solutions Architect needs to upload a large (2GB) file to an S3 bucket. What is the recommended way to upload a

single large file to an S3 bucket?**


1: Use AWS Import/Export


2: Use Multipart Upload


3: Use a single PUT request to upload the large file


4: Use Amazon Snowball


**Answer: 2**


**Explanation:**


In general, when your object size reaches 100 MB, you should consider using multipart uploads instead of uploading the

object in a single operation.


- CORRECT "Use Multipart Upload" is the correct answer.


- INCORRECT "Use AWS Import/Export" is incorrect. AWS Import/Export is a service in which you send in HDDs with data on

  to AWS and they import your data into S3. It is not used for single files.


- INCORRECT "Use a single PUT request to upload the large file" is incorrect. The largest object that can be uploaded in

  a single PUT is 5 gigabytes.


- INCORRECT "Use Amazon Snowball" is incorrect. Snowball is used for migrating large quantities (TB/PB) of data into

  AWS, it is overkill for this requirement.


**References:**


https://docs.aws.amazon.com/AmazonS3/latest/dev/uploadobjusingmpu.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/

