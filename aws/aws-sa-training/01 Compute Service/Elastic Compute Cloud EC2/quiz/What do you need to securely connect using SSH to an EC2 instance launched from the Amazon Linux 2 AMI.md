## What do you need to securely connect using SSH to an EC2 instance launched from the Amazon Linux 2 AMI

<!-- #ec2_keypair -->

- [ ] A signed cookie
- [ ] An access key ID and secret access key
- [x] A key pair
- [ ] A password

----

**Question 1 Answer: a Key Pair **

**Explanation:**

- A signed cookie is incorrect. Signed cookies are not an authentication method for EC- [ ]
- An access key ID and secret access key is incorrect. An access key ID and secret access key are used for programmatic access to AWS services, not for securely connecting to Linux instances over SSH. Make sure you know the difference between these two concepts.
- A key pair is correct. Key pairs are used to securely connect to EC2 instances. A key pair consists of a public key that AWS stores, and a private key file that you store. For Linux AMIs, the private key file allows you to securely SSH (secure shell) into your instance.
- A password is incorrect. You do not need a password to connect to instances launched from the Amazon Linux 2 AMI.


----
#quiz 
relateTo:: [[EC2]]
belongTo:: [[aws_compute_quiz]]