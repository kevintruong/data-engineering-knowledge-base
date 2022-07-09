#### Question  47


**A Solutions Architect is writing some code that uses an AWS Lambda function and would like to enable the function to

connect to an Amazon ElastiCache cluster within an Amazon VPC in the same AWS account. What VPC-specific information

must be included in the function to enable this configuration? (Select TWO)**


1: VPC Subnet IDs


2: VPC Logical IDs


3: VPC Peering IDs


4: VPC Security Group IDs


5: VPC Route Table IDs


**Answer: 1,4**


**Explanation:**


To enable your Lambda function to access resources inside your private VPC, you must provide additional VPC- specific

configuration information that includes VPC subnet IDs and security group IDs. AWS Lambda uses this information to set

up elastic network interfaces (ENIs) that enable your function.


Please see the AWS article linked below for more details on the requirements


- CORRECT "VPC Subnet IDs" is the correct answer.


- CORRECT "VPC Security Group IDs" is the correct answer.


- INCORRECT "VPC Logical IDs" is incorrect as this is not required.


- INCORRECT "VPC Peering IDs" is incorrect as this is not required.


- INCORRECT "VPC Route Table IDs" is incorrect as this is not required.


**References:**


https://docs.aws.amazon.com/lambda/latest/dg/vpc.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/aws-lambda/

