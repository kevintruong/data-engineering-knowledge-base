#### Question  45


**A company has over 2000 users and is planning to migrate data into the AWS Cloud. Some of the data is user’s home

folders on an existing file share and the plan is to move this data to Amazon S3. Each user will have a folder in a

shared bucket under the folder structure:** **_bucket_** **/home/%username%.**


**What steps should a Solutions Architect take to ensure that each user can access their own home folder and no one

else’s? (Select TWO)**


- [ ] Create a bucket policy that applies access permissions based on username


- [x] Create an IAM policy that applies folder-level permissions


- [ ] Create an IAM policy that applies object-level S3 ACLs


- [ ] Attach an S3 ACL sub-resource that grants access based on the %username% variable


- [x] Create an IAM group and attach the IAM policy, add IAM users to the group


*