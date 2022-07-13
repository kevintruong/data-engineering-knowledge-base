##### Question 2 answer: C


Explanation:


```

The visibility timeout is the amount of time a message is invisible in the queue after a reader

picks up the message. If a job is processed within the visibility timeout the message will be

deleted. If a job is not processed within the visibility timeout the message will become visible

again (could be delivered twice). The maximum visibility timeout for an Amazon SQS message is

12 hours.

The message will not be lost and will not be immediately picked up by another instance. As

mentioned above it will be available for processing in the queue again after the timeout expires.

As the instance had not finished processing the message it should only be fully processed once.

Depending on your application process however it is possible some data was written to

DynamoDB.

```

