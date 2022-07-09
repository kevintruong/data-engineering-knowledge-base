#### Question  57


**A company has multiple AWS accounts for several environments (Prod, Dev, Test etc.). A Solutions Architect would like

to copy an Amazon EBS snapshot from DEV to PROD. The snapshot is from an EBS volume that was encrypted with a custom

key.**


**What steps must be performed to share the encrypted EBS snapshot with the Prod account? (Select TWO)**


- [x] Share the custom key used to encrypt the volume


- [ ] Make a copy of the EBS volume and unencrypt the data in the process


- [ ] Create a snapshot of the unencrypted volume and share it with the Prod account


- [x] Modify the permissions on the encrypted snapshot to share it with the Prod account


- [ ] Use CloudHSM to distribute the encryption keys use to encrypt the volume


*