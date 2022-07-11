### AWS CloudTrail


AWS CloudTrail is a web service that records activity made on your account


A CloudTrail trail can be created which delivers log files to an Amazon S3 bucket.


CloudWatch vs CloudTrail:


CloudTrail is about logging and saves a history of API calls for your AWS account.


Provides visibility into user activity by recording actions taken on your account.


API history enables security analysis, resource change tracking, and compliance auditing.


**Logs API calls made via:**


- AWS Management Console.

- AWS SDKs.

- Command line tools.

- Higher-level AWS services (such as CloudFormation).


**CloudTrail records account activity and service events from most AWS services and logs the following records:**


- The identity of the API caller.

- The time of the API call.

- The source IP address of the API caller.

- The request parameters.

- The response elements returned by the AWS service.


CloudTrail is per AWS account.


Trails can be enabled per region or a trail can be applied to all regions.


**Trails can be configured to log data events and management events:**


- **Data events:** These events provide insight into the resource operations performed on or within a resource. These

  are also known as data plane operations.

- **Management events:** Management events provide insight into management operations that are performed on resources in

  your AWS account. These are also known as control plane operations. Management events can also include non-API events

  that occur in your account.


CloudTrail log files are encrypted using S3 Server Side Encryption (SSE).


You can also enable encryption using SSE KMS for additional security.


A single KMS key can be used to encrypt log files for trails applied to all regions.


**You can consolidate logs from multiple accounts using an S3 bucket:**


1. Turn on CloudTrail in the paying account.

2. Create a bucket policy that allows cross-account access.

3. Turn on CloudTrail in the other accounts and use the bucket in the paying account.


You can integrate CloudTrail with CloudWatch Logs to deliver data events captured by CloudTrail to a CloudWatch Logs log

stream.


CloudTrail log file integrity validation feature allows you to determine whether a CloudTrail log file was unchanged,

deleted, or modified since CloudTrail delivered it to the specified Amazon S3 bucket.

