#### Question  64


**A new department will begin using AWS services an AWS account and a Solutions Architect needs to create an

authentication and authorization strategy. Select the correct statements regarding IAM groups? (Select TWO)**


1: IAM groups can be used to assign permissions to users


2: IAM groups can be nested up to 4 levels


3: IAM groups can be used to group EC2 instances


4: IAM groups can temporarily assume a role to take on permissions for a specific task


5: An IAM group is not an identity and cannot be identified as a principal in an IAM policy


**Answer: 1,5**


**Explanation:**


An IAM group is a collection of IAM users. Groups let you specify permissions for multiple users, which can make it

easier to manage the permissions for those users.


The following facts apply to IAM Groups:


- Groups are collections of users and have policies attached to them.

- A group is not an identity and cannot be identified as a principal in an IAM policy.

- Use groups to assign permissions to users.

- IAM groups cannot be used to group EC2 instances.

- Only users and services can assume a role to take on permissions (not groups).


- CORRECT "IAM groups can be used to assign permissions to users" is a correct answer.


- CORRECT "An IAM group is not an identity and cannot be identified as a principal in an IAM policy" is also a correct

  answer.


- INCORRECT "IAM groups can be nested up to 4 levels" is incorrect as this not possible.


- INCORRECT "IAM groups can be used to group EC2 instances" is incorrect as they can only be used to group user

  accounts.


- INCORRECT "IAM groups can temporarily assume a role to take on permissions for a specific task" is incorrect as this

  is not possible.


**References:**


https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/security-identity-

compliance/aws-iam/

