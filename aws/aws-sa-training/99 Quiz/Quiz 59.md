## Quiz 59: A Solutions Architect is developing an encryption solution. The solution requires that data keys are encrypted using envelope protection before they are written to disk.**

**Which solution option can assist with this requirement?**

- [ ] API Gateway with STS
- [ ] IAM Access Key
- [ ] AWS Certificate Manager
- [ ] AWS KMS API

----
Answer: 4
**Explanation:**
When you encrypt your data, your data is protected, but you have to protect your encryption key. One strategy is to encrypt it. _Envelope encryption_ is the practice of encrypting plaintext data with a data key, and then encrypting the data key under another key.
![](aws-solution-architecture-practice-quiz-1641093879933.png)
Envelope encryption offers several benefits:

- **Protecting data keys**
  When you encrypt a data key, you don't have to worry about storing the encrypted data key, because the data key is inherently protected by encryption. You can safely store the encrypted data key alongside the encrypted data.
- **Encrypting the same data under multiple master keys**
  Encryption operations can be time consuming, particularly when the data being encrypted are large objects. Instead of re-encrypting raw data multiple times with different keys, you can re-encrypt only the data keys that protect the raw data.
- **Combining the strengths of multiple algorithms**
  In general, symmetric key algorithms are faster and produce smaller ciphertexts than public key algorithms. But public key algorithms provide inherent separation of roles and easier key management. Envelope encryption lets you combine the strengths of each strategy.
- ✅: "AWS KMS API" is the correct answer.
- ❌: "API Gateway with STS" is incorrect. The AWS Security Token Service (STS) is a web service that enables you to request temporary, limited-privilege credentials for AWS Identity and Access Management

  (IAM) users or for users that you authenticate (federated users).
- ❌: "IAM Access Key" is incorrect. IAM access keys are used for signing programmatic requests you make to AWS.
- ❌: "AWS Certificate Manager" is incorrect. AWS Certificate Manager is a service that lets you easily provision, manage, and deploy public and private Secure Sockets Layer/Transport Layer Security (SSL/TLS)

  certificates for use with AWS services and your internal connected resources.
  **References:**
  https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html
  https://docs.aws.amazon.com/kms/latest/APIReference/Welcome.html
