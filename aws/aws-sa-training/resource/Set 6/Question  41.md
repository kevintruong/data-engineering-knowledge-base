#### Question  41


**A Solutions Architect has logged into an Amazon EC2 Linux instance using SSH and needs to determine a few pieces of

information including what IAM role is assigned, the instance ID and the names of the security groups that are assigned

to the instance.**


**From the options below, what would be the best source of this information?**


1: Metadata


2: Tags


3: User data


4: Parameters


**Answer:**


**Explanation:**


_Instance metadata_ is data about your instance that you can use to configure or manage the running instance. Instance

metadata is divided into categories, for example, host name, events, and security groups.


Instance metadata is available at [http://169.254.169.254/latest/meta-data.](http://169.254.169.254/latest/meta-data.)


- CORRECT "Metadata" is the correct answer.


- INCORRECT "Tags" is incorrect. Tags are used to categorize and label resources.


- INCORRECT "User data" is incorrect. User data is used to configure the system at launch time and specify scripts.


- INCORRECT "Parameters" is incorrect. Parameters are used in databases.


**References:**


https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ec2/

