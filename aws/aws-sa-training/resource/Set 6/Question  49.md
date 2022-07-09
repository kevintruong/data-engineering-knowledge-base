#### Question  49


**A Solutions Architect needs to run a PowerShell script on a fleet of Amazon EC2 instances running Microsoft Windows.

The instances have already been launched in an Amazon VPC. What tool can be run from the AWS Management Console that to

execute the script on all target EC2 instances?**


1: AWS CodeDeploy


2: AWS Config


3: Run Command


4: AWS OpsWorks


**Answer: 3**


**Explanation:**


Run Command is designed to support a wide range of enterprise scenarios including installing software, running ad hoc

scripts or Microsoft PowerShell commands, configuring Windows Update settings, and more.


Run Command can be used to implement configuration changes across Windows instances on a consistent yet ad hoc basis and

is accessible from the AWS Management Console, the AWS Command Line Interface (CLI), the AWS Tools for Windows

PowerShell, and the AWS SDKs.


- CORRECT "Run Command" is the correct answer.


- INCORRECT "AWS CodeDeploy" is incorrect. AWS CodeDeploy is a deployment service that automates application deployments

  to Amazon EC2 instances, on-premises instances, serverless Lambda functions, or Amazon ECS services.


- INCORRECT "AWS Config" is incorrect. AWS Config is a service that enables you to assess, audit, and evaluate the

  configurations of your AWS resources. It is not used for ad-hoc script execution.


- INCORRECT "AWS OpsWorks" is incorrect. AWS OpsWorks provides instances of managed Puppet and Chef.


**References:**


https://aws.amazon.com/blogs/aws/new-ec2-run-command-remote-instance-management-at-scale/

