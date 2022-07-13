#### ENCRYPTION


You can encrypt your Amazon RDS instances and snapshots at rest by enabling the encryption option for your Amazon RDS DB

instance.


Encryption at rest is supported for all DB types and uses AWS KMS.


**When using encryption at rest the following elements are also encrypted:**


- All DB snapshots

- Backups

- DB instance storage

- Read Replicas


You cannot encrypt an existing DB, you need to create a snapshot, copy it, encrypt the copy, then build an encrypted DB

from the snapshot.


Data that is encrypted at rest includes the underlying storage for a DB instance, its automated backups, Read Replicas,

and snapshots.


A Read Replica of an Amazon RDS encrypted instance is also encrypted using the same key as the master instance when both

are in the same region.


If the master and Read Replica are in different regions, you encrypt using the encryption key for that region.


You can’t have an encrypted Read Replica of an unencrypted DB instance or an unencrypted Read Replica of an encrypted DB

instance.


Encryption/decryption is handled transparently.


RDS supports SSL encryption between applications and RDS DB instances.


RDS generates a certificate for the instance.

