*

**Explanation:**

All EBS types and all instance _families_ support encryption but not all instance _types_ support encryption. There is

no direct way to change the encryption state of a volume. Data in transit between an instance and an encrypted volume is

also encrypted.

* ✅ :  "Data in transit between an instance and an encrypted volume is also encrypted" is the correct answer.

* ✅ :  "There is no direct way to change the encryption state of a volume" is the correct answer.

* ❌ :  "Not all EBS types support encryption" is incorrect as all EBS volume types support encryption.

* ❌ :  "All attached EBS volumes must share the same encryption state" is incorrect. You can have encrypted and

  non-encrypted EBS volumes on a single instance.

* ❌ :  "All instance types support encryption" is incorrect. All instance families support encryption, but not all

  instance types.

**References:**

<https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ebs/>

----
* #instance___families___support_encryption #ebs_volume_types #ebs_volumes #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ebs/> #encrypted_volume
