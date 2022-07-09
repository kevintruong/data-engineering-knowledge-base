#### Question  57


**You have created a file system using Amazon Elastic File System (EFS) which will hold home directories for users. What

else needs to be done to enable users to save files to the EFS file system?**


```

Internet Client

```


```

HTTP, HTTPS

```


```

Application Load Balancer

```


```

Target Group 1 Target Group 2

```


```

Listener

```


```

Rule (default) Rule (/orders)

```


```

Instance 1 Instance 2 Instance 3 Instance 4

```


1: Create a separate EFS file system for each user and grant read-write-execute permissions on the root directory to the

respective user. Then mount the file system to the users’ home directory


2: Modify permissions on the root directory to grant read-write-execute permissions to the users. Then create a

subdirectory and mount it to the users’ home directory


3: Instruct the users to create a subdirectory on the file system and mount the subdirectory to their home directory


4: Create a subdirectory for each user and grant read-write-execute permissions to the users. Then mount the

subdirectory to the users’ home directory


Answer: 4


**Explanation:**


After creating a file system, by default, only the root user (UID 0) has read-write-execute permissions. For other users

to modify the file system, the root user must explicitly grant them access.


One common use case is to create a “writable” subdirectory under this file system root for each user you create on the

EC2 instance and mount it on the user’s home directory. All files and subdirectories the user creates in their home

directory are then created on the Amazon EFS file system


- CORRECT "Create a subdirectory for each user and grant read-write-execute permissions to the users. Then mount the

  subdirectory to the users’ home directory" is the correct answer.


- INCORRECT "Create a separate EFS file system for each user and grant read-write-execute permissions on the root

  directory to the respective user. Then mount the file system to the users’ home directory" is incorrect. You don’t

  want to create a separate EFS file system for each user, this would be a higher cost and require more management

  overhead.


- INCORRECT "Modify permissions on the root directory to grant read-write-execute permissions to the users. Then create

  a subdirectory and mount it to the users’ home directory" is incorrect. You don’t want to modify permission on the

  root directory as this will mean all users are able to access other users’ files (and this is a home directory, so the

  contents are typically kept private).


- INCORRECT "Instruct the users to create a subdirectory on the file system and mount the subdirectory to their home

  directory" is incorrect. Instructing the users to create a subdirectory on the file system themselves would not work

  as they will not have access to write to the directory root.


**References:**


https://docs.aws.amazon.com/efs/latest/ug/accessing-fs-nfs-permissions-per-user-subdirs.html


https://docs.aws.amazon.com/efs/latest/ug/accessing-fs-nfs-permissions.html#accessing-fs-nfs-permissions-

ex-scenarios


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-efs/

