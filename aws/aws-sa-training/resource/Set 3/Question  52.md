#### Question  52


**There is expected to be a large increase in write intensive traffic to a website you manage that registers users onto

an online learning program. You are concerned about writes to the database being dropped and need to come up with a

solution to ensure this does not happen. Which of the solution options below would be the best approach to take?**


- [x] Update the application to write data to an SQS queue and provision additional EC2 instances to process the data and

write it to the database


- [ ] Use RDS in a multi-AZ configuration to distribute writes across AZs


- [ ] Use CloudFront to cache the writes and configure the database as a custom origin


- [ ] Update the application to write data to an S3 bucket and provision additional EC2 instances to process the data and

write it to the database



- hasExplain:: [[explanation_Question  52.md]]

#cloudfront #ec2 #azs #writes #queue 