##### Question 1 answer: B

Explanation:

```

AWS CloudFormation StackSets extends the functionality of stacks by enabling you to create,

update, or delete stacks across multiple accounts and regions with a single operation.

Using an administrator account, you define and manage an AWS CloudFormation template, and

use the template as the basis for provisioning stacks into selected target accounts across

specified regions. An administrator account is the AWS account in which you create stack sets.

A stack set is managed by signing in to the AWS administrator account in which it was created. A

target account is the account into which you create, update, or delete one or more stacks in your

stack set.

Before you can use a stack set to create stacks in a target account, you must set up a trust

relationship between the administrator and target accounts.

A regular CloudFormation template cannot be used across regions and accounts. You would

need to create copies of the template and then manage updates.

You do not need to use a third-party product such as Terraform as this functionality can be

delivered through native AWS technology.

```

