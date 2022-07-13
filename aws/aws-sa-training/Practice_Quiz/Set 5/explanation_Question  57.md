*

**Explanation:**

When an EBS volume is encrypted with a custom key you must share the custom key with the PROD account. You also need to

modify the permissions on the snapshot to share it with the PROD account. The PROD account must copy the snapshot before

they can then create volumes from the snapshot

Note that you cannot share encrypted volumes created using a default CMK key and you cannot change the CMK key that is

used to encrypt a volume.

* ✅ :  "Share the custom key used to encrypt the volume" is a correct answer.

* ✅ :  "Modify the permissions on the encrypted snapshot to share it with the Prod account" is also a correct answer.

* ❌ :  "Make a copy of the EBS volume and unencrypt the data in the process" is incorrect. You do not need to

  decrypt the data as there is a workable solution that keeps the data secure at all times.

* ❌ :  "Create a snapshot of the unencrypted volume and share it with the Prod account" is incorrect as the volume

  is already encrypted as security should be maintained.

* ❌ :  "Use CloudHSM to distribute the encryption keys use to encrypt the volume" is incorrect. CloudHSM is used

  for key management and storage but not distribution..

**References:**

<https://aws.amazon.com/blogs/aws/new-cross-account-copying-of-encrypted-ebs-snapshots/>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ebs/>

----
* #encrypted_volumes #ebs_volume #unencrypted_volume #encryption_keys #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ebs/>
