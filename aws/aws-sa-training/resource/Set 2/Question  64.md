#### Question  64


**An EC2 instance that you manage has an IAM role attached to it that provides it with access to Amazon S3 for saving

log data to a bucket. A change in the application architecture means that you now need to provide the additional ability

for the application to securely make API requests to Amazon API Gateway.**


**Which two methods could you use to resolve this challenge? (Select TWO)**


1: Delegate access to the EC2 instance from the API Gateway management console


2: Create an IAM role with a policy granting permissions to Amazon API Gateway and add it to the EC2 instance as an

additional IAM role


3: You cannot modify the IAM role assigned to an EC2 instance after it has been launched. You’ll need to recreate the

EC2 instance and assign a new IAM role


4: Add an IAM policy to the existing IAM role that the EC2 instance is using granting permissions to access Amazon API

Gateway


5: Create a new IAM role with multiple IAM policies attached that grants access to Amazon S3 and Amazon API Gateway, and

replace the existing IAM role that is attached to the EC2 instance


Answer: 4,5


**Explanation:**


There are two possible solutions here. In one you create a new IAM role with multiple policies, in the other you add a

new policy to the existing IAM role.


Contrary to one of the incorrect answers, you **can** modify IAM roles after an instance has been launched – this was

changed quite some time ago now. However, you **cannot** add multiple IAM roles to a single EC2 instance. If you need to

attach multiple policies you must attach them to a single IAM role. There is no such thing as delegating access using

the API Gateway management console.


- CORRECT "Add an IAM policy to the existing IAM role that the EC2 instance is using granting permissions to access

  Amazon API Gateway" is the correct answer.


- CORRECT "Create a new IAM role with multiple IAM policies attached that grants access to Amazon S3 and Amazon API

  Gateway, and replace the existing IAM role that is attached to the EC2 instance" is the correct answer.


- INCORRECT "Delegate access to the EC2 instance from the API Gateway management console" is incorrect as you cannot

  delegate in this manner.


- INCORRECT "Create an IAM role with a policy granting permissions to Amazon API Gateway and add it to the EC2 instance

  as an additional IAM role" is incorrect as you cannot attach an additional IAM role, you can only have one attached to

  an instance at a time.


- INCORRECT "You cannot modify the IAM role assigned to an EC2 instance after it has been launched. You’ll need to

  recreate the EC2 instance and assign a new IAM role" is incorrect as this statement is incorrect, you can.


**References:**


https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ec2/

