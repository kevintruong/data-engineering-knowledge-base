#### SECURITY


You can use IAM policies to control who can read/write messages.


Authentication can be used to secure messages within queues (who can send and receive).


SQS supports HTTPS and supports TLS versions 1.0, 1.1, 1.2.


SQS is PCI DSS level 1 compliant and HIPAA eligible.


**Server-side encryption (SSE) lets you transmit sensitive data in encrypted queues (AWS KMS):**


- SSE encrypts messages as soon as SQS receives them.

- The messages are stored in encrypted form and SQS decrypts messages only when they are


```

sent to an authorized consumer.

```


- Uses AES 256 bit encryption.

- Not available in all regions.

- Standard and FIFO queues.

- Body of message is encrypted.


**The following is not encrypted:**


- Queue metadata.

- Message metadata.

- Per-queue metrics.

