#### CROSS REGION REPLICATION


CRR is an Amazon S3 feature that automatically replicates data across AWS Regions.


With CRR, every object uploaded to an S3 bucket is automatically replicated to a destination bucket in a different AWS

Region that you choose.


Provides automatic, asynchronous copying of objects between buckets in different regions.


CRR is configured at the S3 bucket level.


You enable a CRR configuration on your source bucket by specifying a destination bucket in a different Region for

replication.


You can use either the AWS Management Console, the REST API, the AWS CLI, or the AWS SDKs to enable CRR.


Versioning must be enabled for both the source and destination buckets.


With CRR you can only replication between regions, not within a region (see SRR below for single region replication).


Replication is 1:1 (one source bucket, to one destination bucket).


You can configure separate S3 Lifecycle rules on the source and destination buckets.


You can replicate KMS-encrypted objects by providing a destination KMS key in your replication configuration.


You can set up CRR across AWS accounts to store your replicated data in a different account in the target region.


Provides low latency access for data by copying objects to buckets that are closer to users.


**To activate CRR you need to configure the replication on the source bucket:**


- Define the bucket in the other region to replicate to.

- Specify to replicate all objects or a subset of objects with specific key name prefixes.


The replicas will be exact replicas and share the same key names and metadata.


You can specify a different storage class (by default the source storage class will be used).


AWS S3 will encrypt data in-transit with SSL.


AWS S3 must have permission to replicate objects.


Bucket owners must have permission to read the object and object ACL.


Can be used across accounts but the source bucket owner must have permission to replicate objects into the destination

bucket.


**Triggers for replication are:**


- Uploading objects to the source bucket.

- DELETE of objects in the source bucket.

- Changes to the object, its metadata, or ACL.


**What is replicated:**


- New objects created after enabling replication.

- Changes to objects.

- Objects created using SSE-S3 using the AWS managed key.

- Object ACL updates.


**What isn’t replicated:**


- Objects that existed before enabling replication (can use the copy API).

- Objects created with SSE-C and SSE-KMS.

- Objects to which the bucket owner does not have permissions.

- Updates to bucket-level subresources.

- Actions from lifecycle rules are not replicated.

- Objects in the source bucket that are replicated from another region are not replicated.


**Deletion behavior:**


- If a DELETE request is made without specifying an object version ID a delete marker will be added and replicated.

- If a DELETE request is made specifying an object version ID the object is deleted but the delete marker is not

  replicated.


**Charges:**


- Requests for upload

- Inter-region transfer



- S3 storage in both regions


**SAME REGION REPLICATION (SRR)**


As the name implies you can use SRR to replication objects to a destination bucket within the same region as the source

bucket.


This feature was released in September 2018.


Replication is automatic and asynchronous.


New objects uploaded to an Amazon S3 bucket are configured for replication at the bucket, prefix, or object tag levels.


Replicated objects can be owned by the same AWS account as the original copy or by different accounts, to protect from

accidental deletion.


Replication can be to any Amazon S3 storage class, including S3 Glacier and S3 Glacier Deep Archive to create backups

and long-term archives.


When an S3 object is replicated using SRR, the metadata, Access Control Lists (ACL), and object tags associated with the

object are also part of the replication.


Once SRR is configured on a source bucket, any changes to the object, metadata, ACLs, or object tags trigger a new

replication to the destination bucket.

