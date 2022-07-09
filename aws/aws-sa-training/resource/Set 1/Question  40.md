#### Question  40


**A Linux instance running in your VPC requires some configuration changes to be implemented locally and you need to run

some commands. Which of the following can be used to securely access the instance?**


1: SSL/TLS certificate


2: Public key


3: Key Pairs


4: EC2 password


Answer: 3


**Explanation:**


Amazon EC2 uses public key cryptography to encrypt and decrypt login information. Public key cryptography uses a public

key to encrypt a piece of data, and then the recipient uses the private key to decrypt the data. The public and private

keys are known as a _key pair_. Public key cryptography enables you to securely access your instances using a private

key instead of a password.


A key pair consists of a public key that AWS stores, and a private key file that you store:


- For Windows AMIs, the private key file is required to obtain the password used to log into your instance.

- For Linux AMIs, the private key file allows you to securely SSH into your instance.


- CORRECT "Key Pairs" is the correct answer.


- INCORRECT "SSL/TLS certificate" is incorrect as you cannot securely access an instance to run commands using an

  SSL/TLS certificate.


- INCORRECT "Public key" is incorrect. You cannot login to an EC2 instance using certificates/public keys.


- INCORRECT "EC2 password" is incorrect. The “EC2 password” might refer to the operating system password. By default you

  cannot login this way to Linux and must use a key pair. However, this can be enabled by setting a password and

  updating the /etc/ssh/sshd_config file.


**References:**


https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ec2/

