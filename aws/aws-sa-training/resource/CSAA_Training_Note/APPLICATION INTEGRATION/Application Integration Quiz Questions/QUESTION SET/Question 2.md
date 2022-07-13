##### Question 2


You are using a series of Spot instances that process messages from an SQS queue and store results in a DynamoDB table.

Shortly after picking up a message from the queue AWS terminated the Spot instance. The Spot instance had not finished

processing the message. What will happen to the message?


```

A. The message will be lost as it would have been deleted from the queue when processed

B. The message will remain in the queue and be immediately picked up by another instance

C. The message will become available for processing again after the visibility timeout expires

D. The results may be duplicated in DynamoDB as the message will likely be processed multiple

times

```

