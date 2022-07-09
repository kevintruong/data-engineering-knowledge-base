#### Question  25


**A Solutions Architect is attempting to clean up unused EBS volumes and snapshots to save some space and cost. How many

of the most recent snapshots of an EBS volume need to be maintained to guarantee that you can recreate the full EBS

volume from the snapshot?**


1: You must retain all snapshots as the process is incremental and therefore data is required from each snapshot


2: Two snapshots, the oldest and most recent snapshots


3: The oldest snapshot, as this references data in all other snapshots


4: Only the most recent snapshot. Snapshots are incremental, but the deletion process will ensure that no data is lost


**Answer: 4**


**Explanation:**


Snapshots capture a point-in-time state of an instance. If you make periodic snapshots of a volume, the snapshots are

incremental, which means that only the blocks on the device that have changed after your last snapshot are saved in the

new snapshot.


Even though snapshots are saved incrementally, the snapshot deletion process is designed so that you need to retain only

the most recent snapshot in order to restore the volume.


- CORRECT "Only the most recent snapshot. Snapshots are incremental, but the deletion process will ensure that no data

  is lost" is the correct answer.


- INCORRECT "You must retain all snapshots as the process is incremental and therefore data is required from each

  snapshot" is incorrect as explained above.


- INCORRECT "Two snapshots, the oldest and most recent snapshots" is incorrect as explained above.


- INCORRECT "The oldest snapshot, as this references data in all other snapshots" is incorrect as explained above.


**References:**


https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-deleting-snapshot.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ebs/

