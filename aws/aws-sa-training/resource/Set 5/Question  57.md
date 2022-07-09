#### Question  57


**A company has multiple AWS accounts for several environments (Prod, Dev, Test etc.). A Solutions Architect would like

to copy an Amazon EBS snapshot from DEV to PROD. The snapshot is from an EBS volume that was encrypted with a custom

key.**


**What steps must be performed to share the encrypted EBS snapshot with the Prod account? (Select TWO)**


1: Share the custom key used to encrypt the volume


2: Make a copy of the EBS volume and unencrypt the data in the process


3: Create a snapshot of the unencrypted volume and share it with the Prod account


4: Modify the permissions on the encrypted snapshot to share it with the Prod account


5: Use CloudHSM to distribute the encryption keys use to encrypt the volume


**Answer: 1,4**


**Explanation:**


When an EBS volume is encrypted with a custom key you must share the custom key with the PROD account. You also need to

modify the permissions on the snapshot to share it with the PROD account. The PROD account must copy the snapshot before

they can then create volumes from the snapshot


Note that you cannot share encrypted volumes created using a default CMK key and you cannot change the CMK key that is

used to encrypt a volume.


- CORRECT "Share the custom key used to encrypt the volume" is a correct answer.


- CORRECT "Modify the permissions on the encrypted snapshot to share it with the Prod account" is also a correct answer.


- INCORRECT "Make a copy of the EBS volume and unencrypt the data in the process" is incorrect. You do not need to

  decrypt the data as there is a workable solution that keeps the data secure at all times.


- INCORRECT "Create a snapshot of the unencrypted volume and share it with the Prod account" is incorrect as the volume

  is already encrypted as security should be maintained.


- INCORRECT "Use CloudHSM to distribute the encryption keys use to encrypt the volume" is incorrect. CloudHSM is used

  for key management and storage but not distribution..


**References:**


https://aws.amazon.com/blogs/aws/new-cross-account-copying-of-encrypted-ebs-snapshots/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ebs/

