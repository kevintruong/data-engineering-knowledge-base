#### Question  1

**A security officer requires that access to company financial reports is logged. The reports are stored in an Amazon S3

bucket. Additionally, any modifications to the log files must be detected.**

**Which actions should a solutions architect take?**

- [ ] :  Use S3 server access logging on the bucket that houses the reports with the read and write data events and the log

file validation options enabled

- [ ] :  Use S3 server access logging on the bucket that houses the reports with the read and write management events and log

file validation options enabled

- [x] :  Use AWS CloudTrail to create a new trail. Configure the trail to log read and write data events on the S3 bucket that

houses the reports. Log these events to a new bucket, and enable log file validation

- [ ] :  Use AWS CloudTrail to create a new trail. Configure the trail to log read and write management events on the S3

bucket that houses the reports. Log these events to a new bucket, and enable log file validation

----

- #aws_cloudtrail #amazon_s3 #use_s3_server_access #s3_bucket #log_files
- hasExplain:: [[explanation_Question  1.md]]
