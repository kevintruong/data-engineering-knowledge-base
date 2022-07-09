#### Question  31


**A Solutions Architect regularly deploys and manages infrastructure services for customers on AWS. The SysOps team are

facing challenges in tracking changes that are made to the infrastructure services and rolling back when problems

occur.**


**How can a Solutions Architect BEST assist the SysOps team?**


1: Use AWS Systems Manager to manage all updates to the infrastructure services


2: Use CodeDeploy to manage version control for the infrastructure services


3: Use CloudFormation templates to deploy and manage the infrastructure services


4: Use Trusted Advisor to record updates made to the infrastructure services


**Answer: 3**


**Explanation:**


When you provision your infrastructure with AWS CloudFormation, the AWS CloudFormation template describes exactly what

resources are provisioned and their settings. Because these templates are text files, you simply track differences in

your templates to track changes to your infrastructure, similar to the way developers control revisions to source code.


For example, you can use a version control system with your templates so that you know exactly what changes were made,

who made them, and when. If at any point you need to reverse changes to your infrastructure, you can use a previous

version of your template.


- CORRECT "Use CloudFormation templates to deploy and manage the infrastructure services" is the correct answer.


- INCORRECT "Use AWS Systems Manager to manage all updates to the infrastructure services" is incorrect. AWS Systems

  Manager gives you visibility and control of your infrastructure on AWS. Systems Manager provides a unified user

  interface so you can view operational data from multiple AWS services and allows you


to automate operational tasks across your AWS resources. However, CloudFormation would be the preferred method of

maintaining the state of the overall architecture.


- INCORRECT "Use CodeDeploy to manage version control for the infrastructure services" is incorrect. AWS CodeDeploy is a

  deployment service that automates application (not infrastructure) deployments to Amazon EC2 instances, on-premises

  instances, or serverless Lambda functions. This would be a good fit if we were talking about an application

  environment where code changes need to be managed but not for infrastructure services..


- INCORRECT "Use Trusted Advisor to record updates made to the infrastructure services" is incorrect. AWS Trusted

  Advisor is an online resource to help you reduce cost, increase performance, and improve security by optimizing your

  AWS environment, Trusted Advisor provides real time guidance to help you provision your resources following AWS best

  practices.


**References:**


https://aws.amazon.com/cloudformation/resources/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-

delivery/amazon-cloudfront/

