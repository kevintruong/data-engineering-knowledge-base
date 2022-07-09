#### Question  30


**A client has made some updates to their web application. The application uses an Auto Scaling Group to maintain a

group of several EC2 instances. The application has been modified and a new AMI must be used for launching any new

instances.**


**What does a Solutions Architect need to do to add the new AMI?**


1: Create a new target group that uses a new launch configuration with the new AMI


2: Modify the existing launch configuration to add the new AMI


3: Suspend Auto Scaling and replace the existing AMI


4: Create a new launch configuration that uses the AMI and update the ASG to use the new launch configuration


**Answer: 4**


**Explanation:**


A launch configuration is the template used to create new EC2 instances and includes parameters such as instance family,

instance type, AMI, key pair and security groups.


You cannot edit a launch configuration once defined. In this case you can create a new launch configuration that uses

the new AMI and any new instances that are launched by the ASG will use the new AMI.


- CORRECT "Create a new launch configuration that uses the AMI and update the ASG to use the new launch configuration"

  is the correct answer.


- INCORRECT "Create a new target group that uses a new launch configuration with the new AMI" is incorrect. A target

  group is a concept associated with an ELB not Auto Scaling.


- INCORRECT "Modify the existing launch configuration to add the new AMI" is incorrect as you cannot modify an existing

  launch configuration.


- INCORRECT "Suspend Auto Scaling and replace the existing AMI" is incorrect. Suspending scaling processes can be useful

  when you want to investigate a configuration problem or other issue with your web application and then make changes to

  your application, without invoking the scaling processes. It is not useful in this situation.


**References:**


https://docs.aws.amazon.com/autoscaling/ec2/userguide/LaunchConfiguration.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ebs/

