#### Question  48

**A Solutions Architect needs to transform data that is being uploaded into S3. The uploads happen sporadically and the

transformation should be triggered by an event. The transformed data should then be loaded into a target data store.**

**What services would be used to deliver this solution in the MOST cost-effective manner? (Select TWO)**

- [ ] Configure a CloudWatch alarm to send a notification to CloudFormation when data is uploaded

- [x] Configure S3 event notifications to trigger a Lambda function when data is uploaded and use the Lambda function to

trigger the ETL job

- [ ] Configure CloudFormation to provision a Kinesis data stream to transform the data and load it into S3

- [x] Use AWS Glue to extract, transform and load the data into the target data store

- [ ] Configure CloudFormation to provision AWS Data Pipeline to transform the data

- hasExplain:: [[explanation_Question  48.md]]

# aws_data_pipeline #cloudformation #s3 #kinesis_data_stream #configure_cloudformation
