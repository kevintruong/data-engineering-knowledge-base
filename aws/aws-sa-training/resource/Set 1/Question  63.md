#### Question  63


**An application you are designing receives and processes files. The files are typically around 4GB in size and the

application extracts metadata from the files which typically takes a few seconds for each file. The pattern of updates

is highly dynamic with times of little activity and then multiple uploads within a short period of time.**


**What architecture will address this workload the most cost efficiently?**


- [ ] Use a Kinesis data stream to store the file, and use Lambda for processing


- [ ] Store the file in an EBS volume which can then be accessed by another EC2 instance for processing


- [x] Upload files into an S3 bucket, and use the Amazon S3 event notification to invoke a Lambda function to extract the

metadata


- [ ] Place the files in an SQS queue, and use a fleet of EC2 instances to extract the metadata



- hasExplain:: [[explanation_Question  63.md]]

#s3 #uploads #ec2 #workload #files 