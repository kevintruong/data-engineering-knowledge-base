**Explanation:**

Service control policies (SCPs) offer central control over the maximum available permissions for all accounts in your

organization, allowing you to ensure your accounts stay within your organization’s access control guidelines.

```

AWS Organizations

```

```

Account A

```

```

Organizational unit 1 Organizational unit 2 Organizational unit 3

```

```

Account B Account C Account D

```

```

Service

Control Policy

(SCP)

```

```

Tag Policy

```

```

Tag Policies enforce

rules around tagging

across accounts and

OUs

```

```

SCPs define the AWS

service actions that

are available for use

```

SCPs alone are not sufficient for allowing access in the accounts in your organization. Attaching an SCP to an AWS

Organizations entity (root, OU, or account) defines a guardrail for what actions the principals can perform. You still

need to attach identity-based or resource-based policies to principals or resources in your organization's accounts to

actually grant permissions to them.

- ✅ :  "Create a service control policy in the root organizational unit to deny access to the services or actions"

  is the correct answer.

- ❌ :  "Create an ACL to provide access to the services or actions" is incorrect as access control lists are not

  used for permissions associated with IAM. Permissions policies are used with IAM.

- ❌ :  "Create a security group to allow accounts and attach it to user groups" is incorrect as security groups are

  instance level firewalls. They do not limit service actions.

- ❌ :  "Create cross-account roles in each account to deny access to the services or actions" is incorrect as this

  is a complex solution and does not provide centralized control

**References:**

<https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scp.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/management-tools/aws>-

organizations/

----

- #<https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scp.html> #aws_organizations #service_control_policies #service_control_policy #permissions_policies
