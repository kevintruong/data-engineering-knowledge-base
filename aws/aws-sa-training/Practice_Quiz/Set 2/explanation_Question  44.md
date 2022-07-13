**Explanation:**

CloudTrail is used for recording API calls (auditing) whereas CloudWatch is used for recording metrics

(performance monitoring). The solution can be deployed with a single trail that is applied to all regions. A single KMS

key can be used to encrypt log files for trails applied to all regions. CloudTrail log files are encrypted using S3

Server Side Encryption (SSE) and you can also enable encryption SSE KMS for additional security.

- ✅ :  "Enable encryption with a single KMS key" is the correct answer.

- ✅ :  "Create a CloudTrail trail and apply it to all regions" is the correct answer.

- ❌ :  "Create a CloudTrail trail in each region in which you have services" is incorrect. You do not need to

  create a separate trail in each region.

- ❌ :  "Enable encryption with multiple KMS keys" is incorrect. You do not need to use multiple KMS keys.

- ❌ :  "Use CloudWatch to monitor API calls" is incorrect. CloudWatch is not used for monitoring API calls (use

  CloudTrail).

**References:**

<https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple>- regions.html

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/management-tools/aws>-

cloudtrail/

----

- #cloudwatch #<https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple>-_regions.html> #cloudtrail_trail #encryption_sse_kms #cloudtrail
