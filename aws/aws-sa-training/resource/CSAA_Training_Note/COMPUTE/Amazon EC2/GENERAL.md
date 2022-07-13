#### GENERAL


Amazon Elastic Compute Cloud (Amazon EC2) is a web service that provides resizable compute capacity in the cloud. It is

designed to make web-scale computing easier for developers.


With Amazon EC2 you launch virtual server instances on the AWS cloud.


Each virtual server is known as an “instance”.


You are limited to running up to a total of 20 On-Demand instances across the instance family, purchasing 20 Reserved

Instances, and requesting Spot Instances per your dynamic spot limit per region (by default).


AWS are transitioning to a vCPU based, rather than instance based, limit. This is currently being rolled out and may not

feature on the exam yet.


Amazon EC2 currently supports a variety of operating systems including: Amazon Linux, Ubuntu, Windows Server, Red Hat

Enterprise Linux, SUSE Linux Enterprise Server, Fedora, Debian, CentOS, Gentoo Linux, Oracle Linux, and FreeBSD.


EC2 compute units (ECU) provide the relative measure of the integer processing power of an Amazon EC2 instance.


With EC2 you have full control at the operating system layer.


**Key pairs are used to securely connect to EC2 instances:**


- A key pair consists of a **public key** that AWS stores, and a **private key file** that you store.

- For Windows AMIs, the private key file is required to obtain the password used to log into your instance.

- For Linux AMIs, the private key file allows you to securely SSH (secure shell) into your instance.


**Metadata and User Data:**


- User data is data that is supplied by the user at instance launch in the form of a script.

- Instance metadata is data about your instance that you can use to configure or manage the running instance.

- User data is limited to 16KB.

- User data and metadata are not encrypted.

- Instance metadata is available

  at [http://169.254.169.254/latest/meta-data/](http://169.254.169.254/latest/meta-data/) (the trailing “/” is required)

  .

- Instance user data is available

  at: [http://169.254.169.254/latest/user-data.](http://169.254.169.254/latest/user-data.)

- The IP address 169.254.169.254 is a link-local address and is valid only from the instance.

- On Linux you can use the curl command to view metadata and userdata, e.g.

  “curl [http://169.254.169.254/latest/meta-data/”.](http://169.254.169.254/latest/meta-data/”.)



- The Instance Metadata Query tool allows you to query the instance metadata without having to type out the full URI or

  category names.

