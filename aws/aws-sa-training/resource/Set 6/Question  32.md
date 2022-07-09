#### Question  32


**An Amazon Elastic File System (EFS) has been created to store data that will be accessed by a large number of Amazon

EC2 instances. The data is sensitive and a Solutions Architect is creating a design for security measures to protect the

data. It is required that network traffic is restricted correctly based on firewall rules and access from hosts is

restricted by user or group.**


**How can this be achieved with Amazon EFS? (Select TWO)**


1: Use POSIX permissions to control access from hosts by user or group


2: Use AWS Web Application Firewall (WAF) to protect EFS


3: Use EFS Security Groups to control network traffic


4: Use Network ACLs to control the traffic


5: Use IAM groups to control access by user or group


**Answer: 1,3**


**Explanation:**


You can control who can administer your file system using IAM. You can control access to files and directories with

POSIX-compliant user and group-level permissions. POSIX permissions allows you to restrict access from hosts by user and

group. EFS Security Groups act as a firewall, and the rules you add define the traffic flow.


- CORRECT "Use POSIX permissions to control access from hosts by user or group" is the correct answer.


- CORRECT "Use EFS Security Groups to control network traffic" is the correct answer.


```

VPC

```


```

Private subnet

```


```

Public subnet

```


```

Customer Router

```


```

VPN gateway

```


```

Corporate data center

AWS Direct Connect location

```


```

AWS Cloud

```


```

Amazon Simple Storage

```


Amazon EC (^2) Service (S 3 )

AWS cage Customer / partner cage AWS Direct Connect endpoint Customer / Public VIF partner router Private VIF Region


- INCORRECT "Use AWS Web Application Firewall (WAF) to protect EFS" is incorrect. You cannot use AWS WAF to protect EFS

  data using users and groups.


- INCORRECT "Use Network ACLs to control the traffic" is incorrect. You use EFS Security Groups to control network

  traffic to EFS, not Network ACLs.


- INCORRECT "Use IAM groups to control access by user or group" is incorrect. You do not use IAM to control access to

  files and directories by user and group, but you can use IAM to control who can administer the file system

  configuration.


**References:**


https://aws.amazon.com/efs/features/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-efs/

