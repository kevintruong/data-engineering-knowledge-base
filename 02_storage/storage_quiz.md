## Storage Quiz Questions

Answers and explanations are provided below after the last question in this section.

### **You would like to run some code when an object is uploaded to an Amazon S3 bucket. How can this be achieved?**

- [x] Create an event notification on the S3 bucket that triggers a Lambda function
- [ ] Configure Lambda to poll the S3 bucket for changes and run a function when it finds new objects
- [ ] Create an event notification on the S3 bucket that notifies Amazon SNS to trigger a Lambda function

----

**Answer:**
Create an event notification on the S3 bucket that triggers a Lambda function

**Explanation:**

- Create an event notification on the S3 bucket that triggers a Lambda function is correct. The best way to achieve this is to use an event notification on the S3 bucket that triggers a function that then runs the code.
- Configure Lambda to poll the S3 bucket for changes and run a function when it finds new objects is incorrect. Lambda does not poll S3.
- Create an event notification on the S3 bucket that notifies Amazon SNS to trigger a Lambda function is incorrect. You would not use Amazon SNS in this scenario as it is an unnecessary additional step.

### **Which type Amazon storage service uses standards-based REST web interfaces to manage objects?**

- [ ] Amazon Elastic File System (EFS)
- [ ] Amazon Elastic Block Store (EBS)
- [x] Amazon Simple Storage Service (S3)
- [ ] Amazon FSx for Windows File Server

----
**Answer: 3**

Amazon Simple Storage Service (S3)

**Explanation:**

- Amazon Elastic File System (EFS): is incorrect. EFS is a file-based storage system that is accessed using the NFS protocol.
- Amazon Elastic Block Store (EBS): is incorrect. EBS is a block-based storage system for mounting volumes.
- Amazon Simple Storage Service (S3): is correct. Amazon S3 is an object-based storage system that uses standards-based REST web interfaces to work with objects.
- Amazon FSx for Windows File Server is incorrect. Amazon FSx for Windows File Server provides a fully managed Microsoft filesystem that is mounted using SMB.

### **What is the maximum file size allowed in Amazon S3?**

- [ ] 5 terabytes
- [ ] 0 bytes
- [ ] 5 gigabytes
- [ ] Unlimited

----


**Answer:**

5 terabytes

**Explanation:**

- 5 terabytes is correct. The maximum file size for Amazon S3 objects is 5 terabytes.
- 0 bytes is incorrect. This is the minimum file size possible in Amazon S3.
- 5 gigabytes is incorrect. 5GB is not the maximum file size possible in Amazon S3.
- unlimited is incorrect. There is a limit on the maximum file size for objects in Amazon S3.

### **What type of consistency model is provided in Amazon S3 when you upload a new version of an object?**

- [ ] Read after write consistency
- [x] Eventual consistency

----

**Answer:**

Eventual consistency

**Explanation:**

- Read after write consistency is incorrect. You do not get read after write consistency for overwrite PUT and DELETES.
- Eventual consistency is correct. In Amazon S3 you get eventual consistency for overwrite PUTS and DELETES.

### **Which Amazon S3 capability uses Amazon CloudFront and enables fast uploads for objects?**

- [ ] Multipart upload
- [ ] Cross region replication (CRR)
- [ ] BitTorrent
- [x] Transfer acceleration

**Answer: 4**

Transfer acceleration

**Explanation:**

- Multipart upload is incorrect. Multipart upload is recommended for uploading objects larger than 100MB but it does not use CloudFront.
- Cross region replication (CRR) is incorrect. CRR is used for replicating objects between buckets in different regions.
- BitTorrent is incorrect. BitTorrent can be used for retrieving objects from Amazon S3.It is not used for uploading and doesn’t use CloudFront.
- Transfer acceleration is correct. Transfer Acceleration speeds up data uploads by using the CloudFront network.

### **How can you create a hierarchy that mimics a filesystem in Amazon S3?**

- [ ] Create buckets within other buckets
- [x] Use folders in your buckets
- [ ] Upload objects within other objects
- [ ] Use lifecycle rules to tier your data

---- 
**Answer: 2**

**Explanation:**

- Create buckets within other buckets is incorrect. You cannot nest buckets (create buckets inside other buckets).
- Use folders in your buckets is correct. You can mimic the hierarchy of a filesystem by creating folder in your buckets.
- Upload objects within other objects is incorrect. You cannot upload objects within other objects.
- Use lifecycle rules to tier your data is incorrect. Tiering your data is done for performance not to mimic a filesystem.

### **A US based organization is concerned about uploading data to Amazon S3 as data sovereignty rules mean they cannot move their data outside of the US. What would you tell them?**

- [ ] Data never leaves a region unless specifically configured to do so.
- [ ] Data will be replicated globally so they cannot use Amazon S3.

---- 

**Answer: 1**

Data never leaves a region unless specifically configured to do so.

**Explanation:**

- Data never leaves a region unless specifically configured to do so is correct. S3 is a global service but buckets are created within a region. Data is never replicated outside of that region unless you configure it (e.g. through CRR).
- Data will be replicated globally so they cannot use Amazon S3 is incorrect. Data is not replicated globally with Amazon S3.

### **For compliance reasons, an organization needs to retain data for 7 years. If they need to retrieve data, they have 24 hours to do so. Which Amazon S3 storage class is most cost- effective?**

- [ ] Amazon S3 One-Zone IA
- [ ] Amazon S3 Intelligent Tiering
- [ ] Amazon S3 Glacier
- [ ] Amazon S3 Glacier Deep Archive

----

**Answer:**

Amazon S3 Glacier Deep Archive

**Explanation:**

- Amazon S3 One-Zone IA is incorrect. This is not the most cost-effective option for these requirements.
- Amazon S3 Intelligent Tiering is incorrect. This is not the most cost-effective option for these requirements.
- Amazon S3 Glacier is incorrect. This is not the most cost-effective option for these requirements. It is slightly more expensive than Deep Archive but faster to retrieve data (which isn’t necessary for this scenario).
- Amazon S3 Glacier Deep Archive is correct. This is the most cost-effective option for these requirements as the data retrieval time is 24 hours.

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

### **How can you control access to files and directories in Amazon EFS filesystems?**

- [ ] Using IAM
- [ ] Using EFS security groups
- [ ] Using Network ACLs
- [x] Using user and group-level permissions

----

**Answer**

Using user and group-level permissions

**Explanation:**

- Using IAM is incorrect. iam can be used to control who can administer the file system but not control the access to files and directories.
- Using EFS security groups is incorrect. efs security groups control network traffic that is allowed to reach the filesystem.
- Using Network ACLs is incorrect. network acls are not used for file and directory permissions, they restrict traffic into and out of subnets.
- Using user and group-level permissions is correct. you can control access to files and directories with posix-compliant user and group- level permissions.

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

### **Which AWS storage service provides a NTFS filesystem that can be accessed by multiple EC2 instances using the SMB protocol?**

- [x] Amazon FSx for Windows File Server
- [ ] Amazon Elastic File System (EFS)
- [ ] Amazon FSx for Lustre
- [ ] Amazon Elastic Block Store (EBS)

---- 

**Question 12**

Amazon FSx for Windows File Server

**Explanation:**

- Amazon FSx for Windows File Server is correct. FSx for Windows File Server provides NTFS file systems that can be accessed from up to thousands of compute instances using the SMB protocol.
- Amazon Elastic File System (EFS) is incorrect. EFS is not an NTFS filesystem.
- Amazon FSx for Lustre is incorrect. FSx for Lustre does not provide an NTFS filesystem.
- Amazon Elastic Block Store (EBS) is incorrect. EBS does not provide an NTFS filesystem nor can it be accessed by multiple EC2 instances.