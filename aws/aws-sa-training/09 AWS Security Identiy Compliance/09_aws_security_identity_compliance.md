
## AWS SECURITY, IDENTITY & COMPLIANCE

### AWS IAM

**GENERAL IAM CONCEPTS**

IAM is used to securely control individual and group access to AWS resources.

IAM makes it easy to provide multiple users secure access to AWS resources.

**IAM can be used to manage:**

- Users
- Groups
- Access policies
- Roles
- User credentials
- User password policies
- Multi-factor authentication (MFA)
- API keys for programmatic access (CLI)

Provides centralized control of your AWS account.

Enables shared access to your AWS account.

By default, new users are created with NO access to any AWS services – they can only login to the
AWS console.

Permission must be explicitly granted to allow a user to access an AWS service.

IAM users are individuals who have been granted access to an AWS account.

**Each IAM user has three main components:**

- A user-name
- A password
- Permissions to access various resources

You can apply granular permissions with IAM.

You can assign users individual security credentials such as access keys, passwords, and multi-factor
authentication devices.

IAM is not used for application-level authentication.

Identity Federation (including AD, Facebook etc.) can be configured allowing secure access to
resources in an AWS account without creating an IAM user account.

Multi-factor authentication (MFA) can be enabled/enforced for the AWS account and for individual
users under the account.

MFA uses an authentication device that continually generates random, six-digit, single-use
authentication codes.


**You can authenticate using an MFA device in the following three ways:**

- Through the **AWS Management Console** – the user is prompted for a user name, password
    and authentication code.
- Using the **AWS API** – restrictions are added to IAM policies and developers can request
    temporary security credentials and pass MFA parameters in their AWS STS API requests.
- Using the **AWS CLI** by obtaining temporary security credentials from STS (aws sts get-
    session-token).

It is a best practice to use MFA for all users and to use U2F or hardware MFA devices for all
privileged users.

IAM is universal (global) and does not apply to regions.

IAM is eventually consistent.

IAM replicates data across multiple data centers around the world.

The “root account” is the account created when you setup the AWS account. It has complete Admin
access and is the only account that has this access by default.

It is a best practice to not use the root account for anything other than billing.

Power user access allows all permissions except the management of groups and users in IAM.

Temporary security credentials consist of the AWS access key ID, secret access key, and security
token.

IAM can assign temporary security credentials to provide users with temporary access to
services/resources.

To sign-in you must provide your account ID or account alias in addition to a user name and
password.

The sign-in URL includes the account ID or account alias, e.g.:

https:// **_My_AWS_Account_ID_** .signin.aws.amazon.com/console/.

Alternatively, you can sign-in at the following URL and enter your account ID or alias manually:

https://console.aws.amazon.com/.

IAM integrates with many different AWS services.

IAM supports PCI DSS compliance.

AWS recommend that you use the AWS SDKs to make programmatic API calls to IAM.

However, you can also use the IAM Query API to make direct calls to the IAM web service.


**IAM INFRASTRUCTURE ELEMENTS**

**Principals:**

- An entity that can take an action on an AWS resource.
- Your administrative IAM user is your first principal.
- You can allow users and services to assume a role.
- IAM supports federated users.
- IAM supports programmatic access to allow an application to access your AWS account.
- IAM users, roles, federated users, and applications are all AWS principals

**Requests:**

- Principals send requests via the Console, CLI, SDKs, or APIs.
Requests are:
- Actions (or operations) that the principal wants to perform.
- Resources upon which the actions are performed.
- Principal information including the environment from which the request was made.

**Request context - AWS gathers the request information:**

- Principal (requester).
- Aggregate permissions associated with the principal.


- Environment data, such as IP address, user agent, SSL status etc.
- Resource data, or data that is related to the resource being requested.

**Authentication:**

- A principal sending a request must be authenticated to send a request to AWS.
- To authenticate from the console, you must sign in with your user name and password.
- To authenticate from the API or CLI, you must provide your access key and secret key.

**Authorization:**

- IAM uses values from the request context to check for matching policies and determines
    whether to allow or deny the request.
- IAM policies are stored in IAM as JSON documents and specify the permissions that are
    allowed or denied.
- IAM policies can be:
    o User (identity) based policies
    o Resource-based policies
- IAM checks each policy that matches the context of your request.
- If a single policy has a deny action IAM denies the request and stops evaluating (explicit
    deny).
- **Evaluation logic:**
    o By default, all requests are denied (implicit deny).
    o An explicit allow overrides the implicit deny.
    o An explicit deny overrides any explicit allows.
- Only the root user has access to all resources in the account by default.

**Actions:**

- Actions are defined by a service.
- Actions are the things you can do to a resource such as viewing, creating, editing, deleting.
- Any actions on resources that are not explicitly allowed are denied.
- To allow a principal to perform an action you must include the necessary actions in a policy
    that applies to the principal or the affected resource.

**Resources:**

- A resource is an entity that exists within a service.
- E.g. EC2 instances, S3 buckets, IAM users, and DynamoDB tables.
- Each AWS service defines a set of actions that can be performed on the resource.
- After AWS approves the actions in your request, those actions can be performed on the
    related resources within your account.

**AUTHENTICATION METHODS**

**Console password:**

- A password that the user can enter to sign into interactive sessions such as the AWS
    Management Console.
- You can allow users to change their own passwords.
- You can allow selected IAM users to change their passwords by disabling the option for all


```
users and using an IAM policy to grant permissions for the selected users.
```
**Access Keys:**

- A combination of an access key ID and a secret access key.
- You can assign two active access keys to a user at a time.
- These can be used to make programmatic calls to AWS when using the **API** in program code
    or at a command prompt when using the **AWS CLI** or the **AWS PowerShell** tools.
- You can create, modify, view or rotate access keys.
- When created IAM returns the access key ID and secret access key.
- The secret access is returned only at creation time and if lost a new key must be created.
- Ensure access keys and secret access keys are stored securely.
- Users can be given access to change their own keys through IAM policy (not from the
    console).
- You can disable a user’s access key which prevents it from being used for API calls.

**Server certificates:**

- SSL/TLS certificates that you can use to authenticate with some AWS services.
- AWS recommends that you use the AWS Certificate Manager (ACM) to provision, manage
    and deploy your server certificates.
- Use IAM only when you must support HTTPS connections in a region that is not supported
    by ACM.

The following diagram shows the different methods of authentication available with IAM:

**IAM USERS**

An IAM user is an entity that represents a person or service.

**Can be assigned:**

- An access key ID and secret access key for programmatic access to the AWS API, CLI, SDK,
    and other development tools.
- A password for access to the management console.

By default, users cannot access anything in your account.


The account root user credentials are the email address used to create the account and a password.

The root account has full administrative permissions, and these cannot be restricted.

**Best practice for root accounts:**

- Don’t use the root user credentials.
- Don’t share the root user credentials.
- Create an IAM user and assign administrative permissions as required.
- Enable MFA.

IAM users can be created to represent applications and these are known as “service accounts”.

You can have up to 5000 users per AWS account.

Each user account has a friendly name and an ARN which uniquely identifies the user across AWS.

A unique ID is also created which is returned only when you create the user using the API, Tools for
Windows PowerShell or the AWS CLI.

You should create individual IAM accounts for users (best practice not to share accounts).

The Access Key ID and Secret Access Key are not the same as a password and cannot be used to
login to the AWS console.

The Access Key ID and Secret Access Key can only be generated once and must be regenerated if
lost.

A password policy can be defined for enforcing password length, complexity etc. (applies to all
users).

You can allow or disallow the ability to change passwords using an IAM policy.

Access keys and passwords should be changed regularly.

**GROUPS**

Groups are collections of users and have policies attached to them.

A group is not an identity and cannot be identified as a principal in an IAM policy.

Use groups to assign permissions to users.

Use the principal of least privilege when assigning permissions.

You cannot nest groups (groups within groups).

**ROLES**

Roles are created and then “assumed” by trusted entities and define a set of permissions for
making AWS service requests.

With IAM Roles you can delegate permissions to resources for users and services without using
permanent credentials (e.g. user name and password).

IAM users or AWS services can assume a role to obtain temporary security credentials that can be
used to make AWS API calls.


You can delegate using roles.

There are no credentials associated with a role (password or access keys).

IAM users can temporarily assume a role to take on permissions for a specific task.

A role can be assigned to a federated user who signs in using an external identity provider.

Temporary credentials are primarily used with IAM roles and automatically expire.

Roles can be assumed temporarily through the console or programmatically with the **AWS CLI** ,
**Tools for Windows PowerShell** or **API.**

**IAM roles with EC2 instances:**

- IAM roles can be used for granting applications running on EC2 instances permissions to
    AWS API requests using instance profiles.
- Only one role can be assigned to an EC2 instance at a time.
- A role can be assigned at the **EC2 instance creation time or at any time afterwards**.
- When using the AWS CLI or API instance profiles must be created manually (it’s automatic
    and transparent through the console).
- Applications retrieve temporary security credentials from the instance metadata.

**Role Delegation:**

- Create an IAM role with two policies:
    o Permissions policy – grants the user of the role the required permissions on a resource.
    o Trust policy – specifies the trusted accounts that are allowed to assume the role.
- Wildcards (*) cannot be specified as a principal.
- A permissions policy must also be attached to the user in the trusted account.

**POLICIES**

Policies are documents that define permissions and can be applied to users, groups and roles.

Policy documents are written in JSON (key value pair that consists of an attribute and a value).

All permissions are implicitly denied by default.

The most restrictive policy is applied.

The IAM policy simulator is a tool to help you understand, test, and validate the effects of access
control policies.

The Condition element can be used to apply further conditional logic.

The diagram below provides some more information on the relationship between IAM roles, users,
groups and policies.


**SECURITY TOKEN SERVICE (STS)**

The AWS Security Token Service (STS) is a web service that enables you to request temporary,
limited-privilege credentials for IAM users or for users that you authenticate (federated users).

By default, AWS STS is available as a global service, and all AWS STS requests go to a single endpoint
at https://sts.amazonaws.com

You can optionally send your AWS STS requests to endpoints in any region (can reduce latency).

All regions are enabled for STS by default but can be disabled.

The region in which temporary credentials are requested must be enabled.

Credentials will always work globally.

STS supports AWS CloudTrail, which records AWS calls for your AWS account and delivers log files to
an S3 bucket.

**Temporary security credentials work almost identically to long-term access key credentials that
IAM users can use, with the following differences:**

- Temporary security credentials are short-term.
- They can be configured to last anywhere from a few minutes to several hours.
- After the credentials expire, AWS no longer recognizes them or allows any kind of access to
    API requests made with them.
- Temporary security credentials are not stored with the user but are generated dynamically
    and provided to the user when requested.
- When (or even before) the temporary security credentials expire, the user can request new
    credentials, as long as the user requesting them still has permission to do so.

**Advantages of STS are:**

- You do not have to distribute or embed long-term AWS security credentials with an
    application.
- You can provide access to your AWS resources to users without having to define an AWS
    identity for them (temporary security credentials are the basis for IAM Roles and ID
    Federation).
- The temporary security credentials have a limited lifetime, so you do not have to rotate
    them or explicitly revoke them when they’re no longer needed.


- After temporary security credentials expire, they cannot be reused (you can specify how
    long the credentials are valid for, up to a maximum limit).

**The AWS STS API action returns temporary security credentials that consist of:**

- An access key which consists of an access key ID and a secret ID.
- A session token.
- Expiration or duration of validity.
- Users (or an application that the user runs) can use these credentials to access your
    resources.

**With STS you can request a session token using one of the following APIs:**

- AssumeRole – can only be used by IAM users (can be used for MFA).
- AssumeRoleWithSAML – can be used by any user who passes a SAML authentication
    response that indicates authentication from a known (trusted) identity provider.
- AssumeRoleWithWebIdentity – can be used by a user who passes a web identity token that
    indicates authentication from a known (trusted) identity provider.
- GetSessionToken – can be used by an IAM user or AWS account root user (can be used for
    MFA).
- GetFederationToken – can be used by an IAM user or AWS account root user.

AWS recommends using Cognito for identity federation with Internet identity providers.

**Users can come from three sources:**

**Federation (typically AD):**

- Uses SAML 2.0.
- Grants temporary access based on the users AD credentials.
- Does not need to be a user in IAM.
- Single sign-on allows users to login to the AWS console without assigning IAM credentials.

**Federation with Mobile Apps:**

- Use Facebook/Amazon/Google or other OpenID providers to login.

**Cross Account Access:**

- Lets users from one AWS account access resources in another.
- To make a request in a different account the resource in that account must have an
    attached resource-based policy with the permissions you need.
- Or you must assume a role (identity-based policy) within that account with the permissions
    you need.

**There are a couple of ways STS can be used:**

**Scenario 1:**

1. Develop an Identity Broker to communicate with LDAP and AWS STS.
2. Identity Broker always authenticates with LDAP first, then with AWS STS.
3. Application then gets temporary access to AWS resources.


**Scenario 2:**

1. Develop an Identity Broker to communicate with LDAP and AWS STS.
2. Identity Broker authenticates with LDAP first, then gets an IAM role associated with the
    user.
3. Application then authenticates with STS and assumes that IAM role.
4. Application uses that IAM role to interact with the service.

**IAM BEST PRACTICES**

- Lock Away Your AWS Account Root User Access Keys.
- Create Individual IAM Users.
- Use Groups to Assign Permissions to IAM Users.
- Grant Least Privilege.
- Get Started Using Permissions with AWS Managed Policies.
- Use Customer Managed Policies Instead of Inline Policies.
- Use Access Levels to Review IAM Permissions.
- Configure a Strong Password Policy for Your Users.
- Enable MFA.
- Use Roles for Applications That Run on Amazon EC2 Instances.
- Use Roles to Delegate Permissions.
- Do Not Share Access Keys.
- Rotate Credentials Regularly.
- Remove Unnecessary Credentials.
- Use Policy Conditions for Extra Security.
- Monitor Activity in Your AWS Account.

### AWS Accounts

**AWS ORGANIZATIONS**

AWS Organizations helps you centrally govern your environment as you grow and scale your
workloads on AWS.

Organizations helps you to centrally manage billing; control access, compliance, and security; and
share resources across your AWS accounts.

Using AWS Organizations, you can automate account creation, create groups of accounts to reflect
your business needs, and apply policies for these groups for governance.

You can also simplify billing by setting up a single payment method for all of your AWS accounts.

Through integrations with other AWS services, you can use Organizations to define central
configurations and resource sharing across accounts in your organization.

AWS Organizations is available to all AWS customers at no additional charge.

The AWS Organizations API enables automation for account creation and management.


**Available in two feature sets:**

- Consolidated billing
- All features

By default, organizations support consolidated billing features.

Consolidated billing separates paying accounts and linked accounts.

You can use AWS Organizations to set up a single payment method for all the AWS accounts in your
organization through consolidated billing.

With consolidated billing, you can see a combined view of charges incurred by all your accounts.

Can also take advantage of pricing benefits from aggregated usage, such as volume discounts for
Amazon EC2 and Amazon S3.

Limit of 20 linked accounts for consolidated billing (default).

Policies can be assigned at different points in the hierarchy.

Can help with cost control through volume discounts.

Unused reserved EC2 instances are applied across the group.

Paying accounts should be used for billing purposes only.

Billing alerts can be setup at the paying account which shows billing for all linked accounts.

**Core concepts:**

- **AWS Organization -** An organization is a collection of AWS accounts that you can organize
    into a hierarchy and manage centrally.
- **AWS Account -** An AWS account is a container for your AWS resources.
- **Master Account -** A master account is the AWS account you use to create your organization.
- **Member Account -** A member account is an AWS account, other than the master account,
    that is part of an organization.
- **Administrative Root -** An administrative root is the starting point for organizing your AWS
    accounts. The administrative root is the top-most container in your organization’s hierarchy.
- **Organizational Unit (OU) -** An organizational unit (OU) is a group of AWS accounts within an
    organization. An OU can also contain other OUs enabling you to create a hierarchy.
- **Policy -** A policy is a “document” with one or more statements that define the controls that
    you want to apply to a group of AWS accounts. AWS Organizations supports a specific type
    of policy called a Service Control Policy (SCP). An SCP defines the AWS service actions, such
    as Amazon EC2 RunInstances, that are available for use in different accounts within an
    organization.

**Migrating accounts between organizations:**

- Accounts can be migrated between organizations.
- You must have root or IAM access to both the member and master accounts.
- Use the AWS Organizations console for just a few accounts.
- Use the AWS Organizations API or AWS Command Line Interface (AWS CLI) if there are many
    accounts to migrate.


- Billing history and billing reports for all accounts stay with the master account in an
    organization.
- Before migration download any billing or report history for any member accounts that you
    want to keep.
- When a member account leaves an organization, all charges incurred by the account are
    charged directly to the standalone account.
- Even if the account move only takes a minute to process, it is likely that some charges will
    be incurred by the member account.

### AWS Resource access manager

AWS Resource Access Manager (RAM) is a service that enables you to easily and securely share
AWS resources with any AWS account or within your AWS Organization.

You can share AWS Transit Gateways, Subnets, AWS License Manager configurations, and Amazon
Route 53 Resolver rules resources with RAM.

RAM eliminates the need to create duplicate resources in multiple accounts, reducing the
operational overhead of managing those resources in every single account you own.

You can create resources centrally in a multi-account environment, and use RAM to share those
resources across accounts in **three simple steps** :

1. Create a Resource Share
2. Specify resources
3. Specify accounts

RAM is available at no additional charge.

**Key benefits:**

- **Reduce Operational Overhead -** Procure AWS resources centrally, and use RAM to share
    resources such as subnets or License Manager configurations with other accounts. This
    eliminates the need to provision duplicate resources in every account in a multi-account
    environment.
- **Improve Security and Visibility -** RAM leverages existing policies and permissions set in AWS
    Identity and Access Management (IAM) to govern the consumption of shared resources.
    RAM also provides comprehensive visibility into shared resources to set alarms and visualize
    logs through integration with Amazon CloudWatch and AWS CloudTrail.
- **Optimize Costs -** Sharing resources such as AWS License Manager configurations across
    accounts allows you to leverage licenses in multiple parts of your company to increase
    utilization and optimize costs.

### Resource Groups

You can use resource groups to organize your AWS resources.

In AWS, a resource is an entity that you can work with.


Resource groups make it easier to manage and automate tasks on large numbers of resources at
one time.

Resource groups allow you to group resources and then tag them.

The Tag Editor assists with finding resources and adding tags.

**You can access Resource Groups through any of the following entry points:**

- On the navigation bar of the AWS Management Console.
- In the AWS Systems Manager console, from the left navigation pane entry for Resource
    Groups.
- By using the Resource Groups API, in AWS CLI commands or AWS SDK programming
    languages.

A resource group is a collection of AWS resources that are all in the same AWS region, and that
match criteria provided in a query.

In Resource Groups, there are two types of queries on which you can build a group.

Both query types include resources that are specified in the format AWS::service::resource.

- **Tag-based -** Tag-based queries include lists of resources and tags. Tags are keys that help
    identify and sort your resources within your organization. Optionally, tags include values for
    keys.
- **AWS CloudFormation stack-based -** In an AWS CloudFormation stack-based query, you
    choose an AWS CloudFormation stack in your account in the current region, and then
    choose resource types within the stack that you want to be in the group. You can base your
    query on only one AWS CloudFormation stack.

Resource groups can be nested; a resource group can contain existing resource groups in the same
region.

### AWS Directory Service

**GENERAL**

AWS provide a number of directory types.

**The following three types currently feature on the exam and will be covered on this page:**

- Active Directory Service for Microsoft Active Directory
- Simple AD
- AD Connector

**As an alternative to the AWS Directory service you can build your own Microsoft AD DCs in the
AWS cloud (on EC2):**

- When you build your own you can join an existing on-premise Active Directory domain
    (replication mode).
- You must establish a VPN (on top of Direct Connect if you have it).
- Replication mode is less secure than establishing trust relationships.


The table below summarizes the directory services covered on this page as well as a couple of
others, and provides some typical use cases:

**ACTIVE DIRECTORY SERVICE FOR MICROSOFT ACTIVE DIRECTORY**

Fully managed AWS services on AWS infrastructure.

Best choice if you have more than 5000 users and/or need a trust relationship set up.

Includes software patching, replication, automated backups, replacing failed DCs and monitoring.

Runs on a Windows Server.

Can perform schema extensions.

Works with SharePoint, Microsoft SQL Server and .Net apps.

You can setup trust relationships to extend authentication from on-premises Active Directories into
the AWS cloud.

On-premise users and groups can access resources in either domain using SSO.

Requires a VPN or Direct Connect connection.

Can be used as a standalone AD in the AWS cloud.


When used standalone users can access 3rd party applications such as Microsoft O365 through
federation.

You can also use Active Directory credentials to authenticate to the AWS management console
without having to set up SAML authentication.

AWS Microsoft AD supports AWS applications including Workspaces, WorkDocs, QuickSight, Chime,
Amazon Connect, and RDS for Microsoft SQL Server.

The following diagram shows some of the use cases for your AWS Microsoft AD directory, including
the ability to grant your users access to external cloud applications and allow your on-premises AD
users to manage and have access to resources in the AWS Cloud.

**Includes security features such as:**

- Fine-grained password policy management
- LDAP encryption through SSL/TLS
- HIPAA and PCI DSS approved
- Multi-factor authentication through integration with existing RADIUS-based MFA
    infrastructure

Monitoring provided through CloudTrail, notifications through SNS, daily automated snapshots.

Scalable service that scales by adding Domain Controllers.

Deployed in a HA configuration across two AZs in the same region.

AWS Microsoft AD does not support replication mode where replication to an on-premise AD takes
place.

**Two editions:**

- Standard Edition is optimized to be a primary directory for small and midsize businesses
    with up to 5,000 employees. It provides you enough storage capacity to support up to
    30,000 directory objects, such as users, groups, and computers.
- Enterprise Edition is designed to support enterprise organizations with up to 500,000


```
directory objects.
```
**Directory Sharing:**

- AWS Directory Service for Microsoft Active Directory allows you to use a directory in one
    account and share it with multiple accounts and VPCs.
- There is an hourly sharing charge for each additional account to which you share a
    directory.
- There is no sharing charge for additional VPCs to which you share a directory, or for the
    account in which you install the directory.

**SIMPLE AD**

An inexpensive Active Directory-compatible service with common directory features.

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

You can also sign on to the AWS management console with Simple AD user accounts to manage
AWS resources.

**Available in two editions:**

- Small – supports up to 500 users (approximately 2000 objects).
- Large – supports up to 5000 users (approximately 20,000 objects).

AWS creates two directory servers and DNS servers on two different subnets within an AZ.

**Simple AD does not support:**

- DNS dynamic updates.
- Schema extensions.
- Multi-factor authentication.


- Communication over LDAPS.
- PowerShell AD cmdlets.
- FSMO role transfer.

Not compatible with RDS SQL server.

Does not support trust relationships with other domains (use AWS MS AD).

**AD CONNECTOR**

AD Connector is a directory gateway for redirecting directory requests to your on-premise Active
Directory.

AD Connector eliminates the need for directory synchronization and the cost and complexity of
hosting a federation infrastructure.

Connects your existing on-premise AD to AWS.

Best choice when you want to use an existing Active Directory with AWS services.

**AD Connector comes in two sizes:**

- Small – designed for organizations up to 500 users.
- Large – designed for organizations up to 5000 users.

The VPC must be connected to your on-premise network via VPN or Direct Connect.

When users log in to AWS applications AD connector forwards sign-in requests to your on-premise
AD DCs.

You can also join EC2 instances to your on-premise AD through AD Connector.

You can also login to the AWS Management Console using your on-premise AD DCs for
authentication.

Not compatible with RDS SQL.

You can use AD Connector for multi-factor authentication using RADIUS-based MFA infrastructure.

**AD CONNECTOR VS SIMPLE AD**

The table below describes some of the key differences to consider when choosing AD Connector or
Simple AD:


### AWS Key Management Store (KMS)

AWS Key Management Store (KMS) is a managed service that enables you to easily encrypt your
data.

AWS KMS provides a highly available key storage, management, and auditing solution for you to
encrypt data within your own applications and control the encryption of stored data across AWS
services.

AWS KMS allows you to centrally manage and securely store your keys. These are known as
customer master keys or CMKs.

You can generate CMKs in KMS, in an AWS CloudHSM cluster, or import them from your own key
management infrastructure.

These master keys are protected by hardware security modules (HSMs) and are only ever used
within those modules.

You can submit data directly to KMS to be encrypted or decrypted using these master keys.

You set usage policies on these keys that determine which users can use them to encrypt and
decrypt data and under which conditions.

KMS is tightly integrated into many AWS services like Lambda, S3, EBS, EFS, DynamoDB, SQS etc.

AWS KMS is integrated with AWS services and client-side toolkits that use a method known as
envelope encryption to encrypt your data.

Under this method, KMS generates data keys which are used to encrypt data and are themselves
encrypted using your master keys in KMS.

Data keys are not retained or managed by KMS.

AWS services encrypt your data and store an encrypted copy of the data key along with the data it
protects.

When a service needs to decrypt your data they request KMS to decrypt the data key using your
master key.

If the user requesting data from the AWS service is authorized to decrypt under your master key
policy, the service will receive the decrypted data key from KMS with which it can decrypt the data
and return it in plaintext.

All requests to use your master keys are logged in AWS CloudTrail so you can understand who used
which key under which context and when they used it.

You can control who manages and accesses keys via IAM users and roles.

You can audit the use of keys via CloudTrail.

KMS differs from Secrets Manager as its purpose-built for encryption key management.

KMS is validated by many compliance schemes (e.g. PCI DSS Level 1, FIPS 140 - 2 Level 2).

**You can perform the following key management functions in AWS KMS:**


- Create keys with a unique alias and description.
- Import your own key material.
- Define which IAM users and roles can manage keys.
- Define which IAM users and roles can use keys to encrypt and decrypt data.
- Choose to have AWS KMS automatically rotate your keys on an annual basis.
- Temporarily disable keys so they cannot be used by anyone.
- Re-enable disabled keys.
- Delete keys that you no longer use.
- Audit use of keys by inspecting logs in AWS CloudTrail.
- Create custom key stores*.
- Connect and disconnect custom key stores*.
- Delete custom key stores*.

* The use of custom key stores requires CloudHSM resources to be available in your account.

**Typically, data is encrypted in one of the following three scenarios:**

1. You can use KMS APIs directly to encrypt and decrypt data using your master keys stored in
    KMS.
2. You can choose to have AWS services encrypt your data using your master keys stored in
    KMS. In this case data is encrypted using data keys that are protected by your master keys in
    KMS.
3. You can use the AWS Encryption SDK that is integrated with AWS KMS to perform
    encryption within your own applications, whether they operate in AWS or not.

**Custom Key Store:**

- The AWS KMS custom key store feature combines the controls provided by AWS CloudHSM
    with the integration and ease of use of AWS KMS.
- You can configure your own CloudHSM cluster and authorize KMS to use it as a dedicated
    key store for your keys rather than the default KMS key store.
- When you create keys in KMS you can chose to generate the key material in your CloudHSM
    cluster. Master keys that are generated in your custom key store never leave the HSMs in
    the CloudHSM cluster in plaintext and all KMS operations that use those keys are only
    performed in your HSMs.
- In all other respects master keys stored in your custom key store are consistent with other
    KMS CMKs.

**Key deletion:**

- You can schedule a customer master key and associated metadata that you created in AWS
    KMS for deletion, with a configurable waiting period from 7 to 30 days.
- This waiting period allows you to verify the impact of deleting a key on your applications
    and users that depend on it.
- The default waiting period is 30 days.
- You can cancel key deletion during the waiting period.

**Limits:**


- You can create up to 1000 customer master keys per account per region.
- As both enabled and disabled customer master keys count towards the limit, AWS
    recommend deleting disabled keys that you no longer use.
- AWS managed master keys created on your behalf for use within supported AWS services
    do not count against this limit.
- There is no limit to the number of data keys that can be derived using a master key and
    used in your application or by AWS services to encrypt data on your behalf.

### AWS CloudHSM

The AWS CloudHSM service helps you meet corporate, contractual and regulatory compliance
requirements for data security by using dedicated Hardware Security Module (HSM) instances
within the AWS cloud.

AWS and AWS Marketplace partners offer a variety of solutions for protecting sensitive data within
the AWS platform, but for some applications and data subject to contractual or regulatory
mandates for managing cryptographic keys, additional protection may be necessary.

CloudHSM complements existing data protection solutions and allows you to protect your
encryption keys within HSMs that are designed and validated to government standards for secure
key management.

CloudHSM allows you to securely generate, store and manage cryptographic keys used for data
encryption in a way that keys are accessible only by you.

A Hardware Security Module (HSM) provides secure key storage and cryptographic operations
within a tamper-resistant hardware device.

HSMs are designed to securely store cryptographic key material and use the key material without
exposing it outside the cryptographic boundary of the hardware.

You can use the CloudHSM service to support a variety of use cases and applications, such as
database encryption, Digital Rights Management (DRM), Public Key Infrastructure (PKI),
authentication and authorization, document signing, and transaction processing.

Runs on a dedicated hardware device, single tenanted.

The table below describes the latest version of CloudHSM and how it differs from its predecessor:

When you use the AWS CloudHSM service you create a CloudHSM Cluster.

Clusters can contain multiple HSM instances, spread across multiple Availability Zones in a region.


HSM instances in a cluster are automatically synchronized and load-balanced.

You receive dedicated, single-tenant access to each HSM instance in your cluster. Each HSM
instance appears as a network resource in your Amazon Virtual Private Cloud (VPC).

Adding and removing HSMs from your Cluster is a single call to the AWS CloudHSM API (or on the
command line using the AWS CLI).

After creating and initializing a CloudHSM Cluster, you can configure a client on your EC2 instance
that allows your applications to use the cluster over a secure, authenticated network connection.

Must be within a VPC and can be accessed via VPC Peering.

Applications don’t need to be in the same VPC but but the server or instance on which your
application and the HSM client are running must have network (IP) reachability to all HSMs in the
cluster.

Does not natively integrate with many AWS services like KMS, but instead requires custom
application scripting.

Offload SSL from web server, act as an issuing CA, enable TDE for Oracle databases.
The table below compares CloudHSM against KMS:

### Amazon Cognito

**AMAZON COGNITO GENERAL**

Amazon Cognito lets you add user sign-up, sign-in, and access control to your web and mobile apps
quickly and easily.

Amazon Cognito provides authentication, authorization, and user management for your web and
mobile apps.

Your users can sign in directly with a user name and password, or through a third party such as
Facebook, Amazon, or Google.

**The two main components of AWS Cognito are user pools and identity pools:**

- User pools are user directories that provide sign-up and sign-in options for your app users.
- Identity pools enable you to grant your users access to other AWS services.


You can use identity pools and user pools separately or together.

AWS Cognito works with external identity providers that support SAML or OpenID Connect, social
identity providers (such as Facebook, Twitter, Amazon).

Cognito Identity provides temporary security credentials to access your app’s backend resources in
AWS or any service behind Amazon API Gateway.

You can use Amazon, Facebook, Twitter, Digits, Google and any other OpenID Connect compatible
identity provider.

You can also integrate your own identity provider.

Cognito exposes server-side APIs.

Users can sign-up and sign-in using email, phone number, or user name.

End users of an application can also sign in with SMS-based MFA.

There is an import tool for migrating users into an Amazon Cognito User Pool.

**USER POOLS**

A user pool is a user directory in Amazon Cognito.

With a user pool, users can sign in to your web or mobile app through Amazon Cognito.

Users can also sign in through social identity providers like Facebook or Amazon, and through SAML
identity providers.

Whether users sign in directly or through a third party, all members of the user pool have a
directory profile that you can access through an SDK.

**User pools provide:**

- Sign-up and sign-in services.
- A built-in, customizable web UI to sign in users.
- Social sign-in with Facebook, Google, and Login with Amazon, as well as sign-in with SAML
    identity providers from your user pool.
- User directory management and user profiles.
- Security features such as multi-factor authentication (MFA), checks for compromised
    credentials, account takeover protection, and phone and email verification.
- Customized workflows and user migration through AWS Lambda triggers.

After successfully authenticating a user, Amazon Cognito issues JSON web tokens (JWT) that you
can use to secure and authorize access to your own APIs, or exchange for AWS credentials.

**IDENTITY POOLS**

Amazon Cognito identity pools (federated identities) enable you to create unique identities for your
users and federate them with identity providers.

With an identity pool, you can obtain temporary, limited-privilege AWS credentials to access other
AWS services. Amazon Cognito identity pools support the following identity providers:

- Public providers: Login with Amazon (Identity Pools), Facebook (Identity Pools), Google


```
(Identity Pools).
```
- Amazon Cognito User Pools
- Open ID Connect Providers (Identity Pools)
- SAML Identity Providers (Identity Pools)
- Developer Authenticated Identities (Identity Pools)

**AMAZON COGNITO SYNC**

Amazon Cognito Sync is an AWS service and client library that enables cross-device syncing of
application-related user data.

You can use it to synchronize user profile data across mobile devices and the web without requiring
your own backend.

The client libraries cache data locally so your app can read and write data regardless of device
connectivity status.

When the device is online, you can synchronize data, and if you set up push sync, notify other
devices immediately that an update is available.

### AWS WAF and Shield

**AWS WAF AND AWS SHIELD GENERAL**

AWS WAF and AWS Shield help protect your AWS resources from web exploits and DDoS attacks.

AWS WAF is a web application firewall service that helps protect your web apps from common
exploits that could affect app availability, compromise security, or consume excessive resources.

AWS Shield provides expanded DDoS attack protection for your AWS resources. Get 24/7 support
from the DDoS response team and detailed visibility into DDoS events.

We’ll now go into more detail on each service.

**AWS WEB APPLICATION FIREWALL (WAF)**

AWS WAF is a web application firewall that helps protect your web applications from common web
exploits that could affect application availability, compromise security, or consume excessive
resources.

AWS WAF helps protect web applications from attacks by allowing you to configure rules that allow,
block, or monitor (count) web requests based on conditions that you define.

These conditions include IP addresses, HTTP headers, HTTP body, URI strings, SQL injection and
cross-site scripting.

AWS WAF gives you control over which traffic to allow or block to your web applications by defining
customizable web security rules.

New rules can be deployed within minutes, letting you respond quickly to changing traffic patterns.

When AWS services receive requests for web sites, the requests are forwarded to AWS WAF for
inspection against defined rules.


Once a request meets a condition defined in the rules, AWS WAF instructs the underlying service to
either block or allow the request based on the action you define.

With AWS WAF you pay only for what you use.

AWS WAF pricing is based on how many rules you deploy and how many web requests your web
application receives.

There are no upfront commitments.

AWS WAF is tightly integrated with Amazon CloudFront and the Application Load Balancer (ALB),
services.

When you use AWS WAF on Amazon CloudFront, rules run in all AWS Edge Locations, located
around the world close to end users.

This means security doesn’t come at the expense of performance.

Blocked requests are stopped before they reach your web servers.

When you use AWS WAF on an Application Load Balancer, your rules run in region and can be used
to protect internet-facing as well as internal load balancers.

**WEB TRAFFIC FILTERING**

AWS WAF lets you create rules to filter web traffic based on conditions that include IP addresses,
HTTP headers and body, or custom URIs.

This gives you an additional layer of protection from web attacks that attempt to exploit
vulnerabilities in custom or third-party web applications.

In addition, AWS WAF makes it easy to create rules that block common web exploits like SQL
injection and cross site scripting.

AWS WAF allows you to create a centralized set of rules that you can deploy across multiple
websites.

This means that in an environment with many websites and web applications you can create a
single set of rules that you can reuse across applications rather than recreating that rule on every
application you want to protect.

**FULL FEATURE API**

AWS WAF can be completely administered via APIs.

This provides organizations with the ability to create and maintain rules automatically and
incorporate them into the development and design process.

For example, a developer who has detailed knowledge of the web application could create a
security rule as part of the deployment process.

This capability to incorporate security into your development process avoids the need for complex
handoffs between application and security teams to make sure rules are kept up to date.

AWS WAF can also be deployed and provisioned automatically with AWS CloudFormation sample
templates that allow you to describe all security rules you would like to deploy for your web


applications delivered by Amazon CloudFront.

AWS WAF is integrated with Amazon CloudFront, which supports custom origins outside of AWS –
this means you can protect web sites not hosted in AWS.

Support for IPv6 allows the AWS WAF to inspect HTTP/S requests coming from both IPv6 and IPv4
addresses.

**REAL-TIME VISIBILITY**

AWS WAF provides real-time metrics and captures raw requests that include details about IP
addresses, geo locations, URIs, User-Agent and Referers.

AWS WAF is fully integrated with Amazon CloudWatch, making it easy to setup custom alarms when
thresholds are exceeded, or particular attacks occur.

This information provides valuable intelligence that can be used to create new rules to better
protect applications.

**AWS SHIELD**

AWS Shield is a managed Distributed Denial of Service (DDoS) protection service that safeguards
applications running on AWS.

AWS Shield provides always-on detection and automatic inline mitigations that minimize
application downtime and latency, so there is no need to engage AWS Support to benefit from
DDoS protection.

There are two tiers of AWS Shield – Standard and Advanced.

**AWS SHIELD STANDARD**

All AWS customers benefit from the automatic protections of AWS Shield Standard, at no additional
charge.

AWS Shield Standard defends against most common, frequently occurring network and transport
layer DDoS attacks that target web sites or applications.

When using AWS Shield Standard with Amazon CloudFront and Amazon Route 53, you receive
comprehensive availability protection against all known infrastructure (Layer 3 and 4) attacks.

**AWS SHIELD ADVANCED**

Provides higher levels of protection against attacks targeting applications running on Amazon Elastic
Compute Cloud (EC2), Elastic Load Balancing (ELB), Amazon CloudFront, AWS Global Accelerator
and Amazon Route 53 resources.

In addition to the network and transport layer protections that come with Standard, AWS Shield
Advanced provides additional detection and mitigation against large and sophisticated DDoS
attacks, near real-time visibility into attacks, and integration with AWS WAF, a web application
firewall.

AWS Shield Advanced also gives you 24×7 access to the AWS DDoS Response Team (DRT) and
protection against DDoS related spikes in your Amazon Elastic Compute Cloud (EC2), Elastic Load


Balancing (ELB), Amazon CloudFront, AWS Global Accelerator and Amazon Route 53 charges.

AWS Shield Advanced is available globally on all Amazon CloudFront, AWS Global Accelerator, and
Amazon Route 53 edge locations.

Origin servers can be Amazon S3, Amazon Elastic Compute Cloud (EC2), Elastic Load Balancing (ELB),
or a custom server outside of AWS.

AWS Shield Advanced includes DDoS cost protection, a safeguard from scaling charges as a result of
a DDoS attack that causes usage spikes on protected Amazon EC2, Elastic Load Balancing (ELB),
Amazon CloudFront, AWS Global Accelerator, or Amazon Route 53.

If any of the AWS Shield Advanced protected resources scale up in response to a DDoS attack, you
can request credits via the regular AWS Support channel.


[[Security, Identity & Compliance Quiz Questions]]