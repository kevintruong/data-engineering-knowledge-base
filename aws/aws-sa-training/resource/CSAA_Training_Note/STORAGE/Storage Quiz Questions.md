### Storage Quiz Questions


Answers and explanations are provided below after the last question in this section.


**Question 1: You would like to run some code when an object is uploaded to an Amazon S3 bucket. How can this be

achieved?**


1. Create an event notification on the S3 bucket that triggers a Lambda function

2. Configure Lambda to poll the S3 bucket for changes and run a function when it finds new objects

3. Create an event notification on the S3 bucket that notifies Amazon SNS to trigger a Lambda function


**Question 2: Which type Amazon storage service uses standards-based REST web interfaces to manage objects?**


1. Amazon Elastic File System (EFS)

2. Amazon Elastic Block Store (EBS)

3. Amazon Simple Storage Service (S3)

4. Amazon FSx for Windows File Server


**Question 3: What is the maximum file size allowed in Amazon S3?**


1. 5 terabytes

2. 0 bytes

3. 5 gigabytes

4. Unlimited


**Question 4: What type of consistency model is provided in Amazon S3 when you upload a new version of an object?**


1. Read after write consistency

2. Eventual consistency


**Question 5: Which Amazon S3 capability uses Amazon CloudFront and enables fast uploads for objects?**


1. Multipart upload

2. Cross region replication (CRR)

3. BitTorrent

4. Transfer acceleration


**Question 6: How can you create a hierarchy that mimics a filesystem in Amazon S3?**


1. Create buckets within other buckets

2. Use folders in your buckets

3. Upload objects within other objects

4. Use lifecycle rules to tier your data


**Question 7: A US based organization is concerned about uploading data to Amazon S3 as data sovereignty rules mean they

cannot move their data outside of the US. What would you tell them?**


1. Data never leaves a region unless specifically configured to do so.

2. Data will be replicated globally so they cannot use Amazon S3.


**Question 8: For compliance reasons, an organization needs to retain data for 7 years. If they need to retrieve data,

they have 24 hours to do so. Which Amazon S3 storage class is most cost- effective?**


1. Amazon S3 One-Zone IA

2. Amazon S3 Intelligent Tiering

3. Amazon S3 Glacier

4. Amazon S3 Glacier Deep Archive


**Question 9: An Architect is designing an application that will use hundreds of EC2 instances across multiple

availability zones. A shared filesystem is required that can be mounted by all instances. Which storage service is

suitable for this requirement?**


1. Amazon Elastic File System (EFS)

2. Amazon Elastic Block Store (EBS)

3. Amazon Instance Store

4. Amazon Simple Storage Service (S3)


**Question 10: How can you control access to files and directories in Amazon EFS filesystems?**


1. Using IAM

2. Using EFS security groups

3. Using Network ACLs

4. Using user and group-level permissions


**Question 11: A High-Performance Computing (HPC) application requires a high-performance filesystem for running data

analysis. The filesystem should transparently access source data stored as Amazon S3 objects. Which type of filesystem

is ideal for this use case?**


1. Amazon FSx for Windows File Server

2. Amazon Elastic File System (EFS)

3. Amazon FSx for Lustre

4. Amazon Elastic Block Store (EBS)


**Question 12: Which AWS storage service provides a NTFS filesystem that can be accessed by multiple EC2 instances using

the SMB protocol?**


1. Amazon FSx for Windows File Server

2. Amazon Elastic File System (EFS)

3. Amazon FSx for Lustre

4. Amazon Elastic Block Store (EBS)


**STORAGE - ANSWERS**


**Question 1, Answer: 1**


**Explanation:**


```

1 is correct. The best way to achieve this is to use an event notification on the S3 bucket that

triggers a function that then runs the code.

2 is incorrect. Lambda does not poll S3.

3 is incorrect. You would not use Amazon SNS in this scenario as it is an unnecessary additional

step.

```


**Question 2, Answer: 3**


**Explanation:**


```

1 is incorrect. EFS is a file-based storage system that is accessed using the NFS protocol.

2 is incorrect. EBS is a block-based storage system for mounting volumes.

3 is correct. Amazon S3 is an object-based storage system that uses standards-based REST web

interfaces to work with objects.

4 is incorrect. Amazon FSx for Windows File Server provides a fully managed Microsoft filesystem

that is mounted using SMB.

```


**Question 3, Answer: 1**


**Explanation:**


```

1 is correct. The maximum file size for Amazon S3 objects is 5 terabytes.

2 is incorrect. This is the minimum file size possible in Amazon S3.

3 is incorrect. 5GB is not the maximum file size possible in Amazon S3.

4 is incorrect. There is a limit on the maximum file size for objects in Amazon S3.

```


**Question 4, Answer: 2**


**Explanation:**


```

1 is incorrect. You do not get read after write consistency for overwrite PUT and DELETES.

2 is correct. In Amazon S3 you get eventual consistency for overwrite PUTS and DELETES.

```


**Question 5, Answer: 4**


**Explanation:**


```

1 is incorrect. Multipart upload is recommended for uploading objects larger than 100MB but it

does not use CloudFront.

2 is incorrect. CRR is used for replicating objects between buckets in different regions.

3 is incorrect. BitTorrent can be used for retrieving objects from Amazon S3. It is not used for

uploading and doesn’t use CloudFront.

4 is correct. Transfer Acceleration speeds up data uploads by using the CloudFront network.

```


**Question 6, Answer: 2**


**Explanation:**


```

1 is incorrect. You cannot nest buckets (create buckets inside other buckets).

2 is correct. You can mimic the hierarchy of a filesystem by creating folder in your buckets.

```


```

3 is incorrect. You cannot upload objects within other objects.

4 is incorrect. Tiering your data is done for performance not to mimic a filesystem.

```


**Question 7, Answer: 1**


**Explanation:**


```

1 is correct. S3 is a global service but buckets are created within a region. Data is never replicated

outside of that region unless you configure it (e.g. through CRR).

2 is incorrect. Data is not replicated globally with Amazon S3.

```


**Question 8, Answer: 4**


**Explanation:**


```

1 is incorrect. This is not the most cost-effective option for these requirements.

2 is incorrect. This is not the most cost-effective option for these requirements.

3 is incorrect. This is not the most cost-effective option for these requirements. It is slightly more

expensive than Deep Archive but faster to retrieve data (which isn’t necessary for this

scenario).

4 is correct. This is the most cost-effective option for these requirements as the data retrieval

time is 24 hours.

```


**Question 9, Answer: 1**


**Explanation:**


```

1 is correct. EFS is a file-based storage system accessed over NFS. You can attach thousands of

instances from multiple AZs to the same filesystem.

2 is incorrect. You cannot attach multiple instances to a single EBS volume or attach volumes

across AZs.

3 is incorrect. Instance Stores are local storage on the EC2 host servers, you cannot attach

multiple instances to the same instance store.

4 is incorrect. Amazon S3 is an object-based storage system, not a filesystem.

```


**Question 10, Answer: 4**


**Explanation:**


```

1 is incorrect. IAM can be used to control who can administer the file system but not control the

access to files and directories.

2 is incorrect. EFS security groups control network traffic that is allowed to reach the filesystem.

3 is incorrect. Network ACLs are not used for file and directory permissions, they restrict traffic

into and out of subnets.

4 is correct. You can control access to files and directories with POSIX-compliant user and group-

level permissions.

```


**Question 11, Answer: 3**


**Explanation:**


```

1 is incorrect. FSx for Windows File Server cannot access data stored on Amazon S3.

2 is incorrect. EFS does not integrate with Amazon S3 to transparently access objects.

3 is correct. This is a good use case for Amazon FSx for Lustre.

```


```

4 is incorrect. EBS is not a filesystem nor does it directly integrate with Amazon S3 for

transparent access of S3 objects.

```


**Question 12, Answer: 1**


**Explanation:**


```

1 is correct. FSx for Windows File Server provides NTFS file systems that can be accessed from up

to thousands of compute instances using the SMB protocol.

2 is incorrect. EFS is not an NTFS filesystem.

3 is incorrect. FSx for Lustre does not provide an NTFS filesystem.

4 is incorrect. EBS does not provide an NTFS filesystem nor can it be accessed by multiple EC2

instances.

```

