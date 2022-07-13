#### POLLING

SQS uses short polling and long polling.

**Short polling:**

- Does not wait for messages to appear in the queue.


- It queries only a subset of the available servers for messages (based on
  weighted random execution).

- Short polling is the default.

- ReceiveMessageWaitTime is set to 0.

- More requests are used, which implies higher cost.

**Long polling:**

- Uses fewer requests and reduces cost.

- Eliminates false empty responses by querying all servers.

- SQS waits until a message is available in the queue before sending a response.

- Requests contain at least one of the available messages up to the maximum
  number of messages specified in the

  ReceiveMessage action.

- Shouldn’t be used if your application expects an immediate response to receive
  message calls.

- ReceiveMessageWaitTime is set to a non-zero value (up to 20 seconds).

- Same charge per million requests as short polling.

