**Explanation:**

The permissions boundary for an IAM entity (user or role) sets the maximum permissions that the entity can have. This

can change the effective permissions for that user or role. The effective permissions for an entity are the permissions

that are granted by all the policies that affect the user or role. Within an account, the permissions for an entity can

be affected by identity-based policies, resource-based policies, permissions boundaries, Organizations SCPs, or session

policies.

Therefore, the solutions architect can set an IAM permissions boundary on the developer IAM role that explicitly denies

attaching the administrator policy.

- ✅ :  "Set an IAM permissions boundary on the developer IAM role that explicitly denies attaching the administrator

  policy" is the correct answer.

- ❌ :  "Create an Amazon SNS topic to send an alert every time a developer creates a new policy" is incorrect as

  this would mean investigating every incident which is not an efficient solution.

- ❌ :  "Use service control policies to disable IAM activity across all accounts in the organizational unit"

  is incorrect as this would prevent the developers from being able to work with IAM completely.

- ❌ :  "Prevent the developers from attaching any policies and assign all IAM duties to the security operations

  team" is incorrect as this is not necessary. The requirement is to allow developers to work with policies, the

  solution needs to find a secure way of achieving this.

**References:**

<https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/security-identity>-

compliance/aws-iam/

----

- #iam_permissions #developer_iam_role #iam_duties #iam_entity #permissions_boundaries
