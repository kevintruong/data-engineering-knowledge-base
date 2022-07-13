**Explanation:**

EC2 Instance Stores are high-speed ephemeral storage that is physically attached to the EC2 instance. The i3.large

instance type comes with a single 475GB NVMe SSD instance store so it would be a good way to lower cost and improve

performance by using the attached instance store. As the files are temporary, it can be assumed that ephemeral storage (

which means the data is lost when the instance is stopped) is sufficient.

- ✅ :  "Move the temporary database onto instance storage" is the correct answer.

- ❌ :  "Put the temporary database on a new 50-GB EBS io1 volume with a 3000 IOPS allocation" is incorrect. Moving

  the DB to a new 50-GB EBS io1 volume with a 3000 IOPS allocation will improve performance but is more expensive so

  will not be the most cost-efficient solution.

- ❌ :  "Put the temporary database on a new 50-GB EBS gp2 volume" is incorrect. Moving the DB to a new 50-GB EBS

  gp2 volume will not result in a performance improvement as you get IOPS allocated per GB so a smaller volume will have

  lower performance.

- ❌ :  "Enable EBS optimization on the instance and keep the temporary files on the existing volume" is incorrect.

  Enabling EBS optimization will not lower cost. Also, EBS Optimization is a network traffic optimization, it does not

  change the I/O performance of the volume.

**References:**

<https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ebs/>

----

- #instance_storage #gb_nvme_ssd_instance_store #ec2_instance_stores #gb_ebs_io1_volume #ephemeral_storage
