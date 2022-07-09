#### Question  27


**Amazon EC2 instances in a development environment run between 9am and 5pm Monday-Friday. Production instances run

24/7. Which pricing models should be used? (Select TWO)**


1: Use Spot instances for the development environment


2: Use Reserved instances for the development environment


3: Use scheduled reserved instances for the development environment


4: Use Reserved instances for the production environment


5: Use On-Demand instances for the production environment


Answer: 3,4


**Explanation:**


Scheduled Instances are a good choice for workloads that do not run continuously but do run on a regular schedule. This

is ideal for the development environment.


Reserved instances are a good choice for workloads that run continuously. This is a good option for the production

environment**.**


- CORRECT "Use scheduled reserved instances for the development environment" is a correct answer.


- CORRECT "Use Reserved instances for the production environment" is also a correct answer.


- INCORRECT "Use Spot instances for the development environment" is incorrect. Spot Instances are a cost- effective

  choice if you can be flexible about when your applications run and if your applications can be interrupted. Spot

  instances are not suitable for the development environment as important work may be interrupted.


- INCORRECT "Use Reserved instances for the development environment" is incorrect as they should be used for the

  production environment.


- INCORRECT "Use On-Demand instances for the production environment" is incorrect. There is no long-term commitment

  required when you purchase On-Demand Instances. However, you do not get any discount and therefore this is the most

  expensive option.


**References:**


https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/instance-purchasing-options.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ec2/

