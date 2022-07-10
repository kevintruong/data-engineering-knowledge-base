#### Question  20

**A company allows its developers to attach existing IAM policies to existing IAM roles to enable faster experimentation

and agility. However, the security operations team is concerned that the developers could attach the existing

administrator policy, which would allow the developers to circumvent any other security policies.**

**How should a solutions architect address this issue?**

- [ ] Create an Amazon SNS topic to send an alert every time a developer creates a new policy

- [ ] Use service control policies to disable IAM activity across all accounts in the organizational unit

- [ ] Prevent the developers from attaching any policies and assign all IAM duties to the security operations team

- [x] Set an IAM permissions boundary on the developer IAM role that explicitly denies attaching the administrator policy

- hasExplain:: [[explanation_Question  20.md]]

# iam_policies #iam_roles #iam_permissions #developer_iam_role #iam_duties
