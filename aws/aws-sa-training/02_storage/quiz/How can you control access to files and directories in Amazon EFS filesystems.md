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


---- 
#quiz 