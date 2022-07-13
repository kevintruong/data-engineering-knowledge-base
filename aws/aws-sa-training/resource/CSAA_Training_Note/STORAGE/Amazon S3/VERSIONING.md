#### VERSIONING


Versioning stores all versions of an object (including all writes and even if an object is deleted).


Versioning protects against accidental object/data deletion or overwrites.


Enables “roll-back” and “un-delete” capabilities.


Versioning can also be used for data retention and archive.


Old versions count as billable size until they are permanently deleted.


Enabling versioning does not replicate existing objects.


Can be used for backup.


Once enabled versioning cannot be disabled only suspended.


Can be integrated with lifecycle rules.


Multi-factor authentication (MFA) delete can be enabled.


MFA delete can also be applied to changing versioning settings.


**MFA delete applies to:**


- Changing the bucket’s versioning state.

- Permanently deleting an object.


Cross Region Replication requires versioning to be enabled on the source and destination buckets.


Reverting to previous versions isn’t replicated.


By default, a HTTP GET retrieves the most recent version.


Only the S3 bucket owner can permanently delete objects once versioning is enabled.


When you try to delete an object with versioning enabled a DELETE marker is placed on the object.


You can delete the DELETE marker and the object will be available again.


Deletion with versioning replicates the delete marker. But deleting the delete marker is not replicated.


**Bucket versioning states:**


- Enabled

- Versioned

- Un-versioned


Objects that existed before enabling versioning will have a version ID of NULL.


**Suspension:**


- If you suspend versioning the existing objects remain as they are however new versions will not be created.

- While versioning is suspended new objects will have a version ID of NULL and uploaded objects of the same name will

  overwrite the existing object.

