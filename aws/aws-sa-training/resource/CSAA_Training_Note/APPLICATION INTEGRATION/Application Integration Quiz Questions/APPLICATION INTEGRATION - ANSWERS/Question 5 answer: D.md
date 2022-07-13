##### Question 5 answer: D


Explanation:


```

The key fact you need to consider here is that duplicate messages cannot be introduced into the

queue. For this reason alone you must use a FIFO queue. The statement about it not being

necessary to maintain the order of the messages is meant to confuse you, as that might lead you

to think you can use a standard queue, but standard queues don't guarantee that duplicates are

not introduced into the queue.

FIFO (first-in-first-out) queues preserve the exact order in which messages are sent and received

```


- note that this is not required in the question but exactly once processing is. FIFO queues provide exactly-once

  processing, which means that each message is delivered once and remains available until a consumer processes it and

  deletes it. Standard queues provide a loose-FIFO capability that attempts to preserve the order of messages. Standard

  queues provide at-least-once delivery, which means that each message is delivered at least once. Long polling is

  configuration you can apply to a queue, it is not a queue type. There is no such thing as an Auto Scaling queue.

