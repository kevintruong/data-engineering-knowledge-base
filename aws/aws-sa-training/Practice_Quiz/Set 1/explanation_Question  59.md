**Explanation:**

When you encrypt your data, your data is protected, but you have to protect your encryption key. One strategy is to

encrypt it. _Envelope encryption_ is the practice of encrypting plaintext data with a data key, and then encrypting the

data key under another key.

Envelope encryption offers several benefits:

- **Protecting data keys**

When you encrypt a data key, you don't have to worry about storing the encrypted data key, because the data key is

inherently protected by encryption. You can safely store the encrypted data key alongside the encrypted data.

- **Encrypting the same data under multiple master keys**

Encryption operations can be time consuming, particularly when the data being encrypted are large objects. Instead of

re-encrypting raw data multiple times with different keys, you can re-encrypt only the data keys that protect the raw

data.

- **Combining the strengths of multiple algorithms**

In general, symmetric key algorithms are faster and produce smaller ciphertexts than public key algorithms. But public

key algorithms provide inherent separation of roles and easier key management. Envelope encryption lets you combine the

strengths of each strategy.

- ✅ :  "AWS KMS API" is the correct answer.

- ❌ :  "API Gateway with STS" is incorrect. The AWS Security Token Service (STS) is a web service that enables you

  to request temporary, limited-privilege credentials for AWS Identity and Access Management

  (IAM) users or for users that you authenticate (federated users).

- ❌ :  "IAM Access Key" is incorrect. IAM access keys are used for signing programmatic requests you make to AWS.

- ❌ :  "AWS Certificate Manager" is incorrect. AWS Certificate Manager is a service that lets you easily provision,

  manage, and deploy public and private Secure Sockets Layer/Transport Layer Security (SSL/TLS)

  certificates for use with AWS services and your internal connected resources.

```

Data Key

Encryption Encrypted^ data

algorithm

```

```

Plaintext data

```

```

Encryption

algorithm

```

```

Encryption

Message

```

```

Data Key Master Key Encrypted Data

Key

```

```

Data encrypted with data key

```

```

Data key encrypted with

master key

```

```

Encrypteddata and encrypted

data keys returned in a single

encrypted message

```

**References:**

<https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html>

**Save time with our exam-specific cheat sheets:**

<https://docs.aws.amazon.com/kms/latest/APIReference/Welcome.html>

----

- #envelope_encryption #envelope_encryption__ #encryption_operations #encryption #easier_key_management
