**Explanation:**

To increase the resiliency of the application the solutions architect can use Auto Scaling groups to launch and

terminate instances across multiple availability zones based on demand. An application load balancer (ALB)

can be used to direct traffic to the web application running on the EC2 instances.

Lastly, the Amazon Elastic File System (EFS) can assist with increasing the resilience of the application by providing a

shared file system that can be mounted by multiple EC2 instances from multiple availability zones.

- ✅ :  "Create an Application Load Balancer with Auto Scaling groups across multiple Availability Zones. Store data

  on Amazon EFS and mount a target on each instance" is the correct answer.

- ❌ :  "Launch the application on EC2 instances in each Availability Zone. Attach EBS volumes to each EC2 instance"

  is incorrect as the EBS volumes are single points of failure which are not shared with other instances.

- ❌ :  "Create an Application Load Balancer with Auto Scaling groups across multiple Availability Zones. Mount an

  instance store on each EC2 instance" is incorrect as instance stores are ephemeral data stores which means data is

  lost when powered down. Also, instance stores cannot be shared between instances.

- ❌ :  "Create an Application Load Balancer with Auto Scaling groups across multiple Availability Zones. Store data

  using Amazon S3 One Zone-Infrequent Access (S3 One Zone-IA)" is incorrect as there are data retrieval charges

  associated with this S3 tier. It is not a suitable storage tier for application files.

**References:**

<https://docs.aws.amazon.com/efs/>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-efs/>

----

- #multiple_ec2_instances #amazon_elastic_file_system #ec2_instances #multiple_availability_zones #ec2_instance
