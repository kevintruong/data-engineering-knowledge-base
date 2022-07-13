*

**Explanation:**

Snapshots capture a point-in-time state of an instance. If you make periodic snapshots of a volume, the snapshots are

incremental, which means that only the blocks on the device that have changed after your last snapshot are saved in the

new snapshot.

Even though snapshots are saved incrementally, the snapshot deletion process is designed so that you need to retain only

the most recent snapshot in order to restore the volume.

* ✅ :  "Only the most recent snapshot. Snapshots are incremental, but the deletion process will ensure that no data

  is lost" is the correct answer.

* ❌ :  "You must retain all snapshots as the process is incremental and therefore data is required from each

  snapshot" is incorrect as explained above.

* ❌ :  "Two snapshots, the oldest and most recent snapshots" is incorrect as explained above.

* ❌ :  "The oldest snapshot, as this references data in all other snapshots" is incorrect as explained above.

**References:**

<https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-deleting-snapshot.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ebs/>

----
* #<https://docs.aws.amazon.com/awsec2/latest/userguide/ebs-deleting-snapshot.html> #snapshot_deletion_process #periodic_snapshots #snapshots #last_snapshot
