#### Question  25

**A Solutions Architect is attempting to clean up unused EBS volumes and snapshots to save some space and cost. How many

of the most recent snapshots of an EBS volume need to be maintained to guarantee that you can recreate the full EBS

volume from the snapshot?**

- [ ] :  You must retain all snapshots as the process is incremental and therefore data is required from each snapshot

- [ ] :  Two snapshots, the oldest and most recent snapshots

- [ ] :  The oldest snapshot, as this references data in all other snapshots

- [x] :  Only the most recent snapshot. Snapshots are incremental, but the deletion process will ensure that no data is lost

*----

- #unused_ebs_volumes #ebs_volume #snapshots #recent_snapshots #other_snapshots
- hasExplain:: [[explanation_Question  25.md]]
