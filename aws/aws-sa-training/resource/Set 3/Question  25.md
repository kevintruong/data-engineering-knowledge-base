#### Question  25


**An Architect needs to find a way to automatically and repeatably create many member accounts within an AWS

Organization. The accounts also need to be moved into an OU and have VPCs and subnets created.**


**What is the best way to achieve this?**


1: Use the AWS Organizations API


2: Use CloudFormation with scripts


3: Use the AWS Management Console


4: Use the AWS CLI


Answer: 2


**Explanation:**


The best solution is to use a combination of scripts and AWS CloudFormation. You will also leverage the AWS

Organizations API. This solution can provide all of the requirements.


- CORRECT "Use CloudFormation with scripts" is the correct answer.


- INCORRECT "Use the AWS Organizations API" is incorrect. You can create member accounts with the AWS Organizations API.

  However, you cannot use that API to configure the account and create VPCs and subnets.


- INCORRECT "Use the AWS Management Console" is incorrect. Using the AWS Management Console is not a method of

  automatically creating the resources.


- INCORRECT "Use the AWS CLI" is incorrect. You can do all tasks using the AWS CLI but it is better to automate the

  process using AWS CloudFormation.


**References:**


https://aws.amazon.com/blogs/security/how-to-use-aws-organizations-to-automate-end-to-end-account-

creation/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/management-tools/aws-

organizations/

