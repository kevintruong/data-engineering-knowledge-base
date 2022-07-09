#### Question  31


**An AWS Organization has an OU with multiple member accounts in it. The company needs to restrict the ability to launch

only specific Amazon EC2 instance types. How can this policy be applied across the accounts with the least effort?**


1: Create an SCP with an allow rule that allows launching the specific instance types


2: Create an SCP with a deny rule that denies all but the specific instance types


3: Create an IAM policy to deny launching all but the specific instance types


4: Use AWS Resource Access Manager to control which launch types can be used


Answer: 2


**Explanation:**


To apply the restrictions across multiple member accounts you must use a Service Control Policy (SCP) in the AWS

Organization. The way you would do this is to create a deny rule that applies to anything that does not equal the

specific instance type you want to allow.


The following architecture could be used to achieve this goal:


- CORRECT "Create an SCP with a deny rule that denies all but the specific instance types" is the correct answer.


- INCORRECT "Create an SCP with an allow rule that allows launching the specific instance types" is incorrect as a deny

  rule is required.


- INCORRECT "Create an IAM policy to deny launching all but the specific instance types" is incorrect. With IAM you need

  to apply the policy within each account rather than centrally so this would require much more effort.


- INCORRECT "Use AWS Resource Access Manager to control which launch types can be used" is incorrect. AWS Resource

  Access Manager (RAM) is a service that enables you to easily and securely share AWS resources with any AWS account or

  within your AWS Organization. It is not used for restricting access or permissions.


**References:**


https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_example-

scps.html#example-ec2-instances


**Save time with our exam-specific cheat sheets:**


```

Root

```


```

Organizational unit 1

```


```

Account A

```


```

Service

Control Policy

(SCP)

```


```

Effect: Deny

Action: EC 2 RunInstances

Resource: ec 2 *

StringNotEquals

EC 2 InstanceType: t 2 .micro

```


```

Service

Control Policy

(SCP)

```


```

Master Account

```


```

{

"Version": " 2012 - 10 - 17 ",

“Statement": [

{

“Effect": "Allow",

"Action": "*",

"Resource": "*"

}

]

}

```


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/management-tools/aws-

organizations/

