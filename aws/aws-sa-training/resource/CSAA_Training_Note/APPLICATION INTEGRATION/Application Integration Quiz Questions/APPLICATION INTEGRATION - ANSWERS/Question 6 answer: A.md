##### Question 6 answer: A

Explanation:

```

The best option is to create multiple queues and configure the application to place orders onto a

specific queue based on the level of service. You then configure the back-end instances to poll

these queues in order or priority, so they pick up the higher priority jobs first.

Creating a combination of FIFO and standard queues is incorrect as creating a mixture of queue

types is not the best way to separate the messages, and there is nothing in this option that

explains how the messages would be picked up in the right order.

Creating a single queue and configuring the applications to place orders on the queue in order of

priority would not work as standard queues offer best-effort ordering so there’s no guarantee

that the messages would be picked up in the correct order.

```

Creating multiple SQS queues and configuring exactly-once processing (only
possible with FIFO)

would not ensure that the order of the messages is prioritized.

