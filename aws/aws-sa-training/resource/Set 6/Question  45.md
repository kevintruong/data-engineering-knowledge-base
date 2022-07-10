#### Question  45


**Several Amazon EC2 Spot instances are being used to process messages from an Amazon SQS queue and store results in an

Amazon DynamoDB table. Shortly after picking up a message from the queue AWS terminated the Spot instance. The Spot

instance had not finished processing the message. What will happen to the message?**


- [x] The message will become available for processing again after the visibility timeout expires


- [ ] The message will be lost as it would have been deleted from the queue when processed


- [ ] The message will remain in the queue and be immediately picked up by another instance


- [ ] The results may be duplicated in DynamoDB as the message will likely be processed multiple times


*

- hasExplain:: [[explanation_Question  45.md]]