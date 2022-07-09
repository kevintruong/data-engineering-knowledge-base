#### Question  23


**A high-performance file system is required for a financial modelling application. The data set will be stored on

Amazon S3 and the storage solution must have seamless integration so objects can be accessed as files.**


**Which storage solution should be used?**


1: Amazon FSx for Windows File Server


2: Amazon FSx for Lustre


3: Amazon Elastic File System (EFS)


4: Amazon Elastic Block Store (EBS)


Answer: 2


**Explanation:**


Amazon FSx for Lustre provides a high-performance file system optimized for fast processing of workloads such as machine

learning, high performance computing (HPC), video processing, financial modeling, and electronic design automation (EDA)

. Amazon FSx works natively with Amazon S3, letting you transparently access your S3 objects as files on Amazon FSx to

run analyses for hours to months.


- CORRECT "Amazon FSx for Lustre" is the correct answer.


- INCORRECT "Amazon FSx for Windows File Server" is incorrect. Amazon FSx for Windows File Server provides a fully

  managed native Microsoft Windows file system so you can easily move your Windows-based applications that require

  shared file storage to AWS. This solution integrates with Windows file shares, not with Amazon S3.


- INCORRECT "Amazon Elastic File System (EFS)" is incorrect. EFS and EBS are not good use cases for this solution.

  Neither storage solution is capable of presenting Amazon S3 objects as files to the application.


- INCORRECT "Amazon Elastic Block Store (EBS)" is incorrect. EFS and EBS are not good use cases for this solution.

  Neither storage solution is capable of presenting Amazon S3 objects as files to the application.


**References:**


https://aws.amazon.com/fsx/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-fsx/

