**Explanation:**

Service control policies (SCPs) offer central control over the maximum available permissions for all accounts in your

organization, allowing you to ensure your accounts stay within your organization’s access control guidelines.

In the example below a policy in OU1 restricts all users from launching EC2 instance types other than a t2.micro:

- ✅ :  "Create a service control policy in the root organizational unit to deny access to the services or actions"

  is the correct answer.

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

Account B

```

```

Effect: Allow

Action: EC 2 RunInstances

Resource: ec 2 *

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

```

Organizational unit 2

```

- ❌ :  "Create a Network ACL that limits access to the services or actions and attach it to all relevant subnets"

  is incorrect. Network ACLs control network traffic not API actions.

- ❌ :  "Create an IAM policy in the root account and attach it to users and groups in each account" is incorrect.

  This is not an efficient or centrally managed method of applying the security restrictions.

- ❌ :  "Create cross-account roles in each account to limit access to the services and actions that are allowed"

  is incorrect. This is another example of a complex and inefficient method of providing access across accounts and does

  not restrict API actions within the account.

**References:**

<https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_about-scps.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/security-identity>-

compliance/aws-accounts/

----

- #service_control_policies #service_control_policy #ec2_instance_types #control_policy #aws
