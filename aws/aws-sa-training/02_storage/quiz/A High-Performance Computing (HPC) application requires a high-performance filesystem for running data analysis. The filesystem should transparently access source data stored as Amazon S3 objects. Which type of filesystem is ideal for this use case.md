### **A High-Performance Computing (HPC) application requires a high-performance filesystem for running data analysis. The filesystem should transparently access source data stored as Amazon S3 objects. Which type of filesystem is ideal for this use case?**

- [ ] Amazon FSx for Windows File Server
- [ ] Amazon Elastic File System (EFS)
- [x] Amazon FSx for Lustre
- [ ] Amazon Elastic Block Store (EBS)

---- 

**Answer: 3**

Amazon FSx for Lustre

**Explanation:**

- Amazon FSx for Windows File Server is incorrect. FSx for Windows File Server cannot access data stored on Amazon S3.
- Amazon Elastic File System (EFS) is incorrect. EFS does not integrate with Amazon S3 to transparently access objects.
- Amazon FSx for Lustre is correct. This is a good use case for Amazon FSx for Lustre.
- Amazon Elastic Block Store (EBS) is incorrect. EBS is not a filesystem nor does it directly integrate with Amazon S3 for transparent access of S3 objects.


---- 
#quiz 