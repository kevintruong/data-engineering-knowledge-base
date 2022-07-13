**Explanation:**

Accounts can be migrated between organizations. To do this you must have root or IAM access to both the member and

master accounts. Resources will remain under the control of the migrated account.

- ✅ :  "Migrate the account using the AWS Organizations console" is the correct answer.

- ❌ :  "Create a new account in the destination AWS Organization and migrate resources" is incorrect. You do not

  need to create a new account in the destination AWS Organization as you can just migrate the existing account.

- ❌ :  "Create a new account in the destination AWS Organization and share the original resources using AWS

  Resource Access Manager" is incorrect. You do not need to create a new account in the destination AWS Organization as

  you can just migrate the existing account.

- ❌ :  "Migrate the account using AWS CloudFormation" is incorrect. You do not need to use AWS CloudFormation. You

  can use the Organizations API or AWS CLI for when there are many accounts to migrate and therefore you could use

  CloudFormation for any additional automation but it is not necessary for this scenario.

**References:**

<https://aws.amazon.com/premiumsupport/knowledge-center/organizations-move-accounts/>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/management-tools/aws>-

organizations/

----

- #destination_aws_organization #aws_cloudformation #aws_organizations_console #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/management-tools/aws>>- #aws_cli
