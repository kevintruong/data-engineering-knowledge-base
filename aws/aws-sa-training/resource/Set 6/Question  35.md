#### Question  35


**One of the departments in a company has been generating a large amount of data on Amazon S3 and costs are increasing.

Data older than 90 days is rarely accessed but must be retained for several years. If this data does need to be accessed

at least 24 hours notice is provided.**


**How can a Solutions Architect optimize the costs associated with storage of this data whilst ensuring it is accessible

if required?**


1: Implement archival software that automatically moves the data to tape


2: Use S3 lifecycle policies to move data to the STANDARD_IA storage class


3: Use S3 lifecycle policies to move data to GLACIER after 90 days


4: Select the older data and manually migrate it to GLACIER


**Answer: 3**


**Explanation:**


To manage your objects so that they are stored cost effectively throughout their lifecycle, configure their lifecycle. A

lifecycle configuration is a set of rules that define actions that Amazon S3 applies to a group of objects. Transition

actions define when objects transition to another storage class.


For example, you might choose to transition objects to the STANDARD_IA storage class 30 days after you created them, or

archive objects to the GLACIER storage class one year after creating them.


GLACIER retrieval times:


- Standard retrieval is 3- 5 hours which is well within the requirements here.

- You can use Expedited retrievals to access data in 1 – 5 minutes.

- You can use Bulk retrievals to access up to petabytes of data in approximately 5 – 12 hours.


- CORRECT "Use S3 lifecycle policies to move data to GLACIER after 90 days" is the correct answer.


- INCORRECT "Implement archival software that automatically moves the data to tape" is incorrect as this solution can be

  fully automated using lifecycle policies.


- INCORRECT "Use S3 lifecycle policies to move data to the STANDARD_IA storage class" is incorrect. STANDARD_IA is good

  for infrequently accessed data and provides faster access times than GLACIER but is more expensive so not the best

  option here.


- INCORRECT "Select the older data and manually migrate it to GLACIER" is incorrect as a lifecycle policy can automate

  the process.


**References:**


https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html


https://aws.amazon.com/about-aws/whats-new/2016/11/access-your-amazon-glacier-data-in-minutes-with-

new-retrieval-options/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/

