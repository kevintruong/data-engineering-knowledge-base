#### Question  37


**An Amazon VPC contains a mixture of Amazon EC2 instances in production and non-production environments. A Solutions

Architect needs to devise a way to segregate access permissions to different sets of users for instances in different

environments.**


**How can this be achieved? (Select TWO)**


1: Attach an Identity Provider (IdP) and delegate access to the instances to the relevant groups


2: Create an IAM policy that grants access to any instances with the specific tag and attach to the users and groups


3: Create an IAM policy with a conditional statement that matches the environment variables


4: Add an environment variable to the instances using user data


5: Add a specific tag to the instances you want to grant the users or groups access to


**Answer: 2,5**


**Explanation:**


You can use the condition checking in IAM policies to look for a specific tag. IAM checks that the tag attached to the

principal making the request matches the specified key name and value.


- CORRECT "Create an IAM policy that grants access to any instances with the specific tag and attach to the users and

  groups" is the correct answer.


- CORRECT "Add a specific tag to the instances you want to grant the users or groups access to" is the correct answer.


- INCORRECT "Attach an Identity Provider (IdP) and delegate access to the instances to the relevant groups" is

  incorrect. You cannot use an IdP for this solution.


- INCORRECT "Create an IAM policy with a conditional statement that matches the environment variables" is incorrect as

  the statement should be checking for the tag.


- INCORRECT "Add an environment variable to the instances using user data" is incorrect. You cannot achieve this outcome

  using environment variables stored in user data and conditional statements in a policy. You must use an IAM policy

  that grants access to instances based on the tag.


**References:**


https://aws.amazon.com/premiumsupport/knowledge-center/iam-ec2-resource-tags/


https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html

