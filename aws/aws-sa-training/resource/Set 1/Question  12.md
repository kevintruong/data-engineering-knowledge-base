#### Question  12


**A solutions architect is creating a document submission application for a school. The application will use an Amazon

S3 bucket for storage. The solution must prevent accidental deletion of the documents and ensure that all versions of

the documents are available. Users must be able to upload and modify the documents.**


**Which combination of actions should be taken to meet these requirements? (Select TWO)**


1: Set read-only permissions on the bucket


2: Enable versioning on the bucket


3: Attach an IAM policy to the bucket


4: Enable MFA Delete on the bucket


5: Encrypt the bucket using AWS SSE-S3


Answer: 2, 4


**Explanation:**


None of the options present a good solution for specifying permissions required to write and modify objects so that

requirement needs to be taken care of separately. The other requirements are to prevent accidental deletion and the

ensure that all versions of the document are available.


The two solutions for these requirements are versioning and MFA delete. Versioning will retain a copy of each version of

the document and multi-factor authentication delete (MFA delete) will prevent any accidental deletion as you need to

supply a second factor when attempting a delete.


- CORRECT "Enable versioning on the bucket" is a correct answer.


- CORRECT "Enable MFA Delete on the bucket" is also a correct answer.


- INCORRECT "Set read-only permissions on the bucket" is incorrect as this will also prevent any writing to the bucket

  which is not desired.


- INCORRECT "Attach an IAM policy to the bucket" is incorrect as users need to modify documents which will also allow

  delete. Therefore, a method must be implemented to just control deletes.


- INCORRECT "Encrypt the bucket using AWS SSE-S3" is incorrect as encryption doesn’t stop you from deleting an object.


**References:**


https://docs.aws.amazon.com/AmazonS3/latest/dev/Versioning.html


https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMFADelete.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/

