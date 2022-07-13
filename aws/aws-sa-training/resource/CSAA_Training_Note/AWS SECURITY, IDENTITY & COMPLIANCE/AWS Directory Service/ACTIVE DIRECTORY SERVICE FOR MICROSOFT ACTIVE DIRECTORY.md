#### ACTIVE DIRECTORY SERVICE FOR MICROSOFT ACTIVE DIRECTORY


Fully managed AWS services on AWS infrastructure.


Best choice if you have more than 5000 users and/or need a trust relationship set up.


Includes software patching, replication, automated backups, replacing failed DCs and monitoring.


Runs on a Windows Server.


Can perform schema extensions.


Works with SharePoint, Microsoft SQL Server and .Net apps.


You can setup trust relationships to extend authentication from on-premises Active Directories into the AWS cloud.


On-premise users and groups can access resources in either domain using SSO.


Requires a VPN or Direct Connect connection.


Can be used as a standalone AD in the AWS cloud.


When used standalone users can access 3rd party applications such as Microsoft O365 through federation.


You can also use Active Directory credentials to authenticate to the AWS management console without having to set up

SAML authentication.


AWS Microsoft AD supports AWS applications including Workspaces, WorkDocs, QuickSight, Chime, Amazon Connect, and RDS

for Microsoft SQL Server.


The following diagram shows some of the use cases for your AWS Microsoft AD directory, including the ability to grant

your users access to external cloud applications and allow your on-premises AD users to manage and have access to

resources in the AWS Cloud.


**Includes security features such as:**


- Fine-grained password policy management

- LDAP encryption through SSL/TLS

- HIPAA and PCI DSS approved

- Multi-factor authentication through integration with existing RADIUS-based MFA infrastructure


Monitoring provided through CloudTrail, notifications through SNS, daily automated snapshots.


Scalable service that scales by adding Domain Controllers.


Deployed in a HA configuration across two AZs in the same region.


AWS Microsoft AD does not support replication mode where replication to an on-premise AD takes place.


**Two editions:**


- Standard Edition is optimized to be a primary directory for small and midsize businesses with up to 5,000 employees.

  It provides you enough storage capacity to support up to 30,000 directory objects, such as users, groups, and

  computers.

- Enterprise Edition is designed to support enterprise organizations with up to 500,000


```

directory objects.

```


**Directory Sharing:**


- AWS Directory Service for Microsoft Active Directory allows you to use a directory in one account and share it with

  multiple accounts and VPCs.

- There is an hourly sharing charge for each additional account to which you share a directory.

- There is no sharing charge for additional VPCs to which you share a directory, or for the account in which you install

  the directory.

