#### Question  19


**An application allows users to upload and download files. Files older than 2 years will be accessed less frequently. A

solutions architect needs to ensure that the application can scale to any number of files while maintaining high

availability and durability.**


**Which scalable solutions should the solutions architect recommend?**


- [x] Store the files on Amazon S3 with a lifecycle policy that moves objects older than 2 years to S3 Standard Infrequent

Access (S3 Standard-IA)


- [ ] Store the files on Amazon Elastic File System (EFS) with a lifecycle policy that moves objects older than 2 years to

EFS Infrequent Access (EFS IA)


- [ ] Store the files in Amazon Elastic Block Store (EBS) volumes. Schedule snapshots of the volumes. Use the snapshots to

archive data older than 2 years


- [ ] Store the files in Amazon Elastic Block Store (EBS) volumes. Create a lifecycle policy to move files older than 2

years to Amazon S3 Glacier



- hasExplain:: [[explanation_Question  19.md]]