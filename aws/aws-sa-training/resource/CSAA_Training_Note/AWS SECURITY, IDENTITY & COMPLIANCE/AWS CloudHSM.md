### AWS CloudHSM

The AWS CloudHSM service helps you meet corporate, contractual and regulatory
compliance requirements for data security

by using dedicated Hardware Security Module (HSM) instances within the AWS
cloud.

AWS and AWS Marketplace partners offer a variety of solutions for protecting
sensitive data within the AWS platform, but

for some applications and data subject to contractual or regulatory mandates for
managing cryptographic keys, additional

protection may be necessary.

CloudHSM complements existing data protection solutions and allows you to
protect your encryption keys within HSMs that

are designed and validated to government standards for secure key management.

CloudHSM allows you to securely generate, store and manage cryptographic keys
used for data encryption in a way that

keys are accessible only by you.

A Hardware Security Module (HSM) provides secure key storage and cryptographic
operations within a tamper-resistant

hardware device.

HSMs are designed to securely store cryptographic key material and use the key
material without exposing it outside the

cryptographic boundary of the hardware.

You can use the CloudHSM service to support a variety of use cases and
applications, such as database encryption,

Digital Rights Management (DRM), Public Key Infrastructure (PKI), authentication
and authorization, document signing,

and transaction processing.

Runs on a dedicated hardware device, single tenanted.

The table below describes the latest version of CloudHSM and how it differs from
its predecessor:

When you use the AWS CloudHSM service you create a CloudHSM Cluster.

Clusters can contain multiple HSM instances, spread across multiple Availability
Zones in a region.

HSM instances in a cluster are automatically synchronized and load-balanced.

You receive dedicated, single-tenant access to each HSM instance in your
cluster. Each HSM instance appears as a network

resource in your Amazon Virtual Private Cloud (VPC).

Adding and removing HSMs from your Cluster is a single call to the AWS CloudHSM
API (or on the command line using the

AWS CLI).

After creating and initializing a CloudHSM Cluster, you can configure a client
on your EC2 instance that allows your

applications to use the cluster over a secure, authenticated network connection.

Must be within a VPC and can be accessed via VPC Peering.

Applications don’t need to be in the same VPC but but the server or instance on
which your application and the HSM

client are running must have network (IP) reachability to all HSMs in the
cluster.

Does not natively integrate with many AWS services like KMS, but instead
requires custom application scripting.

Offload SSL from web server, act as an issuing CA, enable TDE for Oracle
databases. The table below compares CloudHSM

against KMS:

