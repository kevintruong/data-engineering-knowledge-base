#### GENERAL


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

