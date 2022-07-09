#### Question  61


**Developers regularly create and update CloudFormation stacks using API calls. For security reasons you need to ensure

that users are restricted to a specified template. How can this be achieved?**


1: Store the template on Amazon S3 and use a bucket policy to restrict access


2: Create an IAM policy with a Condition: ResourceTypes parameter


3: Create an IAM policy with a Condition: TemplateURL parameter


4: Create an IAM policy with a Condition: StackPolicyURL parameter


Answer: 3


**Explanation:**


The cloudformation:TemplateURL, lets you specify where the CloudFormation template for a stack action, such as create or

update, resides and enforce that it be used.


- CORRECT "Create an IAM policy with a Condition: TemplateURL parameter" is the correct answer.


- INCORRECT "Store the template on Amazon S3 and use a bucket policy to restrict access" is incorrect. Configuring a

  bucket policy on the Amazon S3 bucket where you place your templates is a good idea, but it does not enforce

  CloudFormation create and update API requests to use the templates in the bucket.


- INCORRECT "Create an IAM policy with a Condition: ResourceTypes parameter" is incorrect. The CloudFormation API

  accepts a ResourceTypes parameter. In your API call, you specify which types of resources can be created or updated.

  This does not control which template is used.


- INCORRECT "Create an IAM policy with a Condition: StackPolicyURL parameter" is incorrect. You can ensure that every

  CloudFormation stack has a stack policy associated with it upon creation with the StackPolicyURL condition. However,

  this parameter itself is not used to specify the template to use.


**References:**


https://aws.amazon.com/blogs/devops/aws-cloudformation-security-best-practices/


https://aws.amazon.com/cloudformation/aws-cloudformation-templates/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/management-tools/aws-

cloudformation/

