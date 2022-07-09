#### Question  63


**A Solutions Architect needs to create a file system that can be concurrently accessed by multiple Amazon EC2 instances

across multiple availability zones. The file system needs to support high throughput and the ability to burst. As the

data that will be stored on the file system will be sensitive, it must be encrypted at rest and in transit.**


**Which storage solution should the Solutions Architect use for the shared file system?**


- [ ] Add EBS volumes to each EC2 instance and configure data replication


- [ ] Use the Elastic Block Store (EBS) and mount the file system at the block level


- [x] Use the Elastic File System (EFS) and mount the file system using NFS


- [ ] Add EBS volumes to each EC2 instance and use an ELB to distribute data evenly between the volumes


*