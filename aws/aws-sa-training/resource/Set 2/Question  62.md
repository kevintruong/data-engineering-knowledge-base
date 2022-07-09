#### Question  62


**A data-processing application runs on an i3.large EC2 instance with a single 100 GB EBS gp2 volume. The application

stores temporary data in a small database (less than 30 GB) located on the EBS root volume. The application is

struggling to process the data fast enough, and a Solutions Architect has determined that the I/O speed of the temporary

database is the bottleneck.**


**What is the MOST cost-efficient way to improve the database response times?**


1: Put the temporary database on a new 50-GB EBS io1 volume with a 3000 IOPS allocation


2: Move the temporary database onto instance storage


3: Put the temporary database on a new 50-GB EBS gp2 volume


4: Enable EBS optimization on the instance and keep the temporary files on the existing volume


Answer: 2


**Explanation:**


EC2 Instance Stores are high-speed ephemeral storage that is physically attached to the EC2 instance. The i3.large

instance type comes with a single 475GB NVMe SSD instance store so it would be a good way to lower cost and improve

performance by using the attached instance store. As the files are temporary, it can be assumed that ephemeral storage (

which means the data is lost when the instance is stopped) is sufficient.


- CORRECT "Move the temporary database onto instance storage" is the correct answer.


- INCORRECT "Put the temporary database on a new 50-GB EBS io1 volume with a 3000 IOPS allocation" is incorrect. Moving

  the DB to a new 50-GB EBS io1 volume with a 3000 IOPS allocation will improve performance but is more expensive so

  will not be the most cost-efficient solution.


- INCORRECT "Put the temporary database on a new 50-GB EBS gp2 volume" is incorrect. Moving the DB to a new 50-GB EBS

  gp2 volume will not result in a performance improvement as you get IOPS allocated per GB so a smaller volume will have

  lower performance.


- INCORRECT "Enable EBS optimization on the instance and keep the temporary files on the existing volume" is incorrect.

  Enabling EBS optimization will not lower cost. Also, EBS Optimization is a network traffic optimization, it does not

  change the I/O performance of the volume.


**References:**


https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ebs/

