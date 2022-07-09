#### Question  48


**An application currently stores all data on Amazon EBS volumes. All EBS volumes must be backed up durably across

multiple Availability Zones.**


**What is the MOST resilient way to back up volumes?**


1: Take regular EBS snapshots


2: Enable EBS volume encryption


3: Mirror data across two EBS volumes


4: Create a script to copy data to an EC2 instance store


Answer: 1


**Explanation:**


You can back up the data on your Amazon EBS volumes to Amazon S3 by taking point-in-time snapshots. Snapshots are _

incremental_ backups, which means that only the blocks on the device that have changed after your most recent snapshot

are saved. This minimizes the time required to create the snapshot and saves on storage costs by not duplicating data.

When you delete a snapshot, only the data unique to that snapshot is removed. Each snapshot contains all of the

information that is needed to restore your data (from the moment when the snapshot was taken) to a new EBS volume.


- CORRECT "Take regular EBS snapshots" is the correct answer.


- INCORRECT "Enable EBS volume encryption" is incorrect. Enabling volume encryption would not increase resiliency.


- INCORRECT "Mirror data across two EBS volumes" is incorrect. Mirroring data would provide resilience however both

  volumes would need to be mounted to the EC2 instance within the same AZ so you are not getting the redundancy

  required.


- INCORRECT "Create a script to copy data to an EC2 instance store" is incorrect. Instance stores are ephemeral

  (non-persistent) data stores so would not add any resilience.


**References:**


https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSSnapshots.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ebs/

