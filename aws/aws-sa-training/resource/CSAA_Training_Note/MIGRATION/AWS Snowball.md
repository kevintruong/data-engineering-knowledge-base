### AWS Snowball


**GENERAL**


Petabyte scale data transport solution for transferring data into or out of AWS.


Uses a secure storage device for physical transportation.


AWS Snowball Client is software that is installed on a local computer and is used to identify, compress, encrypt, and

transfer data.


Uses 256 - bit encryption (managed with the AWS KMS) and tamper-resistant enclosures with TPM.


Snowball must be ordered from and returned to the same region.


To speed up data transfer it is recommended to run simultaneous instances of the AWS Snowball Client in multiple

terminals and transfer small files as batches.


Snowball can import to S3 or export from S3.


**THE SNOWBALL FAMILY**


Several services are offered in the Snowball family.


The table below describes these at a high-level:


Snowball (80TB) (50TB model available only in the USA).


Snowball Edge (100TB) comes with onboard storage and compute capabilities.


Snowmobile – exabyte scale with up to 100PB per Snowmobile.


AWS Import/export is when you send your own disks into AWS – this is being deprecated in favour of Snowball.

