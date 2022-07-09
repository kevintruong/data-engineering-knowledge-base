#### Question  48


**A company needs to capture detailed information about all HTTP requests that are processed by their Internet facing

Application Load Balancer (ALB). The company requires information on the requester, IP address, and request type for

analyzing traffic patterns to better understand their customer base.**


**Which actions should a Solutions Architect recommend?**


1: Configure metrics in CloudWatch for the ALB


2: Enable EC2 detailed monitoring


3: Enable Access Logs and store the data on S3


4: Use CloudTrail to capture all API calls made to the ALB


**Answer: 3**


**Explanation:**


You can enable access logs on the ALB and this will provide the information required including requester, IP, and

request type. Access logs are not enabled by default. You can optionally store and retain the log files on S3.


- CORRECT "Enable Access Logs and store the data on S3" is the correct answer.


- INCORRECT "Configure metrics in CloudWatch for the ALB" is incorrect. CloudWatch is used for performance monitoring

  and CloudTrail is used for auditing API access.


- INCORRECT "Enable EC2 detailed monitoring" is incorrect. Enabling EC2 detailed monitoring will not capture the

  information requested.


- INCORRECT Use CloudTrail to capture all API calls made to the ALB"" is incorrect. CloudTrail captures API activity and

  would not include the requested information.


**References:**


https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/elastic-load-

balancing/

