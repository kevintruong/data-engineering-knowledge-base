#### Question  44


**A Solutions Architect has deployed a number of AWS resources using CloudFormation. Some changes must be made to a

couple of resources within the stack. Due to recent failed updates, the Solutions Architect is a little concerned about

the effects that implementing updates to the resources might have on other resources in the stack.**


**What is the easiest way to proceed cautiously?**


1: Create and execute a change set


2: Use OpsWorks to manage the configuration changes


3: Use a direct update


4: Deploy a new stack to test the changes


**Answer: 1**


**Explanation:**


AWS CloudFormation provides two methods for updating stacks: direct update or creating and executing change sets. When

you directly update a stack, you submit changes and AWS CloudFormation immediately deploys them.


Use direct updates when you want to quickly deploy your updates. With change sets, you can preview the changes AWS

CloudFormation will make to your stack, and then decide whether to apply those changes.


- CORRECT "Create and execute a change set" is the correct answer.


- INCORRECT "Use OpsWorks to manage the configuration changes" is incorrect. You cannot use OpsWorks to manage the

  configuration changes. OpsWorks is used for implementing managed Chef and Puppet services.


- INCORRECT "Use a direct update" is incorrect. Direct updates will not provide the safeguard of being able to preview

  the changes as changes sets do.


- INCORRECT "Deploy a new stack to test the changes" is incorrect. You do not need to go to the trouble and cost of

  deploying a new stack.


**References:**


https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/management-tools/aws-

cloudformation/

