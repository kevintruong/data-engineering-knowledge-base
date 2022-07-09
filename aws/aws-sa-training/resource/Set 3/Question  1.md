#### Question  1


**A security officer requires that access to company financial reports is logged. The reports are stored in an Amazon S3

bucket. Additionally, any modifications to the log files must be detected.**


**Which actions should a solutions architect take?**


1: Use S3 server access logging on the bucket that houses the reports with the read and write data events and the log

file validation options enabled


2: Use S3 server access logging on the bucket that houses the reports with the read and write management events and log

file validation options enabled


3: Use AWS CloudTrail to create a new trail. Configure the trail to log read and write data events on the S3 bucket that

houses the reports. Log these events to a new bucket, and enable log file validation


4: Use AWS CloudTrail to create a new trail. Configure the trail to log read and write management events on the S3

bucket that houses the reports. Log these events to a new bucket, and enable log file validation


Answer: 3


**Explanation:**


Amazon CloudTrail can be used to log activity on the reports. The key difference between the two answers that include

CloudTrail is that one references data events whereas the other references management events.


Data events provide visibility into the resource operations performed on or within a resource. These are also known as

data plane operations. Data events are often high-volume activities.


Example data events include:


- Amazon S3 object-level API activity (for example, GetObject, DeleteObject, and PutObject API operations).

- AWS Lambda function execution activity (the Invoke API).


Management events provide visibility into management operations that are performed on resources in your AWS account.

These are also known as control plane operations. Example management events include:


- Configuring security (for example, IAM AttachRolePolicy API operations)

- Registering devices (for example, Amazon EC2 CreateDefaultVpc API operations).


Therefore, to log data about access to the S3 objects the solutions architect should log read and write data events.


Log file validation can also be enabled on the destination bucket:


- CORRECT "Use AWS CloudTrail to create a new trail. Configure the trail to log read and write data events on the S3

  bucket that houses the reports. Log these events to a new bucket, and enable log file validation" is the correct

  answer.


- INCORRECT "Use AWS CloudTrail to create a new trail. Configure the trail to log read and write management events on

  the S3 bucket that houses the reports. Log these events to a new bucket, and enable log file validation" is incorrect

  as data events should be logged rather than management events.


- INCORRECT "Use S3 server access logging on the bucket that houses the reports with the read and write data events and

  the log file validation options enabled" is incorrect as server access logging does not have an option for choosing

  data events or log file validation.


- INCORRECT "Use S3 server access logging on the bucket that houses the reports with the read and write management

  events and log file validation options enabled" is incorrect as server access logging does not have an option for

  choosing management events or log file validation.


**References:**


https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/management-tools/aws-

cloudtrail/

