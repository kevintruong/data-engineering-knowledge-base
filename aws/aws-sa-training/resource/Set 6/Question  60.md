#### Question  60


**An Amazon DynamoDB table has a variable load, ranging from sustained heavy usage some days, to only having small

spikes on others. The load is 80% read and 20% write. The provisioned throughput capacity has been configured to account

for the heavy load to ensure throttling does not occur.**


**What would be the most efficient solution to optimize cost?**


- [ ] Create a CloudWatch alarm that triggers an AWS Lambda function that adjusts the provisioned throughput


- [ ] Create a CloudWatch alarm that notifies you of increased/decreased load, and manually adjust the provisioned

throughput


- [ ] Use DynamoDB DAX to increase the performance of the database


- [x] Create a DynamoDB Auto Scaling scaling policy


*

- hasExplain:: [[explanation_Question  60.md]]

#dynamodb #throttling #cloudwatch #aws #optimize 