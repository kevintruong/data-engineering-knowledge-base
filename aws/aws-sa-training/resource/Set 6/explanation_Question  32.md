*

**Explanation:**

You can control who can administer your file system using IAM. You can control access to files and directories with

POSIX-compliant user and group-level permissions. POSIX permissions allows you to restrict access from hosts by user and

group. EFS Security Groups act as a firewall, and the rules you add define the traffic flow.

* ✅ :  "Use POSIX permissions to control access from hosts by user or group" is the correct answer.

* ✅ :  "Use EFS Security Groups to control network traffic" is the correct answer.

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

* ❌ :  "Use AWS Web Application Firewall (WAF) to protect EFS" is incorrect. You cannot use AWS WAF to protect EFS

  data using users and groups.

* ❌ :  "Use Network ACLs to control the traffic" is incorrect. You use EFS Security Groups to control network

  traffic to EFS, not Network ACLs.

* ❌ :  "Use IAM groups to control access by user or group" is incorrect. You do not use IAM to control access to

  files and directories by user and group, but you can use IAM to control who can administer the file system

  configuration.

**References:**

<https://aws.amazon.com/efs/features/>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-efs/>

----
* #aws_web_application_firewall #aws_cloud #efs_security_groups #aws #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-efs/>
