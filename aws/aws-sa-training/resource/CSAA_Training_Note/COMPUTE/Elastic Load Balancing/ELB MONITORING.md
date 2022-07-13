#### ELB MONITORING


Monitoring takes place using:


- **CloudWatch – every 1 minute**

  o ELB service only sends information when requests are active. o Can be used to trigger SNS notifications.

- **Access Logs**

  o Disabled by default. o Includes information about the clients (not included in CloudWatch metrics). o Can identify

  requester, IP, request type etc. o Can be optionally stored and retained in S3.



- **CloudTrail**

  o Can be used to capture API calls to the ELB. o Can be stored in an S3 bucket.

