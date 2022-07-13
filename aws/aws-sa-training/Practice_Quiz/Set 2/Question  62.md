#### Question  62

**A data-processing application runs on an i3.large EC2 instance with a single 100 GB EBS gp2 volume. The application

stores temporary data in a small database (less than 30 GB) located on the EBS root volume. The application is

struggling to process the data fast enough, and a Solutions Architect has determined that the I/O speed of the temporary

database is the bottleneck.**

**What is the MOST cost-efficient way to improve the database response times?**

- [ ] :  Put the temporary database on a new 50-GB EBS io1 volume with a 3000 IOPS allocation

- [x] :  Move the temporary database onto instance storage

- [ ] :  Put the temporary database on a new 50-GB EBS gp2 volume

- [ ] :  Enable EBS optimization on the instance and keep the temporary files on the existing volume

----

- #ebs_optimization #i3.large_ec2_instance #instance_storage #gb_ebs_io1_volume #temporary_database
- hasExplain:: [[explanation_Question  62.md]]
