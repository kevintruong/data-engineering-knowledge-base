#### Question  45


**Several Amazon EC2 Spot instances are being used to process messages from an Amazon SQS queue and store results in an

Amazon DynamoDB table. Shortly after picking up a message from the queue AWS terminated the Spot instance. The Spot

instance had not finished processing the message. What will happen to the message?**


1: The message will become available for processing again after the visibility timeout expires


2: The message will be lost as it would have been deleted from the queue when processed


3: The message will remain in the queue and be immediately picked up by another instance


4: The results may be duplicated in DynamoDB as the message will likely be processed multiple times


**Answer: 1**


**Explanation:**


The visibility timeout is the amount of time a message is invisible in the queue after a reader picks up the message. If

a job is processed within the visibility timeout the message will be deleted. If a job is not processed within the

visibility timeout the message will become visible again (could be delivered twice). The maximum visibility timeout for

an Amazon SQS message is 12 hours.


- CORRECT "The message will become available for processing again after the visibility timeout expires" is the correct

  answer.


- INCORRECT "The message will be lost as it would have been deleted from the queue when processed" is incorrect. The

  message will not be lost and will not be immediately picked up by another instance.


```

SQS Queue

```


```

1

```


```

Message cannot be

returned

```


```

Timeline

```


```

Delay Seconds

```


```

1

```


```

Message is visible

```


```

Message received

```


```

Consumer

```


```

Producer

```


```

Visibility Timeout

```


```

1

```


```

Message is invisible

```


```

Message fails to

process

```


```

1

```


```

Message becomes

visible again

```


- INCORRECT "The message will remain in the queue and be immediately picked up by another instance" is incorrect. As

  mentioned above it will be available for processing in the queue again after the timeout expires.


- INCORRECT "The results may be duplicated in DynamoDB as the message will likely be processed multiple times" is

  incorrect. As the instance had not finished processing the message it should only be fully processed once. Depending

  on your application process however it is possible some data was written to DynamoDB.


**References:**


https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-

timeout.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/application-

integration/amazon-sqs/

