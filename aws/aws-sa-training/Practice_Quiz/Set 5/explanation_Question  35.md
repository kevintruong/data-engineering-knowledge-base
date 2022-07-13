*

**Explanation:**

Some facts about Amazon EBS encrypted volumes and snapshots:

* All **EBS** types support encryption and all instance **families** now support encryption.

* Not all **instance** types support encryption.

* Data in transit between an instance and an encrypted volume is also encrypted (data is encrypted in trans.

* You can have encrypted an unencrypted EBS volumes attached to an instance at the same time.

* Snapshots of encrypted volumes are encrypted automatically.

* EBS volumes restored from encrypted snapshots are encrypted automatically.

* EBS volumes created from encrypted snapshots are also encrypted.

* ✅ :  "Encryption is supported on all Amazon EBS volume types" is a correct answer.

* ✅ :  "Data in transit between an instance and an encrypted volume is also encrypted" is also a correct answer.

* ❌ :  "Data is only encrypted at rest" is incorrect. Please refer to the facts above.

* ❌ :  "Volumes created from encrypted snapshots are unencrypted" is incorrect. Please refer to the facts above.

* ❌ :  "You cannot mix encrypted with unencrypted volumes on an instance" is incorrect. Please refer to the facts

  above.

**References:**

<https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ebs/>

----
* #unencrypted_ebs_volumes #amazon_ebs_volume_types #ebs_volumes #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ebs/> #encryption
