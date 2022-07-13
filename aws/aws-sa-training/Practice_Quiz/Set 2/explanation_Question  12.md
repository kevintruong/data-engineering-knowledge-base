**Explanation:**

Amazon FSx for Lustre provides a high-performance file system optimized for fast processing of workloads such as machine

learning, high performance computing (HPC), video processing, financial modeling, and electronic design automation (EDA)

.

These workloads commonly require data to be presented via a fast and scalable file system interface, and typically have

data sets stored on long-term data stores like Amazon S3.

Amazon FSx works natively with Amazon S3, making it easy to access your S3 data to run data processing workloads. Your

S3 objects are presented as files in your file system, and you can write your results back to S3. This lets you run data

processing workloads on FSx for Lustre and store your long-term data on S3 or on- premises data stores.

Therefore, the best combination for this scenario is to use S3 for cold data and FSx for Lustre for the parallel HPC

job.

- ✅ :  "Amazon S3 for cold data storage" is the correct answer.

- ✅ :  "Amazon FSx for Lustre for high-performance parallel storage" is the correct answer.

- ❌ :  "Amazon EFS for cold data storage" is incorrect as FSx works natively with S3 which is also more economical.

- ❌ :  "Amazon S3 for high-performance parallel storage" is incorrect as S3 is not suitable for running

  high-performance computing jobs.

- ❌ :  "Amazon FSx for Windows for high-performance parallel storage" is incorrect as FSx for Lustre should be used

  for HPC use cases and use cases that require storing data on S3.

**References:**

<https://aws.amazon.com/fsx/lustre/>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-fsx/>

----

- #performance_parallel_storage #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-fsx/> #s3_data #performance_file_system #cold_data_storage
