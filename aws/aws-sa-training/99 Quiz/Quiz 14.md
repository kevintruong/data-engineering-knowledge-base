## Quiz 14: A team are planning to run analytics jobs on log files each day and require a storage solution. The size and number of logs is unknown and data will persist for 24 hours only.**

**What is the MOST cost-effective solution?**

- [ ] Amazon S3 Glacier Deep Archive

- [x] Amazon S3 Standard

- [ ] Amazon S3 Intelligent-Tiering

- [ ] Amazon S3 One Zone-Infrequent Access (S3 One Zone-IA)

----
Answer: 2

- [x] Amazon S3 Standard
  **Explanation:**
  S3 standard is the best choice in this scenario for a short term storage solution. In this case the size and number of logs is unknown and it would be difficult to fully assess the access patterns at this stage. Therefore, using S3 standard is best as it is cost-effective, provides immediate access, and there are no retrieval fees or minimum capacity charge per object.
- ✅: "Amazon S3 Standard" is the correct answer.

- ❌: "Amazon S3 Intelligent-Tiering" is incorrect as there is an additional fee for using this service and for a short-term requirement it may not be beneficial.

- ❌: "Amazon S3 One Zone-Infrequent Access (S3 One Zone-IA)" is incorrect as this storage class has a minimum capacity charge per object (128 KB) and a per GB retrieval fee.

- ❌: "Amazon S3 Glacier Deep Archive" is incorrect as this storage class is used for archiving data. There are retrieval fees and it take hours to retrieve data from an archive.
  **References:**
  https://aws.amazon.com/s3/storage-classes/



----
#quiz 
- relateTo:: [[Domain 4 Design Cost-Optimized Architectures]]