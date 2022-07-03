### **An Architect is designing an application that will use hundreds of EC2 instances across multiple availability zones. A shared filesystem is required that can be mounted by all instances. Which storage service is suitable for this requirement?**

- [x] Amazon Elastic File System (EFS)
- [ ] Amazon Elastic Block Store (EBS)
- [ ] Amazon Instance Store
- [ ] Amazon Simple Storage Service (S3)

----


**Answer:**

Amazon Elastic File System (EFS)

**Explanation:**

- Amazon Elastic File System (EFS) is correct. EFS is a file-based storage system accessed over NFS. You can attach thousands of instances from multiple AZs to the same filesystem.
- Amazon Elastic Block Store (EBS) is incorrect. You cannot attach multiple instances to a single EBS volume or attach volumes across AZs.
- Amazon Instance Store is incorrect. Instance Stores are local storage on the EC2 host servers, you cannot attach multiple instances to the same instance store.
- Amazon Simple Storage Service (S3) is incorrect. Amazon S3 is an object-based storage system, not a filesystem.

---- 
#quiz 