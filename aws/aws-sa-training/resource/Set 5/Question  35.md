#### Question  35


**Encrypted Amazon Elastic Block Store (EBS) volumes are attached to some Amazon EC2 instances. Which statements are

correct about using encryption with Amazon EBS volumes? (Select TWO)**


1: Data is only encrypted at rest


2: Encryption is supported on all Amazon EBS volume types


3: Data in transit between an instance and an encrypted volume is also encrypted


4: Volumes created from encrypted snapshots are unencrypted


5: You cannot mix encrypted with unencrypted volumes on an instance


**Answer: 2, 3**


**Explanation:**


Some facts about Amazon EBS encrypted volumes and snapshots:


- All **EBS** types support encryption and all instance **families** now support encryption.

- Not all **instance** types support encryption.

- Data in transit between an instance and an encrypted volume is also encrypted (data is encrypted in trans.

- You can have encrypted an unencrypted EBS volumes attached to an instance at the same time.

- Snapshots of encrypted volumes are encrypted automatically.

- EBS volumes restored from encrypted snapshots are encrypted automatically.

- EBS volumes created from encrypted snapshots are also encrypted.


- CORRECT "Encryption is supported on all Amazon EBS volume types" is a correct answer.


- CORRECT "Data in transit between an instance and an encrypted volume is also encrypted" is also a correct answer.


- INCORRECT "Data is only encrypted at rest" is incorrect. Please refer to the facts above.


- INCORRECT "Volumes created from encrypted snapshots are unencrypted" is incorrect. Please refer to the facts above.


- INCORRECT "You cannot mix encrypted with unencrypted volumes on an instance" is incorrect. Please refer to the facts

  above.


**References:**


https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ebs/

