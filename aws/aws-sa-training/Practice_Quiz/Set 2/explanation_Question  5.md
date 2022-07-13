**Explanation:**

Amazon EFS is a fully-managed service that makes it easy to set up, scale, and cost-optimize file storage in the Amazon

Cloud. EFS file systems are accessible to Amazon EC2 instances via a file system interface (using standard operating

system file I/O APIs) and support full file system access semantics (such as strong consistency and file locking).

EFS is a good solution for when you need to attach a shared filesystem to multiple EC2 instances across multiple

Availability Zones.

- ✅ :  "Create an Amazon Elastic File System (Amazon EFS) file system and mount it on the individual Amazon EC2

  instances" is the correct answer.

- ❌ :  "Create an Amazon S3 bucket to store the web content and use Amazon CloudFront to deliver the content" is

  incorrect as this may require more effort in terms of reprogramming the application to use the S3 API.

- ❌ :  "Create a shared Amazon Block Store (Amazon EBS) volume and mount it on the individual Amazon EC2 instances"

  is incorrect. Please note that you can multi-attach an EBS volume to multiple EC2 instances but the instances must be

  in the same AZ.

- ❌ :  "Create a volume gateway using AWS Storage Gateway to host the data and mount it to the Auto Scaling group"

  is incorrect as a storage gateway is used on-premises.

**References:**

<https://aws.amazon.com/efs/faq/>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-efs/>

----

- #amazon_elastic_file_system #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-efs/> #individual_amazon_ec2 #amazon_efs #<https://aws.amazon.com/efs/faq/>
