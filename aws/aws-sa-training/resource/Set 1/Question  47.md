#### Question  47


**A recent security audit uncovered some poor deployment and configuration practices within your VPC. You need to ensure

that applications are deployed in secure configurations.**


**How can this be achieved in the most operationally efficient manner?**


1: Remove the ability for staff to deploy applications


2: Use CloudFormation with securely configured templates


3: Manually check all application configurations before deployment


4: Use AWS Inspector to apply secure configurations


Answer: 2


**Explanation:**


CloudFormation helps users to deploy resources in a consistent and orderly way. By ensuring the CloudFormation templates

are created and administered with the right security configurations for your resources, you can then repeatedly deploy

resources with secure settings and reduce the risk of human error.


- CORRECT "Use CloudFormation with securely configured templates" is the correct answer.


- INCORRECT "Remove the ability for staff to deploy applications" is incorrect. Removing the ability of staff to deploy

  resources does not help you to deploy applications securely as it does not solve the problem of how to do this in an

  operationally efficient manner.


- INCORRECT "Manually check all application configurations before deployment" is incorrect. Manual checking of all

  application configurations before deployment is not operationally efficient.


- INCORRECT "Use AWS Inspector to apply secure configurations" is incorrect. Amazon Inspector is an automated security

  assessment service that helps improve the security and compliance of applications **_deployed_** on AWS. It is not

  used to secure the actual deployment of resources, only to assess the deployed state of the resources.


**References:**


https://aws.amazon.com/cloudformation/resources/templates/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/management-tools/aws-

cloudformation/

