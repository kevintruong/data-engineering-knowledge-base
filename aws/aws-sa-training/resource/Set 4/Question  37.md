#### Question  37


**A Solutions Architect is creating an AWS CloudFormation template that will provision a new EC2 instance and new EBS

volume. What must be specified to associate the block store with the instance?**


1: Both the EC2 physical ID and the EBS physical ID


2: The EC2 physical ID


3: Both the EC2 logical ID and the EBS logical ID


4: The EC2 logical ID


**Answer: 3**


**Explanation:**


The logical ID is used to reference the resource in parts of the template. For example, if you want to map an Amazon

Elastic Block Store volume to an Amazon EC2 instance, you reference the logical IDs to associate the block stores with

the instance.


In addition to the logical ID, certain resources also have a physical ID, which is the actual assigned name for that

resource, such as an EC2 instance ID or an S3 bucket name. Use the physical IDs to identify resources outside of AWS

CloudFormation templates, but only after the resources have been created.


Think of logical IDs as being used to reference resources within the template and Physical IDs being used to identify

resources outside of AWS CloudFormation templates after they have been created.


- CORRECT "Both the EC2 logical ID and the EBS logical ID" is the correct answer.


- INCORRECT "Both the EC2 physical ID and the EBS physical ID" is incorrect as logical IDs can be used within the

  template.


- INCORRECT "The EC2 physical ID" is incorrect as logical IDs can be used.


- INCORRECT "The EC2 logical ID" is incorrect as the EBS logical ID should also be specified.


**References:**


https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resources-section-structure.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/management-tools/aws-

cloudformation/

