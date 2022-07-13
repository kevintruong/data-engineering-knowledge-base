#### PERFORMANCE

**There are two performance modes:**

- “General Purpose” performance mode is appropriate for most file systems.

- “Max I/O” performance mode is optimized for applications where tens, hundreds,
  or thousands of EC2 instances are

  accessing the file system.

Amazon EFS is designed to burst to allow high throughput levels for periods of
time.

Amazon EFS file systems are distributed across an unconstrained number of
storage servers, enabling file systems to grow

elastically to petabyte scale and allowing massively parallel access from Amazon
EC2 instances to your data.

This distributed data storage design means that multithreaded applications and
applications that concurrently access

data from multiple Amazon EC2 instances can drive substantial levels of
aggregate throughput and IOPS.

The table below compares high-level performance and storage characteristics for
AWS’s file (EFS)

and block (EBS) cloud storage offerings:

