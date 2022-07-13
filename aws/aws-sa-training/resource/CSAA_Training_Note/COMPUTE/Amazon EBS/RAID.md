#### RAID


RAID can be used to increase IOPS.


RAID 0 = 0 striping – data is written across multiple disks and increases performance but no redundancy.


RAID 1 = 1 mirroring – creates 2 copies of the data but does not increase performance, only redundancy.


RAID 10 = 10 combination of RAID 1 and 2 resulting in increase performance and redundancy (at the cost of additional

disks).


You can configure multiple striped gp2 or standard volumes (typically RAID 0).


You can configure multiple striped PIOPS volumes (typically RAID 0).


RAID is configured through the guest OS.


EBS optimized EC2 instances are another way of increasing performance.


Ensure the EC2 instance can handle the bandwidth required for the increased performance.


Use EBS optimized instances or instances with a 10 Gbps network interface.


Not recommended to use RAID for root/boot volumes.


**EBS LIMITS (PER REGION)**

