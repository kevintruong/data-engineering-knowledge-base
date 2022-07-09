#### Question  44


**The security team in your company is defining new policies for enabling security analysis, resource change tracking,

and compliance auditing. They would like to gain visibility into user activity by recording API calls made within the

company’s AWS account. The information that is logged must be encrypted. This requirement applies to all AWS regions in

which your company has services running.**


**How will you implement this request? (Select TWO)**


1: Create a CloudTrail trail in each region in which you have services


2: Enable encryption with a single KMS key


3: Create a CloudTrail trail and apply it to all regions


4: Enable encryption with multiple KMS keys


5: Use CloudWatch to monitor API calls


Answer: 2,3


**Explanation:**


CloudTrail is used for recording API calls (auditing) whereas CloudWatch is used for recording metrics

(performance monitoring). The solution can be deployed with a single trail that is applied to all regions. A single KMS

key can be used to encrypt log files for trails applied to all regions. CloudTrail log files are encrypted using S3

Server Side Encryption (SSE) and you can also enable encryption SSE KMS for additional security.


- CORRECT "Enable encryption with a single KMS key" is the correct answer.


- CORRECT "Create a CloudTrail trail and apply it to all regions" is the correct answer.


- INCORRECT "Create a CloudTrail trail in each region in which you have services" is incorrect. You do not need to

  create a separate trail in each region.


- INCORRECT "Enable encryption with multiple KMS keys" is incorrect. You do not need to use multiple KMS keys.


- INCORRECT "Use CloudWatch to monitor API calls" is incorrect. CloudWatch is not used for monitoring API calls (use

  CloudTrail).


**References:**


https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-

regions.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/management-tools/aws-

cloudtrail/

