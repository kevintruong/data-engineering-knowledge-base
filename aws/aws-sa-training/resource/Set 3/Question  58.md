#### Question  58


**You are deploying an application on Amazon EC2 that must call AWS APIs. Which method of securely passing credentials

to the application should you use?**


1: Store the API credentials on the instance using instance metadata


2: Store API credentials as an object in Amazon S3


3: Embed the API credentials into your application files


4: Assign IAM roles to the EC2 instances


Answer: 4


**Explanation:**


Applications must sign their API requests with AWS credentials. Therefore, if you are an application developer, you need

a strategy for managing credentials for your applications that run on EC2 instances. For example, you can securely

distribute your AWS credentials to the instances, enabling the applications on those instances to use your credentials

to sign requests, while protecting your credentials from other users.


However, it's challenging to securely distribute credentials to each instance, especially those that AWS creates on your

behalf, such as Spot Instances or instances in Auto Scaling groups. You must also be able to update the credentials on

each instance when you rotate your AWS credentials.


IAM roles enable your applications to securely make API requests from your instances, without requiring you to manage

the security credentials that the applications use. Instead of creating and distributing your AWS credentials, you can

delegate permission to make API requests using IAM roles.


- CORRECT "Assign IAM roles to the EC2 instances" is the correct answer.


- INCORRECT "Store the API credentials on the instance using instance metadata" is incorrect. It is an AWS best practice

  not to store API credentials within applications, on file systems or on instances (such as in metadata).


- INCORRECT "Store API credentials as an object in Amazon S3" is incorrect. It is an AWS best practice not to store API

  credentials within applications, on file systems or on instances (such as in metadata).


- INCORRECT "Embed the API credentials into your application files" is incorrect. It is an AWS best practice not to

  store API credentials within applications, on file systems or on instances (such as in metadata).


**References:**


https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/security-identity-

compliance/aws-iam/

