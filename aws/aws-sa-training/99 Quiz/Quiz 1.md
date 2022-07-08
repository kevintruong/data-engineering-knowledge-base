---
date created: 2022-07-05 23:40
---

## Quiz 1: An application is being created that will use Amazon EC2 instances to generate and store data. Another set of EC2 instances will then analyze and modify the data. Storage requirements will be significant and will continue to grow over time. The application architects require a storage solution.**

**Which actions would meet these needs?**

- [ ] Store the data in an Amazon EBS volume. Mount the EBS volume on the application instances
- [ ] Store the data in an Amazon EFS filesystem. Mount the file system on the application instances
- [ ] Store the data in Amazon S3 Glacier. Update the vault policy to allow access to the application instances
- [ ] Store the data in AWS Storage Gateway. Setup AWS Direct Connect between the Gateway appliance and the EC2 instances

---

Answer: 2
**Explanation:**
Amazon Elastic File System (Amazon EFS) provides a simple, scalable, fully managed elastic NFS file system for use with AWS Cloud services and on-premises resources. It is built to scale on demand to petabytes without disrupting applications, growing and shrinking automatically as you add and remove files, eliminating the need to provision and manage capacity to accommodate growth.

![](assets/fc31168a.png)

Amazon EFS supports the Network File System version 4 (NFSv4.1 and NFSv4.0) protocol. Multiple Amazon EC2 instances can access an Amazon EFS file system at the same time, providing a common data source for workloads and applications running on more than one instance or server. For this scenario, EFS is a great choice as it will provide a scalable file system that can be mounted by multiple EC2 instances and accessed simultaneously.

- ✅: "Store the data in an Amazon EFS filesystem. Mount the file system on the application instances" is the correct answer.

- ❌: "Store the data in an Amazon EBS volume. Mount the EBS volume on the application instances" is incorrect. Though there is a new feature that allows (EBS multi-attach) that allows attaching multiple Nitro instances to a volume, this is not on the exam yet, and has some specific constraints.

- ❌: "Store the data in Amazon S3 Glacier. Update the vault policy to allow access to the application instances" is incorrect as S3 Glacier is not a suitable storage location for live access to data, it is used for archival.

- ❌: "Store the data in AWS Storage Gateway. Setup AWS Direct Connect between the Gateway appliance and the EC2 instances" is incorrect. There is no reason to store the data on-premises in a Storage Gateway, using EFS is a much better solution.
  **References:**
  <https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html>
