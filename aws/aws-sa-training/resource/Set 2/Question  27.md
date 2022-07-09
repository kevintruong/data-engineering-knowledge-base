#### Question  27


**A company has divested a single business unit and needs to move the AWS account owned by the business unit to another

AWS Organization. How can this be achieved?**


1: Create a new account in the destination AWS Organization and migrate resources


2: Create a new account in the destination AWS Organization and share the original resources using AWS Resource Access

Manager


3: Migrate the account using AWS CloudFormation


4: Migrate the account using the AWS Organizations console


Answer: 4


**Explanation:**


Accounts can be migrated between organizations. To do this you must have root or IAM access to both the member and

master accounts. Resources will remain under the control of the migrated account.


- CORRECT "Migrate the account using the AWS Organizations console" is the correct answer.


- INCORRECT "Create a new account in the destination AWS Organization and migrate resources" is incorrect. You do not

  need to create a new account in the destination AWS Organization as you can just migrate the existing account.


- INCORRECT "Create a new account in the destination AWS Organization and share the original resources using AWS

  Resource Access Manager" is incorrect. You do not need to create a new account in the destination AWS Organization as

  you can just migrate the existing account.


- INCORRECT "Migrate the account using AWS CloudFormation" is incorrect. You do not need to use AWS CloudFormation. You

  can use the Organizations API or AWS CLI for when there are many accounts to migrate and therefore you could use

  CloudFormation for any additional automation but it is not necessary for this scenario.


**References:**


https://aws.amazon.com/premiumsupport/knowledge-center/organizations-move-accounts/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/management-tools/aws-

organizations/

