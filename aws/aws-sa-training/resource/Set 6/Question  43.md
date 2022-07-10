#### Question  43


**A company runs a web-based application that uses Amazon EC2 instances for the web front-end and Amazon RDS for the

database back-end. The web application writes transaction log files to an Amazon S3**


**bucket and the quantity of files is becoming quite large. It is acceptable to retain the most recent 60 days of log

files and permanently delete the rest.**


**Which action can a Solutions Architect take to enable this to happen automatically?**


- [x] Use an S3 lifecycle policy with object expiration configured to automatically remove objects that are more than 60

days old


- [ ] Write a Ruby script that checks the age of objects and deletes any that are more than 60 days old


- [ ] Use an S3 bucket policy that deletes objects that are more than 60 days old


- [ ] Use an S3 lifecycle policy to move the log files that are more than 60 days old to the GLACIER storage class


*

- hasExplain:: [[explanation_Question  43.md]]