---
date created: 2022-07-05 23:16
---

## Quiz 5: A company is migrating from an on-premises infrastructure to the AWS Cloud. One of the company's applications stores files on a Windows file server farm that uses Distributed File System Replication (DFSR)

to keep data in sync. A solutions architect needs to replace the file server farm.**
**Which service should the solutions architect use?**

- [ ] Amazon EFS
- [ ] Amazon FSx
- [ ] Amazon S3
- [ ] AWS Storage Gateway

---

**Explanation:**
Amazon FSx for Windows File Server provides fully managed, highly reliable file storage that is accessible over the industry-standard Server Message Block (SMB) protocol. Amazon FSx is built on Windows Server and provides a rich set of administrative features that include end-user file restore, user quotas, and Access Control Lists (ACLs). Additionally, Amazon FSX for Windows File Server supports Distributed File System Replication (DFSR) in both Single-AZ and Multi-AZ deployments as can be seen in the feature comparison table below.
![](assets/55c89abf.png)

- ✅: "Amazon FSx" is the correct answer.
- ❌: "Amazon EFS" is incorrect as EFS only supports Linux systems.
- ❌: "Amazon S3" is incorrect as this is not a suitable replacement for a Microsoft filesystem.
- ❌: "AWS Storage Gateway" is incorrect as this service is primarily used for connecting on-premises storage to cloud storage. It consists of a software device installed on-premises and can be used with SMB shares but it actually stores the data on S3. It is also used for migration. However, in this case the company need to replace the file server farm and Amazon FSx is the best choice for this job.
  **References:**
  <https://docs.aws.amazon.com/fsx/latest/WindowsGuide/high-availability-multiAZ.html>
  
----
#quiz 
- relateTo:: [[Domain 1 Design Resilient Architectures]]
