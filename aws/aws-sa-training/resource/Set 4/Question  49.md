#### Question  49


**The Systems Administrators in a company currently use Chef for configuration management of on-premise servers. Which

AWS service can a Solutions Architect use that will provide a fully-managed configuration management service that will

enable the use of existing Chef cookbooks?**


1: Elastic Beanstalk


2: CloudFormation


3: OpsWorks for Chef Automate


4: Opsworks Stacks


**Answer: 3**


**Explanation:**


AWS OpsWorks is a configuration management service that provides managed instances of Chef and Puppet. AWS OpsWorks for

Chef Automate is a fully-managed configuration management service that hosts Chef Automate, a suite of automation tools

from Chef for configuration management, compliance and security, and continuous deployment. OpsWorks for Chef Automate

is completely compatible with tooling and cookbooks from the Chef community and automatically registers new nodes with

your Chef server.


- CORRECT "OpsWorks for Chef Automate" is the correct answer.


- INCORRECT "Opsworks Stacks" is incorrect. AWS OpsWorks Stacks lets you manage applications and servers on AWS and

  on-premises and uses Chef Solo. The question does not require the managed solution on AWS to manage on-premises

  resources, just to use existing cookbooks so this is not the preferred solution.


- INCORRECT "Elastic Beanstalk" is incorrect. AWS Elastic Beanstalk is not able to build infrastructure using Chef

  cookbooks.


- INCORRECT "CloudFormation" is incorrect. AWS CloudFormation is not able to build infrastructure using Chef cookbooks.


**References:**


https://aws.amazon.com/opsworks/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/management-tools/aws-

opsworks/

