#### Question  62


**The application development team in a company have developed a Java application and saved the source code in a .war

file. They would like to run the application on AWS resources and are looking for a service that can handle the

provisioning and management of the underlying resources it will run on.**


**Which AWS service should a Solutions Architect recommend the Developers use to upload the Java source code file?**


1: AWS Elastic Beanstalk


2: AWS CodeDeploy


3: AWS CloudFormation


4: AWS OpsWorks


**Answer: 1**


**Explanation:**


AWS Elastic Beanstalk can be used to quickly deploy and manage applications in the AWS Cloud. Developers upload

applications and Elastic Beanstalk handles the deployment details of capacity provisioning, load balancing,

auto-scaling, and application health monitoring


Elastic Beanstalk supports applications developed in Go, Java, .NET, Node.js, PHP, Python, and Ruby, as well as

different platform configurations for each language. To use Elastic Beanstalk, you create an application, upload an

application version in the form of an application source bundle (for example, a Java .war file) to Elastic Beanstalk,

and then provide some information about the application.


- CORRECT "AWS Elastic Beanstalk" is the correct answer.


- INCORRECT "AWS CodeDeploy" is incorrect. AWS CodeDeploy is a deployment service that automates application deployments

  to Amazon EC2 instances, on-premises instances, serverless Lambda functions, or Amazon ECS services.


- INCORRECT "AWS CloudFormation" is incorrect. AWS CloudFormation uses templates to deploy infrastructure as code. It is

  not a PaaS service like Elastic Beanstalk and is more focused on infrastructure than applications and management of

  applications.


- INCORRECT "AWS OpsWorks" is incorrect. AWS OpsWorks is a configuration management service that provides managed

  instances of Chef and Puppet.


**References:**


https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/aws-elastic-

beanstalk/

