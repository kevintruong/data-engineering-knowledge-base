#### Question  10


**A company's web application is using multiple Amazon EC2 Linux instances and storing data on Amazon EBS volumes. The

company is looking for a solution to increase the resiliency of the application in case of a failure. What should a

solutions architect do to meet these requirements?**


1: Launch the application on EC2 instances in each Availability Zone. Attach EBS volumes to each EC2 instance


2: Create an Application Load Balancer with Auto Scaling groups across multiple Availability Zones. Mount an instance

store on each EC2 instance


3: Create an Application Load Balancer with Auto Scaling groups across multiple Availability Zones. Store data on Amazon

EFS and mount a target on each instance


4: Create an Application Load Balancer with Auto Scaling groups across multiple Availability Zones. Store data using

Amazon S3 One Zone-Infrequent Access (S3 One Zone-A)


Answer: 3


**Explanation:**


To increase the resiliency of the application the solutions architect can use Auto Scaling groups to launch and

terminate instances across multiple availability zones based on demand. An application load balancer (ALB)

can be used to direct traffic to the web application running on the EC2 instances.


Lastly, the Amazon Elastic File System (EFS) can assist with increasing the resilience of the application by providing a

shared file system that can be mounted by multiple EC2 instances from multiple availability zones.


- CORRECT "Create an Application Load Balancer with Auto Scaling groups across multiple Availability Zones. Store data

  on Amazon EFS and mount a target on each instance" is the correct answer.


- INCORRECT "Launch the application on EC2 instances in each Availability Zone. Attach EBS volumes to each EC2 instance"

  is incorrect as the EBS volumes are single points of failure which are not shared with other instances.


- INCORRECT "Create an Application Load Balancer with Auto Scaling groups across multiple Availability Zones. Mount an

  instance store on each EC2 instance" is incorrect as instance stores are ephemeral data stores which means data is

  lost when powered down. Also, instance stores cannot be shared between instances.


- INCORRECT "Create an Application Load Balancer with Auto Scaling groups across multiple Availability Zones. Store data

  using Amazon S3 One Zone-Infrequent Access (S3 One Zone-IA)" is incorrect as there are data retrieval charges

  associated with this S3 tier. It is not a suitable storage tier for application files.


**References:**


https://docs.aws.amazon.com/efs/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-efs/

