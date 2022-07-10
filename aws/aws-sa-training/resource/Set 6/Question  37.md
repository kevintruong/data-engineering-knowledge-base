#### Question  37

**A web application receives order processing information from customers and places the messages on an Amazon SQS queue.

A fleet of Amazon EC2 instances are configured to pick up the messages, process them, and store the results in a

DynamoDB table. The current configuration has been resulting in a large number of empty responses to ReceiveMessage API

requests.**

**A Solutions Architect needs to eliminate empty responses to reduce operational overhead. How can this be done?**

- [ ] Use a Standard queue to provide at-least-once delivery, which means that each message is delivered at least once

- [ ] Use a FIFO (first-in-first-out) queue to preserve the exact order in which messages are sent and received

- [x] Configure Long Polling to eliminate empty responses by allowing Amazon SQS to wait until a message is available in a

queue before sending a response

- [ ] Configure Short Polling to eliminate empty responses by reducing the length of time a connection request remains open

*

- hasExplain:: [[explanation_Question  37.md]]
