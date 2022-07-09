#### Question  60


**An Amazon DynamoDB table has a variable load, ranging from sustained heavy usage some days, to only having small

spikes on others. The load is 80% read and 20% write. The provisioned throughput capacity has been configured to account

for the heavy load to ensure throttling does not occur.**


**What would be the most efficient solution to optimize cost?**


1: Create a CloudWatch alarm that triggers an AWS Lambda function that adjusts the provisioned throughput


2: Create a CloudWatch alarm that notifies you of increased/decreased load, and manually adjust the provisioned

throughput


3: Use DynamoDB DAX to increase the performance of the database


4: Create a DynamoDB Auto Scaling scaling policy


**Answer: 4**


**Explanation:**


_Amazon DynamoDB auto scaling_ uses the AWS Application Auto Scaling service to dynamically adjust provisioned

throughput capacity on your behalf, in response to actual traffic patterns. This is the most efficient and

cost-effective solution to optimizing for cost.


- CORRECT "Create a DynamoDB Auto Scaling scaling policy" is the correct answer.


- INCORRECT "Create a CloudWatch alarm that triggers an AWS Lambda function that adjusts the provisioned throughput"

  is incorrect. Using AWS Lambda to modify the provisioned throughput is possible but it would be more cost-effective to

  use DynamoDB Auto Scaling as there is no cost to using it.


- INCORRECT "Create a CloudWatch alarm that notifies you of increased/decreased load, and manually adjust the

  provisioned throughput" is incorrect. Manually adjusting the provisioned throughput is not efficient.


- INCORRECT "Use DynamoDB DAX to increase the performance of the database" is incorrect. DynamoDB DAX is an in-memory

  cache that increases the performance of DynamoDB. However, it costs money and there is no requirement to increase

  performance.


**References:**


https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AutoScaling.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-

dynamodb/

