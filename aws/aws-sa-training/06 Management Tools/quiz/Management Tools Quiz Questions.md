### Management Tools Quiz Questions

Answers and explanations are provided below after the last question in this section.

**Question 1:**

You are a Solutions Architect at Digital Cloud Training. A client from a large multinational corporation is working on a deployment of a significant amount of resources into AWS. The client would like to be able to deploy resources across multiple AWS accounts and regions using a single toolset and template. You have been asked to suggest a toolset that can provide this functionality?

```
A. Use a CloudFormation template that creates a stack and specify the logical IDs of each account and region
B. Use a CloudFormation StackSet and specify the target accounts and regions in which the stacks will be created
C. Use a third-party product such as Terraform that has support for multiple AWS accounts and regions
D. This cannot be done, use separate CloudFormation templates per AWS account and region
```

**Question 2:**

A Solutions Architect needs to monitor application logs and receive a notification whenever a specific number of occurrences of certain HTTP status code errors occur. Which tool should the Architect use?

```
A. CloudWatch Events
B. CloudWatch Logs
C. CloudTrail Trails
D. CloudWatch Metrics
```
**Question 3:**

A Solutions Architect is designing the system monitoring and deployment layers of a serverless application. The system monitoring layer will manage system visibility through recording logs and metrics and the deployment layer will deploy the application stack and manage workload changes through a release management process.

The Architect needs to select the most appropriate AWS services for these functions. Which services and frameworks should be used for the system monitoring and deployment layers? (choose 2)

```
A. Use AWS X-Ray to package, test, and deploy the serverless application stack
B. Use Amazon CloudTrail for consolidating system and application logs and monitoring custom metrics
C. Use AWS Lambda to package, test, and deploy the serverless application stack
D. Use AWS SAM to package, test, and deploy the serverless application stack
E. Use Amazon CloudWatch for consolidating system and application logs and monitoring custom metrics

**Question 4:**

A systems integration consultancy regularly deploys and manages multi-tiered web services for customers on AWS. The SysOps team are facing challenges in tracking changes that are made to the web services and rolling back when problems occur.

Which of the approaches below would BEST assist the SysOps team?

```
A. Use AWS Systems Manager to manage all updates to the web services
B. Use CodeDeploy to manage version control for the web services
C. Use Trusted Advisor to record updates made to the web services
D. Use CloudFormation templates to deploy and manage the web services
```

**Question 5:**

An event in CloudTrail is the record of an activity in an AWS account. What are the two types of events that can be logged in CloudTrail? (choose 2)

```
A. System Events which are also known as instance level operations
B. Management Events which are also known as control plane operations
C. Platform Events which are also known as hardware level operations
D. Data Events which are also known as data plane operations
E. API events which are also known as CloudWatch events
```
**Question 6:**

Your company currently uses Puppet Enterprise for infrastructure and application management.  You are looking to move some of your infrastructure onto AWS and would like to continue to use the same tools in the cloud. What AWS service provides a fully managed configuration management service that is compatible with Puppet Enterprise?

```
A. Elastic Beanstalk
B. CloudFormation
C. OpsWorks
D. CloudTrail
```

**Question 7:**

The operations team in your company are looking for a method to automatically respond to failed system status check alarms that are being received from an EC2 instance. The system in question is experiencing intermittent problems with its operating system software.

Which two steps will help you to automate the resolution of the operating system software issues?  (choose 2)

A. Create a CloudWatch alarm that monitors the “StatusCheckFailed_System” metric
B. Create a CloudWatch alarm that monitors the “StatusCheckFailed_Instance” metric
C. Configure an EC2 action that recovers the instance
D. Configure an EC2 action that terminates the instance
E. Configure an EC2 action that reboots the instance


**MANAGEMENT TOOLS - ANSWERS**

**Question 1 answer: B**

Explanation:

```
AWS CloudFormation StackSets extends the functionality of stacks by enabling you to create, update, or delete stacks across multiple accounts and regions with a single operation.  Using an administrator account, you define and manage an AWS CloudFormation template, and use the template as the basis for provisioning stacks into selected target accounts across specified regions. An administrator account is the AWS account in which you create stack sets.

A stack set is managed by signing in to the AWS administrator account in which it was created. A target account is the account into which you create, update, or delete one or more stacks in your stack set.

Before you can use a stack set to create stacks in a target account, you must set up a trust relationship between the administrator and target accounts.  A regular CloudFormation template cannot be used across regions and accounts. You would
need to create copies of the template and then manage updates.

You do not need to use a third-party product such as Terraform as this functionality can be delivered through native AWS technology.
```

**Question 2 answer: B**

Explanation:

```
You can use CloudWatch Logs to monitor applications and systems using log data. For example, CloudWatch Logs can track the number of errors that occur in your application logs and send you a notification whenever the rate of errors exceeds a threshold you specify. This is the best tool for this requirement.

Amazon CloudWatch Events delivers a near real-time stream of system events that describe changes in Amazon Web Services (AWS) resources. Though you can generate custom application- level events and publish them to CloudWatch Events this is not the best tool for monitoring application logs.

CloudTrail is used for monitoring API activity on your account, not for monitoring application logs.

CloudWatch Metrics are the fundamental concept in CloudWatch. A metric represents a time- ordered set of data points that are published to CloudWatch. You cannot use a metric alone; it is used when setting up monitoring for any service in CloudWatch.
```

**Question 3 answer: D,E**

Explanation:

```
AWS Serverless Application Model (AWS SAM) is an extension of AWS CloudFormation that is used to package, test, and deploy serverless applications.

With Amazon CloudWatch, you can access system metrics on all the AWS services you use, consolidate system and application level logs, and create business key performance indicators (KPIs) as custom metrics for your specific needs.

AWS Lambda is used for executing your code as functions, it is not used for packaging, testing and deployment. AWS Lambda is used with AWS SAM. 

AWS X-Ray lets you analyze and debug serverless applications by providing distributed tracing and service maps to easily identify performance bottlenecks by visualizing a request end-to-end.
```
**Question 4 answer: D**

Explanation:

```
When you provision your infrastructure with AWS CloudFormation, the AWS CloudFormation template describes exactly what resources are provisioned and their settings. Because these templates are text files, you simply track differences in your templates to track changes to your infrastructure, similar to the way developers control revisions to source code. For example, you can use a version control system with your templates so that you know exactly what changes were made, who made them, and when. If at any point you need to reverse changes to your infrastructure, you can use a previous version of your template.

AWS Systems Manager gives you visibility and control of your infrastructure on AWS. Systems Manager provides a unified user interface so you can view operational data from multiple AWS services and allows you to automate operational tasks across your AWS resources. However, CloudFormation would be the preferred method of maintaining the state of the overall architecture.

AWS CodeDeploy is a deployment service that automates application deployments to Amazon EC2 instances, on-premises instances, or serverless Lambda function.
AWS Trusted Advisor is an online resource to help you reduce cost, increase performance, and improve security by optimizing your AWS environment, Trusted Advisor provides real time guidance to help you provision your resources following AWS best practices.
```

**Question 5 answer: B,D**

Explanation:

```
Trails can be configured to log Data events and Management events:

- **Data events:** These events provide insight into the resource operations performed on or within a resource. These are also known as data plane operations
- **Management events:** Management events provide insight into management operations that are performed on resources in your AWS account. These are also known as control plane operations. Management events can also include non-API events that occur in your account

```

**Question 6 answer: C**

Explanation:

```
The only service that would allow you to continue to use the same tools is OpsWorks. AWS OpsWorks is a configuration management service that provides managed instances of Chef and Puppet. OpsWorks lets you use Chef and Puppet to automate how servers are configured, deployed, and managed across your Amazon EC2 instances or on-premises compute environments.
```

**Question 7 answer: B,E**

Explanation:

```
EC2 status checks are performed every minute and each returns a pass or a fail status. If all checks pass, the overall status of the instance is OK. If one or more checks fail, the overall status is impaired.

System status checks detect (StatusCheckFailed_System) problems with your instance that require AWS involvement to repair whereas Instance status checks (StatusCheckFailed_Instance) detect problems that require your involvement to repair.

The action to recover the instance is only supported on specific instance types and can be used only with StatusCheckFailed_System.

Configuring an action to terminate the instance would not help resolve system software issues as the instance would be terminated.
```