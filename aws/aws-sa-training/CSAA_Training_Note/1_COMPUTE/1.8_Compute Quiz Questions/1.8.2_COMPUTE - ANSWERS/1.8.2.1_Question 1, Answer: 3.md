##### Question 1, Answer: 3


**Explanation:**


```

1 is incorrect. Signed cookies are not an authentication method for EC2.

2 is incorrect. An access key ID and secret access key are used for programmatic access to AWS

services, not for securely connecting to Linux instances over SSH. Make sure you know the

difference between these two concepts.

3 is correct. Key pairs are used to securely connect to EC2 instances. A key pair consists of a

public key that AWS stores, and a private key file that you store. For Linux AMIs, the private

key file allows you to securely SSH (secure shell) into your instance.

4 is incorrect. You do not need a password to connect to instances launched from the Amazon

Linux 2 AMI.

```

