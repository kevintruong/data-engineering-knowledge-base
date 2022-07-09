#### Question  22


**An organization is creating a new storage solution and needs to ensure that Amazon S3 objects that are deleted are

immediately restorable for up to 30 days. After 30 days the objects should be retained for a further 180 days and be

restorable within 24 hours.**


**The solution should be operationally simple and cost-effective. How can these requirements be achieved?

(Select TWO)**


1: Enable object versioning on the Amazon S3 bucket that will contain the objects


3: Create a lifecycle rule to transition non-current versions to GLACIER after 30 days, and then expire the objects

after 180 days


3: Enable multi-factor authentication (MFA) delete protection


4: Enable cross-region replication (CRR) for the Amazon S3 bucket that will contain the objects


5: Create a lifecycle rule to transition non-current versions to STANDARD_IA after 30 days, and then expire the objects

after 180 days


Answer: 1,2


**Explanation:**


Object Versioning is a means of keeping multiple variants of an object in the same Amazon S3 bucket. When you delete an

object in a versioning enabled bucket the object is not deleted, a delete marker is added and the object is considered

“non-current”. In this case we can then transition the non-current versions to GLACIER after 30 days (as we need

immediate recoverability for 30 days), and then expire the object after 180 days as they are no longer required to be

recoverable.


- CORRECT "Enable object versioning on the Amazon S3 bucket that will contain the objects" is the correct answer.


- CORRECT "Create a lifecycle rule to transition non-current versions to GLACIER after 30 days, and then expire the

  objects after 180 days" is the correct answer.


- INCORRECT "Enable multi-factor authentication (MFA) delete protection" is incorrect. Multi-factor authentication (

  MFA) delete is a way of adding an extra layer of security to prevent accidental deletion. That’s not what we’re

  looking to do here. We don’t want to add any additional operational elements, we just need the ability to restore if

  we accidentally delete something.


- INCORRECT "Enable cross-region replication (CRR) for the Amazon S3 bucket that will contain the objects" is incorrect.

  Cross-region replication (CRR) is used for replicating the entire bucket to another region. This provide disaster

  recovery and a full additional copy of data. This is not the most cost-effective solution as you have 2 full copies of

  your data. However, deletions are not replicated so it does provide protection from deleting objects.


- INCORRECT "Create a lifecycle rule to transition non-current versions to STANDARD_IA after 30 days, and then expire

  the objects after 180 days" is incorrect. Transitioning to STANDARD_IA is less cost-effective than transitioning to

  GLACIER. As we only need recoverability within 24 hours GLACIER is the best option.


**References:**


https://d0.awsstatic.com/whitepapers/protecting-s3-against-object-deletion.pdf


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/

