#### Question  64


**A security officer has requested that all data associated with a specific customer is encrypted. The data resides on

Elastic Block Store (EBS) volumes. Which of the following statements about using EBS encryption are correct? (Select

TWO)**


1: Not all EBS types support encryption


2: All attached EBS volumes must share the same encryption state


3: All instance types support encryption


4: Data in transit between an instance and an encrypted volume is also encrypted


5: There is no direct way to change the encryption state of a volume


**Answer: 4,5**


**Explanation:**


All EBS types and all instance _families_ support encryption but not all instance _types_ support encryption. There is

no direct way to change the encryption state of a volume. Data in transit between an instance and an encrypted volume is

also encrypted.


- CORRECT "Data in transit between an instance and an encrypted volume is also encrypted" is the correct answer.


- CORRECT "There is no direct way to change the encryption state of a volume" is the correct answer.


- INCORRECT "Not all EBS types support encryption" is incorrect as all EBS volume types support encryption.


- INCORRECT "All attached EBS volumes must share the same encryption state" is incorrect. You can have encrypted and

  non-encrypted EBS volumes on a single instance.


- INCORRECT "All instance types support encryption" is incorrect. All instance families support encryption, but not all

  instance types.


**References:**


https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ebs/

