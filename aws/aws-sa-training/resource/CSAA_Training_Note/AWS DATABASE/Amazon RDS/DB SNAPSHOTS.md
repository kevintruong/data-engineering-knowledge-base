#### DB SNAPSHOTS

DB Snapshots are user-initiated and enable you to back up your DB instance in a
known state as frequently as you wish,

and then restore to that specific state.

Cannot be used for point-in-time recovery.

Snapshots are stored on S3.

Snapshots remain on S3 until manually deleted.

Backups are taken within a defined window.

I/O is briefly suspended while backups initialize and may increase latency (
applicable to single-AZ RDS).

DB snapshots that are performed manually will be stored even after the RDS
instance is deleted.

Restored DBs will always be a new RDS instance with a new DNS endpoint.

Can restore up to the last 5 minutes.

You cannot restore from a DB snapshot to an existing DB – a new instance is
created when you restore.

Only default DB parameters and security groups are restored – you must manually
associate all other DB parameters and

SGs.

It is recommended to take a final snapshot before deleting an RDS instance.

Snapshots can be shared with other AWS accounts.

