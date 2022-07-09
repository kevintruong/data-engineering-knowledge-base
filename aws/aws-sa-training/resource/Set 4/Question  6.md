#### Question  6


**An application is being monitored using Amazon GuardDuty. A Solutions Architect needs to be notified by email of

medium to high severity events. How can this be achieved?**


1: Configure an Amazon CloudWatch alarm that triggers based on a GuardDuty metric


2: Create an Amazon CloudWatch events rule that triggers an Amazon SNS topic


3: Create an Amazon CloudWatch Logs rule that triggers an AWS Lambda function


4: Configure an Amazon CloudTrail alarm the triggers based on GuardDuty API activity


Answer: 2


**Explanation:**


A CloudWatch Events rule can be used to set up automatic email notifications for Medium to High Severity findings to the

email address of your choice. You simply create an Amazon SNS topic and then associate it with an Amazon CloudWatch

events rule.


Note: step by step procedures for how to set this up can be found in the article linked in the references below.


```

Redshift Leader Node

```


```

Compute node Compute^ node Compute^ node

```


```

Availability Zone

```


```

Leader coordinates

query execution

```


```

SQL Client / BI Tools

JDBC/ODBC

```


```

Compute nodes

execute queries

```


```

Ingestion, backup, restore on Amazon S 3

```


```

Region A

```


```

Region B

```


```

Snapshot

```


```

Cross-region

snapshots

```


```

Snapshot

```


- CORRECT "Create an Amazon CloudWatch events rule that triggers an Amazon SNS topic" is the correct answer.


- INCORRECT "Configure an Amazon CloudWatch alarm that triggers based on a GuardDuty metric" is incorrect. There is no

  metric for GuardDuty that can be used for specific findings.


- INCORRECT "Create an Amazon CloudWatch Logs rule that triggers an AWS Lambda function" is incorrect. CloudWatch logs

  is not the right CloudWatch service to use. CloudWatch events is used for reacting to changes in service state.


- INCORRECT "Configure an Amazon CloudTrail alarm the triggers based on GuardDuty API activity" is incorrect. CloudTrail

  cannot be used to trigger alarms based on GuardDuty API activity.


**References:**


https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_findings_cloudwatch.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/management-

tools/amazon-cloudwatch/

