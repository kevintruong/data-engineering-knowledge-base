#### SIMPLE AD

An inexpensive Active Directory-compatible service with common directory
features.

Standalone, fully managed, directory on the AWS cloud.

Simple AD is generally the least expensive option.

Best choice for less than 5000 users and doesn’t need advanced AD features.

Powered by SAMBA 4 Active Directory compatible server.

Can create users and control access to applications on AWS.

Provides a subset of the features provided by AWS MS AD.

**Features include:**

- Manage user accounts.

- Manage groups.

- Apply group policies.

- Securely connect to EC2 instances.

- Kerberos-based SSO.

- Supports joining Linux or Windows based EC2 instances.

AWS provides monitoring, daily snapshots, and recovery services.

Manual snapshots possible.

Simple AD is compatible with WorkSpaces, WorkDocs, Workmail and QuickSight.

You can also sign on to the AWS management console with Simple AD user accounts
to manage AWS resources.

**Available in two editions:**

- Small – supports up to 500 users (approximately 2000 objects).

- Large – supports up to 5000 users (approximately 20,000 objects).

AWS creates two directory servers and DNS servers on two different subnets
within an AZ.

**Simple AD does not support:**

- DNS dynamic updates.

- Schema extensions.

- Multi-factor authentication.


- Communication over LDAPS.

- PowerShell AD cmdlets.

- FSMO role transfer.

Not compatible with RDS SQL server.

Does not support trust relationships with other domains (use AWS MS AD).

