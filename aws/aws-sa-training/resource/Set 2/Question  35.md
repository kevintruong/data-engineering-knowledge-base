#### Question  35


**A company’s Amazon EC2 instances were terminated or stopped, resulting in a loss of important data that was stored on

attached EC2 instance stores. They want to avoid this happening in the future and need a solution that can scale as data

volumes increase with the LEAST amount of management and configuration.**


**Which storage is most appropriate?**


1: Amazon EFS


2: Amazon S3


3: Amazon EBS


4: Amazon RDS


Answer: 1


**Explanation:**


Amazon EFS is a fully managed service that requires no changes to your existing applications and tools, providing access

through a standard file system interface for seamless integration. It is built to scale on demand to petabytes without

disrupting applications, growing and shrinking automatically as you add and remove files. This is an easy solution to

implement and the option that requires the least management and configuration.


An instance store provides temporary block-level storage for an EC2 instance. If you terminate the instance you lose all

data. The alternative is to use Elastic Block Store volumes which are also block-level storage devices but the data is

persistent. However, EBS is not a fully managed solution and doesn’t grow automatically as your data requirements

increase – you would need to increase the volume size and then extend your filesystem.


- CORRECT "Amazon EFS" is the correct answer.


- INCORRECT "Amazon S3" is incorrect. Amazon S3 is an object storage solution and as the data is currently sitting on a

  block storage you would need to develop some way to use the REST API to upload/manage data on S3 – this is not the

  easiest solution to implement.


- INCORRECT "Amazon EBS" is incorrect as EBS is not a fully managed solution and doesn’t grow automatically as your data

  requirements increase – you would need to increase the volume size and then extend your filesystem.


- INCORRECT "Amazon RDS" is incorrect. Amazon RDS is a relational database service, the question is not looking for a

  database, just a way of storing data.


**References:**


https://aws.amazon.com/efs/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-efs/

