#### Question  54


**A large quantity of data that is rarely accessed is being archived onto Amazon Glacier. Your CIO wants to understand

the resilience of the service. Which of the statements below is correct about Amazon Glacier storage? (Select TWO)**


1: Data is replicated globally


2: Provides 99.999999999% durability of archives


3: Data is resilient in the event of one entire Availability Zone destruction


4: Data is resilient in the event of one entire region destruction


5: Provides 99.9% availability of archives


**Answer: 2,3**


**Explanation:**


Glacier is designed for durability of 99.999999999% of objects across multiple Availability Zones. Data is resilient in

the event of one entire Availability Zone destruction. Glacier supports SSL for data in transit and encryption of data

at rest. Glacier is extremely low cost and is ideal for long-term archival.


- CORRECT "Provides 99.999999999% durability of archives" is the correct answer.


- CORRECT "Data is resilient in the event of one entire Availability Zone destruction" is the correct answer.


- INCORRECT "Data is replicated globally" is incorrect. Data is not replicated globally.


- INCORRECT "Data is resilient in the event of one entire region destruction" is incorrect. Data is not resilient to the

  failure of an entire region.


- INCORRECT "Provides 99.9% availability of archives" is incorrect. Glacier is “designed for” availability of **

  99.99%**


**References:**


https://aws.amazon.com/s3/storage-classes/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/

