### AWS Storage Gateway


**GENERAL**


The AWS Storage Gateway service enables hybrid storage between on-premises environments and the AWS Cloud.


It provides low-latency performance by caching frequently accessed data on premises, while storing data securely and

durably in Amazon cloud storage services.


Implemented using a virtual machine that you run on-premises (VMware or Hyper-V virtual appliance).


Provides local storage resources backed by AWS S3 and Glacier.


Often used in disaster recovery preparedness to sync data to AWS.


Useful in cloud migrations.


AWS Storage Gateway supports three storage interfaces: file, volume, and tape.


The table below shows the different gateways available and the interfaces and use cases:


Each gateway you have can provide one type of interface.


All data transferred between any type of gateway appliance and AWS storage is encrypted using SSL.


By default, all data stored by AWS Storage Gateway in S3 is encrypted server-side with Amazon S3- Managed Encryption

Keys (SSE-S3).


When using the file gateway, you can optionally configure each file share to have your objects encrypted with AWS

KMS-Managed Keys using SSE-KMS.


**FILE GATEWAY**


File gateway provides a virtual on-premises file server, which enables you to store and retrieve files as objects in

Amazon S3.


Can be used for on-premises applications, and for Amazon EC2-resident applications that need file storage in S3 for

object-based workloads.


Used for flat files only, stored directly on S3.


File gateway offers SMB or NFS-based access to data in Amazon S3 with local caching.


File gateway supports Amazon S3 Standard, S3 Standard – Infrequent Access (S3 Standard – IA) and S3 One Zone – IA.


File gateway supports clients connecting to the gateway using NFS v3 and v4.1.


Microsoft Windows clients that support NFS v3 can connect to file gateway.


The maximum size of an individual file is 5 TB.


**VOLUME GATEWAY**


The volume gateway represents the family of gateways that support block-based volumes, previously referred to as

gateway-cached and gateway-stored modes.


Block storage – iSCSI based.


Cached Volume mode – the entire dataset is stored on S3 and a cache of the most frequently accessed data is cached

on-site.


Stored Volume mode – the entire dataset is stored on-site and is asynchronously backed up to S3

(EBS point-in-time snapshots). Snapshots are incremental and compressed.


Each volume gateway can support up to 32 volumes.


In cached mode, each volume can be up to 32 TB for a maximum of 1 PB of data per gateway (32 volumes, each 32 TB in

size).


In stored mode, each volume can be up to 16 TB for a maximum of 512 TB of data per gateway (32 volumes, each 16 TB in

size).


**GATEWAY VIRTUAL TAPE LIBRARY**


Used for backup with popular backup software.


Each gateway is preconfigured with a media changer and tape drives. Supported by NetBackup, Backup Exec, Veeam etc.


When creating virtual tapes, you select one of the following sizes: 100 GB, 200 GB, 400 GB, 800 GB, 1.5 TB, and 2.5 TB.


A tape gateway can have up to 1,500 virtual tapes with a maximum aggregate capacity of 1 PB.

