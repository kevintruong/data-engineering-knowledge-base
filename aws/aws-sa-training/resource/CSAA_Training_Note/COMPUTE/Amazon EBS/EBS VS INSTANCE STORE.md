#### EBS VS INSTANCE STORE

EBS-backed means the root volume is an EBS volume and storage is persistent.

Instance store-backed means the root volume is an instance store volume and
storage is not persistent.

On an EBS-backed instance, the default action is for the root EBS volume to be
deleted upon

termination.

Instance store volumes are sometimes called Ephemeral storage (non-persistent).

Instance store backed instances cannot be stopped. If the underlying host fails,
the data will be lost.

Instance store volume root devices are created from AMI templates stored on S3.

EBS backed instances can be stopped. You will not lose the data on this instance
if it is stopped

(persistent).

EBS volumes can be detached and reattached to other EC2 instances.

EBS volume root devices are launched from AMI’s that are backed by EBS
snapshots.

Instance store volumes cannot be detached/reattached.

When rebooting the instances for both types data will not be lost.

By default, both root volumes will be deleted on termination unless you
configured otherwise.

