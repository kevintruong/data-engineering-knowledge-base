#### AD CONNECTOR

AD Connector is a directory gateway for redirecting directory requests to your
on-premise Active Directory.

AD Connector eliminates the need for directory synchronization and the cost and
complexity of hosting a federation

infrastructure.

Connects your existing on-premise AD to AWS.

Best choice when you want to use an existing Active Directory with AWS services.

**AD Connector comes in two sizes:**

- Small – designed for organizations up to 500 users.

- Large – designed for organizations up to 5000 users.

The VPC must be connected to your on-premise network via VPN or Direct Connect.

When users log in to AWS applications AD connector forwards sign-in requests to
your on-premise AD DCs.

You can also join EC2 instances to your on-premise AD through AD Connector.

You can also login to the AWS Management Console using your on-premise AD DCs
for authentication.

Not compatible with RDS SQL.

You can use AD Connector for multi-factor authentication using RADIUS-based MFA
infrastructure.

