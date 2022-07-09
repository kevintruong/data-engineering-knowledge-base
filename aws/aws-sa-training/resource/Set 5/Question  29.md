#### Question  29


**A Solutions Architect needs to migrate an Oracle database running on RDS onto Amazon RedShift to improve performance

and reduce cost. What combination of tasks using AWS services should be followed to execute the migration? (Select

TWO)**


1: Migrate the database using the AWS Database Migration Service (DMS)


2: Convert the schema using the AWS Schema Conversion Tool


3: Take a snapshot of the Oracle database and restore the snapshot onto RedShift


4: Configure API Gateway to extract, transform and load the data into RedShift


5: Enable log shipping from the Oracle database to RedShift


**Answer: 1,2**


**Explanation:**


Convert the data warehouse schema and code from the Oracle database running on RDS using the AWS Schema Conversion

Tool (AWS SCT) then migrate data from the Oracle database to Amazon Redshift using the AWS Database Migration Service (

AWS DMS)


- CORRECT "Migrate the database using the AWS Database Migration Service (DMS)" is the correct answer.


- CORRECT "Convert the schema using the AWS Schema Conversion Tool" is the correct answer.


- INCORRECT "Take a snapshot of the Oracle database and restore the snapshot onto RedShift" is incorrect. Snapshots are

  not a supported migration method from RDS to RedShift.


- INCORRECT "Configure API Gateway to extract, transform and load the data into RedShift" is incorrect. API Gateway is

  not used for ETL functions.


- INCORRECT "Enable log shipping from the Oracle database to RedShift" is incorrect. Log shipping is not a supported

  migration method from RDS to RedShift.


**References:**


https://aws.amazon.com/getting-started/projects/migrate-oracle-to-amazon-redshift/

