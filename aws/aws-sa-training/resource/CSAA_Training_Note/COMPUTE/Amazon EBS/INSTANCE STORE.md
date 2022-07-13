#### INSTANCE STORE


An instance store provides _temporary_ (non-persistent) block-level storage for your instance.


This is different to EBS which provides persistent storage but is also a block storage service that can be a root or

additional volume.


Instance store storage is located on disks that are physically attached to the host computer.


Instance store is ideal for temporary storage of information that changes frequently, such as buffers, caches, scratch

data, and other temporary content, or for data that is replicated across a fleet of instances, such as a load-balanced

pool of web servers.


You can specify instance store volumes for an instance only when you launch it.


You can't detach an instance store volume from one instance and attach it to a different instance.


The instance type determines the size of the instance store available and the type of hardware used for the instance

store volumes.


Instance store volumes are included as part of the instance's usage cost.


Some instance types use NVMe or SATA-based solid state drives (SSD) to deliver high random I/O performance.


This is a good option when you need storage with very low latency, but you don't need the data to persist when the

instance terminates, or you can take advantage of fault-tolerant architectures.

