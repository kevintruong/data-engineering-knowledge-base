#### LIMITS

In-flight messages are messages that have been picked up by a consumer but not
yet deleted from the queue.

Standard queues have a limit of 120,000 in-flight messages per queue.

FIFO queues have a limit of 20,000 in-flight messages per queue.

Queue names can be up to 80 characters.

Messages are retained for 4 days by default up to 14 days.

FIFO queues support up to 3000 messages per second when batching or 300 per
second otherwise.

The maximum messages size is 256KB.

