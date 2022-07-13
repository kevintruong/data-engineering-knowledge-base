#### EFS FILE SYNC


EFS File Sync provides a fast and simple way to securely sync existing file systems into Amazon EFS.


EFS File Sync copies files and directories into Amazon EFS at speeds up to 5x faster than standard Linux copy tools,

with simple setup and management in the AWS Console.


EFS File Sync securely and efficiently copies files over the internet or an AWS Direct Connect connection.


Copies file data and file system metadata such as ownership, timestamps, and access permissions.


**EFS File Sync provides the following benefits:**


- Efficient high-performance parallel data transfer that tolerates unreliable and high-latency networks.

- Encryption of data transferred from your IT environment to AWS.

- Data transfer rate up to five times faster than standard Linux copy tools.

- Full and incremental syncs for repetitive transfers.


The following diagram shows a high-level view of the EFS File Sync architecture:


**Note:** EFS File Sync currently doesn’t support syncing from an Amazon EFS source to an NFS destination.


When deploying Amazon EFS File Sync on EC2, the instance size must be at least xlarge for your EFS File Sync to

function.


Recommended to use one of the Memory optimized r4.xlarge instance types.


Can choose to run EFS File Sync either on-premises as a virtual machine (VM), or in AWS as an EC2 instance.


Supports VMware ESXi.

