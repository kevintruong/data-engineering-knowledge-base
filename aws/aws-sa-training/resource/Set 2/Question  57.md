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

- [ ] Create a separate EFS file system for each user and grant read-write-execute permissions on the root directory to the

respective user. Then mount the file system to the users’ home directory

- [ ] Modify permissions on the root directory to grant read-write-execute permissions to the users. Then create a

subdirectory and mount it to the users’ home directory

- [ ] Instruct the users to create a subdirectory on the file system and mount the subdirectory to their home directory

- [x] Create a subdirectory for each user and grant read-write-execute permissions to the users. Then mount the

subdirectory to the users’ home directory

- hasExplain:: [[explanation_Question  57.md]]

# amazon_elastic_file_system #efs_file_system #separate_efs_file_system #efs #permissions
