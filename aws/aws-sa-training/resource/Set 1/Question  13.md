#### Question  13


**A solutions architect is designing an application on AWS. The compute layer will run in parallel across EC2 instances.

The compute layer should scale based on the number of jobs to be processed. The compute layer is stateless. The

solutions architect must ensure that the application is loosely coupled and the job items are durably stored.**


**Which design should the solutions architect use?**


- [ ] Create an Amazon SNS topic to send the jobs that need to be processed. Create an Amazon EC2 Auto Scaling group for

the compute application. Set the scaling policy for the Auto Scaling group to add and remove nodes based on CPU usage


- [ ] Create an Amazon SQS queue to hold the jobs that need to be processed. Create an Amazon EC2 Auto Scaling group for

the compute application. Set the scaling policy for the Auto Scaling group to add and remove nodes based on network

usage


- [x] Create an Amazon SQS queue to hold the jobs that needs to be processed. Create an Amazon EC2 Auto Scaling group for

the compute application. Set the scaling policy for the Auto Scaling group to add and remove nodes based on the number

of items in the SQS queue


- [ ] Create an Amazon SNS topic to send the jobs that need to be processed. Create an Amazon EC2 Auto Scaling group for

the compute application. Set the scaling policy for the Auto Scaling group to add and remove nodes based on the number

of messages published to the SNS topic



- hasExplain:: [[explanation_Question  13.md]]

#aws #ec2 #scaling #queue #nodes 