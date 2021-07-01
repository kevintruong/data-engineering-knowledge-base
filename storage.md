
## STORAGE

### Amazon S3

**GENERAL**

Amazon S3 is object storage built to store and retrieve any amount of data from anywhere on the
Internet.

It’s a simple storage service that offers an extremely durable, highly available, and infinitely scalable
data storage infrastructure at very low costs.

Amazon S3 is a distributed architecture and objects are redundantly stored on multiple devices
across multiple facilities (AZs) in an Amazon S3 region.

Amazon S3 is a simple key-based object store.

Keys can be any string, and they can be constructed to mimic hierarchical attributes.

Alternatively, you can use S3 Object Tagging to organize your data across all of your S3 buckets
and/or prefixes.

Amazon S3 provides a simple, standards-based REST web services interface that is designed to work
with any Internet-development toolkit.

Files can be from 0 bytes to 5TB.

The largest object that can be uploaded in a single PUT is 5 gigabytes.

For objects larger than 100 megabytes use the Multipart Upload capability.

Updates to an object are atomic – when reading an updated object, you will either get the new
object or the old one, you will never get partial or corrupt data.

There is unlimited storage available.

It is recommended to access S3 through SDKs and APIs (the console uses APIs).

Event notifications for specific actions, can send alerts or trigger actions.

**Notifications can be sent to:**

- SNS Topics.
- SQS Queue.
- Lambda functions.
- Need to configure SNS/SQS/Lambda before S3.
- No extra charges from S3 but you pay for SNS, SQS and Lambda.

Requester pays function causes the requester to pay (removes anonymous access).

Can provide time-limited access to objects.

Provides read after write consistency for PUTS of new objects.

Provides eventual consistency for overwrite PUTS and DELETES (takes time to propagate).


You can only store files (objects) on S3.

HTTP 200 code indicates a successful write to S3.

**S3 data is made up of:**

- Key (name)
- Value (data)
- Version ID
- Metadata
- Access Control Lists

Amazon S3 automatically scales to high request rates.

For example, your application can achieve at least 3,500 PUT/POST/DELETE and 5,500 GET requests
per second per prefix in a bucket.

There are no limits to the number of prefixes in a bucket. It is simple to increase your read or write
performance exponentially.

For read intensive requests you can also use CloudFront edge locations to offload from S3.

**ADDITIONAL CAPABILITIES**

Additional capabilities offered by Amazon S3 include:

**USE CASES**

**Typical use cases include:**

- Backup and Storage – Provide data backup and storage services for others.
- Application Hosting – Provide services that deploy, install, and manage web applications.
- Media Hosting – Build a redundant, scalable, and highly available infrastructure that hosts
    video, photo, or music uploads and downloads.


- Software Delivery – Host your software applications that customers can download.
- Static Website – you can configure a static website to run from an S3 bucket.

S3 is a persistent, highly durable data store.

Persistent data stores are non-volatile storage systems that retain data when powered off.

This is in contrast to transient data stores and ephemeral data stores which lose the data when
powered off.

The following table provides a description of persistent, transient and ephemeral data stores and
which AWS service to use:

**BUCKETS**

**Files are stored in buckets:**

- A bucket can be viewed as a container for objects.
- A bucket is a flat container of objects.
- It does not provide a hierarchy of objects.
- You can use an object key name to mimic folders.

100 buckets per account by default.

You can store unlimited objects in your buckets.

You can create folders in your buckets (only available through the Console).

You cannot create nested buckets.

Bucket ownership is not transferrable.

Bucket names cannot be changed after they have been created.

If a bucket is deleted its name becomes available again.

Bucket names are part of the URL used to access the bucket.

An S3 bucket is region specific.

S3 is a universal namespace so names must be unique globally.


URL is in this format: https://s3- **_eu-west- 1_** .amazonaws.com/ **_<bucketname>._**

Can backup a bucket to another bucket in another account.

Can enable logging to a bucket.

**Bucket naming:**

- Bucket names must be at least 3 and no more than 63 character in length.
- Bucket names must start and end with a lowercase character or a number.
- Bucket names must be a series of one or more labels which are separated by a period.
- Bucket names can contain lowercase letters, numbers and hyphens.
- Bucket names cannot be formatted as an IP address.

For better performance, lower latency, and lower cost, create the bucket closer to your clients.

**OBJECTS**

Each object is stored and retrieved by a unique key (ID or name).

**An object in S3 is uniquely identified and addressed through:**

- Service end-point.
- Bucket name.
- Object key (name).
- Optionally, an object version.

Objects stored in a bucket will never leave the region in which they are stored unless you move
them to another region or enable cross-region replication.

You can define permissions on objects when uploading and at any time afterwards using the AWS
Management Console.

**SUB-RESOURCES**

- Sub-resources are subordinate to objects, they do not exist independently but are always
    associated with another entity such as an object or bucket.
- Sub-resources (configuration containers) associated with buckets include:
- Lifecycle – define an object’s lifecycle.
- Website – configuration for hosting static websites.
- Versioning – retain multiple versions of objects as they are changed.
- Access Control Lists (ACLs) – control permissions access to the bucket.
- Bucket Policies – control access to the bucket.
- Cross Origin Resource Sharing (CORS).
- Logging
- Sub-resources associated with objects include:
- ACLs – define permissions to access the object.
- Restore – restoring an archive.

**STORAGE CLASSES**

**There are six S3 storage classes.**


- S3 Standard (durable, immediately available, frequently accessed).
- S3 Intelligent-Tiering (automatically moves data to the most cost-effective tier).
- S3 Standard-IA (durable, immediately available, infrequently accessed).
- S3 One Zone-IA (lower cost for infrequently accessed data with less resilience).
- S3 Glacier (archived data, retrieval times in minutes or hours).
- S3 Glacier Deep Archive (lowest cost storage class for long term retention).

The table below provides the details of each Amazon S3 storage class:

Objects stored in the S3 One Zone-IA storage class are stored redundantly within a single
Availability Zone in the AWS Region you select.

**ACCESS AND ACCESS POLICIES**

**There are four mechanisms for controlling access to Amazon S3 resources:**

- IAM policies.
- Bucket policies.
- Access Control Lists (ACLs).
- Query string authentication (URL to an Amazon S3 object which is only valid for a limited
    time).

Access auditing can be configured by configuring an Amazon S3 bucket to create access log records
for all requests made against it.

For capturing IAM/user identity information in logs configure AWS CloudTrail Data Events.

By default, a bucket, its objects, and related sub-resources are all private.

By default, only a resource owner can access a bucket.

The resource owner refers to the AWS account that creates the resource.

With IAM the account owner rather than the IAM user is the owner.

Within an IAM policy you can grant either programmatic access or AWS Management Console
access to Amazon S3 resources.


Amazon Resource Names (ARN) are used for specifying resources in a policy.

**The format for any resource on AWS is:**

arn:partition:service:region:namespace:relative-id.

**For S3 resources:**

- aws is a common partition name.
- s3 is the service.
- You don’t specify Region and namespace.
- For Amazon S3, it can be a bucket-name or a bucket-name/object-key. You can use wild
    card

**The format for S3 resources is:**

arn:aws:s3:::bucket_name.

arn:aws:s3:::bucket_name/key_name.

A bucket owner can grant cross-account permissions to another AWS account (or users in an
account) to upload objects.

The AWS account that uploads the objects owns them.

The bucket owner does not have permissions on objects that other accounts own, however:

- The bucket owner pays the charges.
- The bucket owner can deny access to any objects regardless of ownership.
- The bucket owner can archive any objects or restore archived objects regardless of
    ownership.

**Access to buckets and objects can be granted to:**

- Individual users.
- AWS accounts.
- Everyone (public/anonymous).
- All authenticated users (AWS users).

Access policies define access to resources and can be associated with resources (buckets and
objects) and users.

You can use the AWS Policy Generator to create a bucket policy for your Amazon S3 bucket.

The categories of policy are resource-based policies and user policies.

**Resource-based policies:**

- Attached to buckets and objects.
- ACL-based policies define permissions.
- ACLs can be used to grant read/write permissions to other accounts.
- Bucket policies can be used to grant other AWS accounts or IAM users permission to the
    bucket and objects.

**User policies:**


- Can use IAM to manage access to S3 resources.
- Using IAM you can create users, groups and roles and attach access policies to them
    granting them access to resources.
- You cannot grant anonymous permissions in an IAM user policy as the policy is attached to a
    user.
- User policies can grant permissions to a bucket and the objects in it.

**ACLs:**

- S3 ACLs enable you to manage access to buckets and objects.
- Each bucket and object has an ACL attached to it as a subresource.
- Bucket and object permissions are independent of each other.
- The ACL defines which AWS accounts (grantees) or pre-defined S3 groups are granted
    access and the type of access.
- A grantee can be an AWS account or one of the predefined Amazon S3 groups.
- When you create a bucket or an object, S3 creates a default ACL that grants the resource
    owner full control over the resource.

**Cross account access:**

- You grant permission to another AWS account using the email address or the canonical user
    ID.
- However, if you provide an email address in your grant request, Amazon S3 finds the
    canonical user ID for that account and adds it to the ACL.
- Grantee accounts can then then delegate the access provided by other accounts to their
    individual users.

**PRE-DEFINED GROUPS**

**Authenticated Users group:**

- This group represents all AWS accounts.
- Access permission to this group allows any AWS account access to the resource.
- All requests must be signed (authenticated).
- Any authenticated user can access the resource.

**All Users group:**

- Access permission to this group allows anyone in the world access to the resource.
- The requests can be signed (authenticated) or unsigned (anonymous).
- Unsigned requests omit the authentication header in the request.
- AWS recommends that you never grant the All Users group WRITE, WRITE_ACP, or
    FULL_CONTROL permissions.

**Log Delivery group:**

- Providing WRITE permission to this group on a bucket enables S3 to write server access logs.
- Not applicable to objects.

**The following table lists the set of permissions that Amazon S3 supports in an ACL:**

- The set of ACL permissions is the same for an object ACL and a bucket ACL.


- Depending on the context (bucket ACL or object ACL), these ACL permissions grant
    permissions for specific buckets or object operations.
- The table lists the permissions and describes what they mean in the context of objects and
    buckets.

**Note the following:**

- Permissions are assigned at the account level for authenticated users.
- You cannot assign permissions to individual IAM users.
- When Read is granted on a bucket it only provides the ability to list the objects in the
    bucket.
- When Read is granted on an object the data can be read.
- ACP means access control permissions and READ_ACP/WRITE_ACP control who can
    read/write the ACLs themselves.
- WRITE is only applicable to the bucket level (except for ACP).

Bucket policies are limited to 20 KB in size.

Object ACLs are limited to 100 granted permissions per ACL.

The only recommended use case for the bucket ACL is to grant write permissions to the S3 Log
Delivery group.

**There are limits to managing permissions using ACLs:**

- You cannot grant permissions to individual users.
- You cannot grant conditional permissions.
- You cannot explicitly deny access.

When granting other AWS accounts the permissions to upload objects, permissions to these objects
can only be managed by the object owner using object ACLs.

**You can use bucket policies for:**


- Granting users permissions to a bucket owned by your account.
- Managing object permissions (where the object owner is the same account as the bucket
    owner).
- Managing cross-account permissions for all Amazon S3 permissions.

**You can use user policies for:**

- Granting permissions for all Amazon S3 operations.
- Managing permissions for users in your account.
- Granting object permissions to users within the account.

**For an IAM user to access resources in another account the following must be provided:**

- Permission from the parent account through a user policy.
- Permission from the resource owner to the IAM user through a bucket policy, or the parent
    account through a bucket policy, bucket ACL or object ACL.

If an AWS account owns a resource it can grant permissions to another account, that account can
then delegate those permissions or a subset of them to uses in the account (permissions
delegation).

An account that receives permissions from another account cannot delegate permissions cross-
account to a third AWS account.

**CHARGES**

No charge for data transferred between EC2 and S3 in the same region.

Data transfer into S3 is free of charge.

Data transferred to other regions is charged.

Data Retrieval (applies to S3 Standard-IA and S3 One Zone-IA, S3 Glacier and S3 Glacier Deep
Archive).

**Charges are:**

- Per GB/month storage fee.
- Data transfer out of S3.
- Upload requests (PUT and GET).
- Retrieval requests (S3-IA or Glacier).

**Requester pays:**

- The bucket owner will only pay for object storage fees.
- The requester will pay for requests (uploads/downloads) and data transfers.
- Can only be enabled at the bucket level.

**MULTIPART UPLOAD**

Can be used to speed up uploads to S3.

Multipart upload uploads objects in parts independently, in parallel and in any order.

Performed using the S3 Multipart upload API.


It is recommended for objects of 100MB or larger.

Can be used for objects from 5MB up to 5TB.

Must be used for objects larger than 5GB.

If transmission of any part fails it can be retransmitted.

Improves throughput.

Can pause and resume object uploads.

Can begin upload before you know the final object size.

**COPY**

You can create a copy of objects up to 5GB in size in a single atomic operation.

For files larger than 5GB you must use the multipart upload API.

Can be performed using the AWS SDKs or REST API.

**The copy operation can be used to:**

- Generate additional copies of objects.
- Renaming objects.
- Changing the copy’s storage class or encryption at rest status.
- Move objects across AWS locations/regions.
- Change object metadata.

Once uploaded to S3 some object metadata cannot be changed, copying the object can allow you to
modify this information.

**TRANSFER ACCELERATION**

Amazon S3 Transfer Acceleration enables fast, easy, and secure transfers of files over long distances
between your client and your Amazon S3 bucket.

S3 Transfer Acceleration leverages Amazon CloudFront’s globally distributed AWS Edge Locations.

Used to accelerate object uploads to S3 over long distances (latency).

Transfer acceleration is as secure as a direct upload to S3.

You are charged only if there was a benefit in transfer times.

Need to enable transfer acceleration on the S3 bucket.

Cannot be disabled, can only be suspended.

May take up to 30 minutes to implement.

URL is: <bucketname>.s3-accelerate.amazonaws.com.

Bucket names must be DNS compliance and cannot have periods between labels.

Now HIPAA compliant.

You can use multipart uploads with transfer acceleration.


**Must use one of the following endpoints:**

- .s3-accelerate.amazonaws.com.
- .s3-accelerate.dualstack.amazonaws.com (dual-stack option).

S3 Transfer Acceleration supports all bucket level features including multipart uploads.

**STATIC WEBSITES**

S3 can be used to host static websites.

Cannot use dynamic content such as PHP, .Net etc.

Automatically scales.

You can use a custom domain name with S3 using a Route 53 Alias record.

When using a custom domain name the bucket name must be the same as the domain name.

Can enable redirection for the whole domain, pages or specific objects.

URL is: <bucketname>.s3-website-.amazonaws.com.

Requester pays does not work with website endpoints.

Does not support HTTPS/SSL.

Returns an HTML document.

Supports object and bucket level redirects.

Only supports GET and HEAD requests on objects.

Supports publicly readable content only.

**To enable website hosting on a bucket, specify:**

- An Index document (default web page)
- Error document (optional)


**PRE-SIGNED URLS**

Pre-signed URLs can be used to provide temporary access to a specific object to those who do not
have AWS credentials.

By default, all objects are private and can only be accessed by the owner.

To share an object, you can either make it public or generate a pre-signed URL.

Expiration date and time must be configured.

These can be generated using SDKs for Java and .Net and AWS explorer for Visual Studio.

Can be used for downloading and uploading S3 objects.

**VERSIONING**

Versioning stores all versions of an object (including all writes and even if an object is deleted).

Versioning protects against accidental object/data deletion or overwrites.

Enables “roll-back” and “un-delete” capabilities.

Versioning can also be used for data retention and archive.

Old versions count as billable size until they are permanently deleted.

Enabling versioning does not replicate existing objects.

Can be used for backup.

Once enabled versioning cannot be disabled only suspended.

Can be integrated with lifecycle rules.


Multi-factor authentication (MFA) delete can be enabled.

MFA delete can also be applied to changing versioning settings.

**MFA delete applies to:**

- Changing the bucket’s versioning state.
- Permanently deleting an object.

Cross Region Replication requires versioning to be enabled on the source and destination buckets.

Reverting to previous versions isn’t replicated.

By default, a HTTP GET retrieves the most recent version.

Only the S3 bucket owner can permanently delete objects once versioning is enabled.

When you try to delete an object with versioning enabled a DELETE marker is placed on the object.

You can delete the DELETE marker and the object will be available again.

Deletion with versioning replicates the delete marker. But deleting the delete marker is not
replicated.

**Bucket versioning states:**

- Enabled
- Versioned
- Un-versioned

Objects that existed before enabling versioning will have a version ID of NULL.

**Suspension:**

- If you suspend versioning the existing objects remain as they are however new versions will
    not be created.
- While versioning is suspended new objects will have a version ID of NULL and uploaded
    objects of the same name will overwrite the existing object.

**LIFECYCLE MANAGEMENT**

Used to optimize storage costs, adhere to data retention policies and to keep S3 volumes well-
maintained.

A _lifecycle configuration_ is a set of rules that define actions that Amazon S3 applies to a group of
objects. There are two types of actions:

- **Transition actions** —Define when objects transition to another storage class. For example,
    you might choose to transition objects to the STANDARD_IA storage class 30 days after you
    created them, or archive objects to the GLACIER storage class one year after creating them.

There are costs associated with the lifecycle transition requests. For pricing information, see
Amazon S3 Pricing.

- **Expiration actions** —Define when objects expire. Amazon S3 deletes expired objects on your
    behalf.


Lifecycle configuration is an XML file applied at the bucket level as a subresource.

Can be used in conjunction with versioning or independently.

Can be applied to current and previous versions.

Can be applied to specific objects within a bucket: objects with a specific tag or objects with a
specific prefix.

**Supported Transitions and Related Constraints**

**Amazon S3 supports the following lifecycle transitions between storage classes using a lifecycle
configuration:**

- You can transition from the STANDARD storage class to any other storage class.
- You can transition from any storage class to the GLACIER or DEEP_ARCHIVE storage classes.
- You can transition from the STANDARD_IA storage class to the INTELLIGENT_TIERING or
    ONEZONE_IA storage classes.
- You can transition from the INTELLIGENT_TIERING storage class to the ONEZONE_IA storage
    class.
- You can transition from the GLACIER storage class to the DEEP_ARCHIVE storage class.

**The following lifecycle transitions are not supported:**

- You can't transition from any storage class to the STANDARD storage class.
- You can't transition from any storage class to the REDUCED_REDUNDANCY storage class.
- You can't transition from the INTELLIGENT_TIERING storage class to the STANDARD_IA
    storage class.
- You can't transition from the ONEZONE_IA storage class to the STANDARD_IA or
    INTELLIGENT_TIERING storage classes.
- You can transition from the GLACIER storage class to the DEEP_ARCHIVE storage class only.
- You can't transition from the DEEP_ARCHIVE storage class to any other storage class.

**The lifecycle storage class transitions have the following constraints:**

- From the STANDARD or STANDARD_IA storage class to INTELLIGENT_TIERING. The following
    constraints apply:
    o For larger objects, there is a cost benefit for transitioning to INTELLIGENT_TIERING.
       Amazon S3 does not transition objects that are smaller than 128 KB to the
       INTELLIGENT_TIERING storage class because it's not cost effective.
- From the STANDARD storage classes to STANDARD_IA or ONEZONE_IA. The following
    constraints apply:
    o For larger objects, there is a cost benefit for transitioning to STANDARD_IA or
       ONEZONE_IA. Amazon S3 does not transition objects that are smaller than 128 KB to the
       STANDARD_IA or ONEZONE_IA storage classes because it's not cost effective.
    o Objects must be stored at least 30 days in the current storage class before you can
       transition them to STANDARD_IA or ONEZONE_IA. For example, you cannot create a
       lifecycle rule to transition objects to the STANDARD_IA storage class one day after you
       create them.
    o Amazon S3 doesn't transition objects within the first 30 days because newer objects are


```
often accessed more frequently or deleted sooner than is suitable for STANDARD_IA or
ONEZONE_IA storage.
o If you are transitioning noncurrent objects (in versioned buckets), you can transition
only objects that are at least 30 days noncurrent to STANDARD_IA or ONEZONE_IA
storage.
```
- From the STANDARD_IA storage class to ONEZONE_IA. The following constraints apply:
    o Objects must be stored at least 30 days in the STANDARD_IA storage class before you
       can transition them to the ONEZONE_IA class.

**ENCRYPTION**

You can securely upload/download your data to Amazon S 3 via SSL endpoints using the HTTPS
protocol (In Transit – SSL/TLS).

**Encryption options:**

**Server side encryption options:**

- **SSE-S3 – Server Side Encryption with S3 managed keys**
    o Each object is encrypted with a unique key.
    o Encryption key is encrypted with a master key.
    o AWS regularly rotate the master key.
    o Uses AES 256.
- **SSE-KMS – Server Side Encryption with AWS KMS keys**
    o KMS uses Customer Master Keys (CMKs) to encrypt.
    o Can use the automatically created CMK key.
    o OR you can select your own key (gives you control for management of keys).
    o An envelope key protects your keys.
    o Chargeable.
- **SSE-C – Server Side Encryption with client provided keys**
    o Client manages the keys, S3 manages encryption.
    o AWS does not store the encryption keys.
    o If keys are lost data cannot be decrypted.

The following diagram depicts the options for enabling encryption and shows you where the
encryption is applied and where the keys are managed:


**EVENT NOTIFICATIONS**

Amazon S3 event notifications can be sent in response to actions in Amazon S3 like PUTs, POSTs,
COPYs, or DELETEs.

Amazon S3 event notifications enable you to run workflows, send alerts, or perform other actions in
response to changes in your objects stored in S3.

To enable notifications, you must first add a notification configuration that identifies the events you
want Amazon S3 to publish and the destinations where you want Amazon S3 to send the
notifications.

You can configure notifications to be filtered by the prefix and suffix of the key name of objects.

**Amazon S3 can publish notifications for the following events:**

- New object created events
- Object removal events
- Restore object events
- Reduced Redundancy Storage (RRS) object lost events
- Replication events

**Amazon S3 can send event notification messages to the following destinations:**

- Publish event messages to an Amazon Simple Notification Service (Amazon SNS) topic.
- Publish event messages to an Amazon Simple Queue Service (Amazon SQS) queue.
- Publish event messages to AWS Lambda by invoking a Lambda function and providing the
    event message as an argument.

Need to grant Amazon S3 permissions to post messages to an Amazon SNS topic or an Amazon SQS
queue.

Need to also grant Amazon S3 permission to invoke an AWS Lambda function on your behalf. For
information about granting these permissions.

**OBJECT TAGS**

S3 object tags are key-value pairs applied to S3 objects which can be created, updated or deleted at


any time during the lifetime of the object.

Allow you to create Identity and Access Management (IAM) policies, setup S3 Lifecycle policies, and
customize storage metrics.

Up to ten tags can be added to each S3 object and you can use either the AWS Management
Console, the REST API, the AWS CLI, or the AWS SDKs to add object tags.

**S3 CLOUDWATCH METRICS**

You can use the AWS Management Console to enable the generation of 1 - minute CloudWatch
request metrics for your S3 bucket or configure filters for the metrics using a prefix or object tag.

Alternatively, you can call the S3 PUT Bucket Metrics API to enable and configure publication of S3
storage metrics.

CloudWatch Request Metrics will be available in CloudWatch within 15 minutes after they are
enabled.

CloudWatch Storage Metrics are enabled by default for all buckets and reported once per day.

**The S3 metrics that can be monitored include:**

- S3 requests
- Bucket storage
- Bucket size
- All requests
- HTTP 4XX/5XX errors

**CROSS REGION REPLICATION**

CRR is an Amazon S3 feature that automatically replicates data across AWS Regions.

With CRR, every object uploaded to an S3 bucket is automatically replicated to a destination bucket
in a different AWS Region that you choose.

Provides automatic, asynchronous copying of objects between buckets in different regions.

CRR is configured at the S3 bucket level.

You enable a CRR configuration on your source bucket by specifying a destination bucket in a
different Region for replication.

You can use either the AWS Management Console, the REST API, the AWS CLI, or the AWS SDKs to
enable CRR.

Versioning must be enabled for both the source and destination buckets.

With CRR you can only replication between regions, not within a region (see SRR below for single
region replication).

Replication is 1:1 (one source bucket, to one destination bucket).

You can configure separate S3 Lifecycle rules on the source and destination buckets.

You can replicate KMS-encrypted objects by providing a destination KMS key in your replication
configuration.


You can set up CRR across AWS accounts to store your replicated data in a different account in the
target region.

Provides low latency access for data by copying objects to buckets that are closer to users.

**To activate CRR you need to configure the replication on the source bucket:**

- Define the bucket in the other region to replicate to.
- Specify to replicate all objects or a subset of objects with specific key name prefixes.

The replicas will be exact replicas and share the same key names and metadata.

You can specify a different storage class (by default the source storage class will be used).

AWS S3 will encrypt data in-transit with SSL.

AWS S3 must have permission to replicate objects.

Bucket owners must have permission to read the object and object ACL.

Can be used across accounts but the source bucket owner must have permission to replicate
objects into the destination bucket.

**Triggers for replication are:**

- Uploading objects to the source bucket.
- DELETE of objects in the source bucket.
- Changes to the object, its metadata, or ACL.

**What is replicated:**

- New objects created after enabling replication.
- Changes to objects.
- Objects created using SSE-S3 using the AWS managed key.
- Object ACL updates.

**What isn’t replicated:**

- Objects that existed before enabling replication (can use the copy API).
- Objects created with SSE-C and SSE-KMS.
- Objects to which the bucket owner does not have permissions.
- Updates to bucket-level subresources.
- Actions from lifecycle rules are not replicated.
- Objects in the source bucket that are replicated from another region are not replicated.

**Deletion behavior:**

- If a DELETE request is made without specifying an object version ID a delete marker will be
    added and replicated.
- If a DELETE request is made specifying an object version ID the object is deleted but the
    delete marker is not replicated.

**Charges:**

- Requests for upload
- Inter-region transfer


- S3 storage in both regions

**SAME REGION REPLICATION (SRR)**

As the name implies you can use SRR to replication objects to a destination bucket within the same
region as the source bucket.

This feature was released in September 2018.

Replication is automatic and asynchronous.

New objects uploaded to an Amazon S3 bucket are configured for replication at the bucket, prefix,
or object tag levels.

Replicated objects can be owned by the same AWS account as the original copy or by different
accounts, to protect from accidental deletion.

Replication can be to any Amazon S3 storage class, including S3 Glacier and S3 Glacier Deep Archive
to create backups and long-term archives.

When an S3 object is replicated using SRR, the metadata, Access Control Lists (ACL), and object tags
associated with the object are also part of the replication.

Once SRR is configured on a source bucket, any changes to the object, metadata, ACLs, or object
tags trigger a new replication to the destination bucket.

**S3 ANALYTICS**

Can run analytics on data stored on Amazon S3.

This includes data lakes, IoT streaming data, machine learning, and artificial intelligence.

The following strategies can be used:

### S3 performance guidelines

AWS provide some performance guidelines for Amazon S3. These are summarized here:

**Measure Performance -** When optimizing performance, look at network throughput, CPU, and
DRAM requirements. Depending on the mix of demands for these different resources, it might be
worth evaluating different Amazon EC2 instance types.

**Scale Storage Connections Horizontally -** You can achieve the best performance by issuing multiple
concurrent requests to Amazon S3. Spread these requests over separate connections to maximize
the accessible bandwidth from Amazon S3.


**Use Byte-Range Fetches** - Using the Range HTTP header in a GET Object request, you can fetch a
byte-range from an object, transferring only the specified portion. You can use concurrent
connections to Amazon S3 to fetch different byte ranges from within the same object. This helps
you achieve higher aggregate throughput versus a single whole-object request. Fetching smaller
ranges of a large object also allows your application to improve retry times when requests are
interrupted.

**Retry Requests for Latency-Sensitive Applications -** Aggressive timeouts and retries help drive
consistent latency. Given the large scale of Amazon S3, if the first request is slow, a retried request
is likely to take a different path and quickly succeed. The AWS SDKs have configurable timeout and
retry values that you can tune to the tolerances of your specific application.

**Combine Amazon S3 (Storage) and Amazon EC2 (Compute) in the Same AWS Region -** Although S3
bucket names are globally unique, each bucket is stored in a Region that you select when you
create the bucket. To optimize performance, we recommend that you access the bucket from
Amazon EC2 instances in the same AWS Region when possible. This helps reduce network latency
and data transfer costs.

**Use Amazon S3 Transfer Acceleration to Minimize Latency Caused by Distance -** Amazon S3
Transfer Acceleration manages fast, easy, and secure transfers of files over long geographic
distances between the client and an S3 bucket. Transfer Acceleration takes advantage of the
globally distributed edge locations in Amazon CloudFront. As the data arrives at an edge location, it
is routed to Amazon S3 over an optimized network path. Transfer Acceleration is ideal for
transferring gigabytes to terabytes of data regularly across continents. It's also useful for clients that
upload to a centralized bucket from all over the world.

### Glacier

Glacier is an archiving storage solution for infrequently accessed data.

**There are two storage tiers:**

**S3 Glacier:**

- Same low latency and high throughput performance of S3 Standard.
- Designed for durability of 99.999999999% of objects in a single Availability Zone†.
- Designed for 99.5% availability over a given year.
- Backed with the Amazon S3 Service Level Agreement for availability.
- Supports SSL for data in transit and encryption of data at rest.
- S3 Lifecycle management for automatic migration of objects to other S3 Storage Classes.

**S3 Glacier Deep Archive.**

- Designed for durability of 99.999999999% of objects across multiple Availability Zones.
- Data is resilient in the event of one entire Availability Zone destruction.
- Supports SSL for data in transit and encryption of data at rest.
- Low-cost design is ideal for long-term archive.
- Configurable retrieval times, from minutes to hours.
- S3 PUT API for direct uploads to S3 Glacier, and S3 Lifecycle management for automatic


```
migration of objects.
```
The key difference between the tiers is that Deep Archive is lower cost, but retrieval times are much
longer (12 hours).

The S3 Glacier tier has configurable retrieval times from minutes to hours (you pay accordingly).

Archived objects are not available for real time access and you need to submit a retrieval request.

Glacier must complete a job before you can get its output.

Requested archival data is copied to S3 One Zone-IA.

Following retrieval, you have 24 hours to download your data.

You cannot specify Glacier as the storage class at the time you create an object.

Glacier is designed to sustain the loss of two facilities.

Glacier automatically encrypts data at rest using AES 256 symmetric keys and supports secure
transfer of data over SSL.

Glacier may not be available in all AWS regions.

Glacier objects are visible through S3 only (not Glacier directly).

Glacier does not archive object metadata; you need to maintain a client-side database to maintain
this information.

Archives can be 1 bytes up to 40TB.

Glacier file archives of 1 byte – 4 GB can be performed in a single operation.

Glacier file archives from 100MB up to 40TB can be uploaded to Glacier using the multipart upload
API.

Uploading archives is synchronous.

Downloading archives is asynchronous.

The contents of an archive that has been uploaded cannot be modified.

You can upload data to Glacier using the CLI, SDKs or APIs – you cannot use the AWS Console.

Glacier adds 32 - 40KB (indexing and archive metadata) to each object when transitioning from other
classes using lifecycle policies.

AWS recommends that if you have lots of small objects they are combined in an archive (e.g. zip
file) before uploading.

A description can be added to archives, no other metadata can be added.

Glacier archive IDs are added upon upload and are unique for each upload.

**Archive retrieval:**

- Expedited is 1 - 5 minutes retrieval (most expensive).
- Standard is 3.5 hours retrieval (cheaper, 10GB data retrieval free per month).
- Bulk retrieval is 5 - 12 hours (cheapest, use for large quantities of data).


You can retrieve parts of an archive.

When data is retrieved it is copied to S3 and the archive remains in Glacier and the storage class
therefore does not change.

AWS SNS can send notifications when retrieval jobs are complete.

Retrieved data is available for 24 hours by default (can be changed).

To retrieve specific objects within an archive you can specify the byte range (Range) in the HTTP
GET request (need to maintain a DB of byte ranges).

**Glacier Charges:**

There is no charge for data transfer between EC2 and Glacier in the same region.

There is a charge if you delete data within 90 days.

**When you restore you pay for:**

- The Glacier archive.
- The requests.
- The restored data on S3.

### Amazon EFS

**GENERAL**

EFS is a fully-managed service that makes it easy to set up and scale file storage in the Amazon
Cloud.

Implementation of an NFS file share and is accessed using the NFSv4.1 protocol.

Elastic storage capacity and pay for what you use (in contrast to EBS with which you pay for what
you provision).

Multi-AZ metadata and data storage.

Can configure mount-points in one, or many, AZs.

Can be mounted from on-premises systems ONLY if using Direct Connect or a VPN connection.

Alternatively, use the EFS File Sync agent.

Good for big data and analytics, media processing workflows, content management, web serving,
home directories etc.

Pay for what you use (no pre-provisioning required).

Can scale up to petabytes.

EFS is elastic and grows and shrinks as you add and remove data.

Can concurrently connect 1 to 1000s of EC2 instances, from multiple AZs.

A file system can be accessed concurrently from all AZs in the region where it is located.

The following diagram depicts the various options for mounting an EFS filesystem:


By default, you can create up to 10 file systems per account.

Access to EFS file systems from on-premises servers can be enabled via Direct Connect or AWS VPN.

You mount an EFS file system on your on-premises Linux server using the standard Linux mount
command for mounting a file system via the NFSv4.1 protocol.

Can choose General Purpose or Max I/O (both SSD).

The VPC of the connecting instance must have DNS hostnames enabled.

EFS provides a file system interface, file system access semantics (such as strong consistency and
file locking).

Data is stored across multiple AZ’s within a region.

Read after write consistency.

Need to create mount targets and choose AZ’s to include (recommended to include all AZ’s).

Instances can be behind an ELB.

EC2 Classic instances must mount via ClassicLink.

EFS is compatible with all Linux-based AMIs for Amazon EC2.

Using the EFS-to-EFS Backup solution, you can schedule automatic incremental backups of your
Amazon EFS file system.

The following table provides a comparison of the **storage characteristics of EFS vs EBS** :


**PERFORMANCE**

**There are two performance modes:**

- “General Purpose” performance mode is appropriate for most file systems.
- “Max I/O” performance mode is optimized for applications where tens, hundreds, or
    thousands of EC2 instances are accessing the file system.

Amazon EFS is designed to burst to allow high throughput levels for periods of time.

Amazon EFS file systems are distributed across an unconstrained number of storage servers,
enabling file systems to grow elastically to petabyte scale and allowing massively parallel access
from Amazon EC2 instances to your data.

This distributed data storage design means that multithreaded applications and applications that
concurrently access data from multiple Amazon EC2 instances can drive substantial levels of
aggregate throughput and IOPS.

The table below compares high-level performance and storage characteristics for AWS’s file (EFS)
and block (EBS) cloud storage offerings:

**ACCESS CONTROL**

When you create a file system, you create endpoints in your VPC called “mount targets”.

When mounting from an EC2 instance, your file system’s DNS name, which you provide in your
mount command, resolves to a mount target’s IP address.

You can control who can administer your file system using IAM.

You can control access to files and directories with POSIX-compliant user and group-level
permissions.

POSIX permissions allow you to restrict access from hosts by user and group.


EFS Security Groups act as a firewall, and the rules you add define the traffic flow.

**EFS ENCRYPTION**

EFS offers the ability to encrypt data at rest and in transit.

Encryption keys are managed by the AWS Key Management Service (KMS).

Data encryption in transit uses industry standard Transport Layer Security (TLS) 1.2 to encrypt data
sent between your clients and EFS file systems.

Data encrypted at rest is transparently encrypted while being written, and transparently decrypted
while being read.

Enable encryption at rest in the EFS console or by using the AWS CLI or SDKs.

Encryption of data at rest and of data in transit can be configured together or separately to help
meet your unique security requirements.

**EFS FILE SYNC**

EFS File Sync provides a fast and simple way to securely sync existing file systems into Amazon EFS.

EFS File Sync copies files and directories into Amazon EFS at speeds up to 5x faster than standard
Linux copy tools, with simple setup and management in the AWS Console.

EFS File Sync securely and efficiently copies files over the internet or an AWS Direct Connect
connection.

Copies file data and file system metadata such as ownership, timestamps, and access permissions.

**EFS File Sync provides the following benefits:**

- Efficient high-performance parallel data transfer that tolerates unreliable and high-latency
    networks.
- Encryption of data transferred from your IT environment to AWS.
- Data transfer rate up to five times faster than standard Linux copy tools.
- Full and incremental syncs for repetitive transfers.

The following diagram shows a high-level view of the EFS File Sync architecture:

**Note:** EFS File Sync currently doesn’t support syncing from an Amazon EFS source to an NFS
destination.


When deploying Amazon EFS File Sync on EC2, the instance size must be at least xlarge for your EFS
File Sync to function.

Recommended to use one of the Memory optimized r4.xlarge instance types.

Can choose to run EFS File Sync either on-premises as a virtual machine (VM), or in AWS as an EC2
instance.

Supports VMware ESXi.

**COMPATIBILITY**

EFS is integrated with a number of other AWS services, including CloudWatch, CloudFormation,
CloudTrail, IAM, and Tagging services.

CloudWatch allows you to monitor file system activity using metrics.

CloudFormation allows you to create and manage file systems using templates.

CloudTrail allows you to record all Amazon EFS API calls in log files.

IAM allows you to control who can administer your file system.

Tagging services allows you to label your file systems with metadata that you define.

**PRICING AND BILLING**

You pay only for the amount of file system storage you use per month.

When using the Provisioned Throughput mode, you pay for the throughput you provision per
month.

There is no minimum fee and there are no set-up charges.

With EFS File Sync, you pay per-GB for data copied to EFS.

### AWS Storage Gateway

**GENERAL**

The AWS Storage Gateway service enables hybrid storage between on-premises environments and
the AWS Cloud.

It provides low-latency performance by caching frequently accessed data on premises, while storing
data securely and durably in Amazon cloud storage services.

Implemented using a virtual machine that you run on-premises (VMware or Hyper-V virtual
appliance).

Provides local storage resources backed by AWS S3 and Glacier.

Often used in disaster recovery preparedness to sync data to AWS.

Useful in cloud migrations.

AWS Storage Gateway supports three storage interfaces: file, volume, and tape.


The table below shows the different gateways available and the interfaces and use cases:

Each gateway you have can provide one type of interface.

All data transferred between any type of gateway appliance and AWS storage is encrypted using
SSL.

By default, all data stored by AWS Storage Gateway in S3 is encrypted server-side with Amazon S3-
Managed Encryption Keys (SSE-S3).

When using the file gateway, you can optionally configure each file share to have your objects
encrypted with AWS KMS-Managed Keys using SSE-KMS.

**FILE GATEWAY**

File gateway provides a virtual on-premises file server, which enables you to store and retrieve files
as objects in Amazon S3.

Can be used for on-premises applications, and for Amazon EC2-resident applications that need file
storage in S3 for object-based workloads.

Used for flat files only, stored directly on S3.

File gateway offers SMB or NFS-based access to data in Amazon S3 with local caching.

File gateway supports Amazon S3 Standard, S3 Standard – Infrequent Access (S3 Standard – IA) and
S3 One Zone – IA.

File gateway supports clients connecting to the gateway using NFS v3 and v4.1.

Microsoft Windows clients that support NFS v3 can connect to file gateway.

The maximum size of an individual file is 5 TB.

**VOLUME GATEWAY**

The volume gateway represents the family of gateways that support block-based volumes,
previously referred to as gateway-cached and gateway-stored modes.

Block storage – iSCSI based.


Cached Volume mode – the entire dataset is stored on S3 and a cache of the most frequently
accessed data is cached on-site.

Stored Volume mode – the entire dataset is stored on-site and is asynchronously backed up to S3
(EBS point-in-time snapshots). Snapshots are incremental and compressed.

Each volume gateway can support up to 32 volumes.

In cached mode, each volume can be up to 32 TB for a maximum of 1 PB of data per gateway (32
volumes, each 32 TB in size).

In stored mode, each volume can be up to 16 TB for a maximum of 512 TB of data per gateway (32
volumes, each 16 TB in size).

**GATEWAY VIRTUAL TAPE LIBRARY**

Used for backup with popular backup software.

Each gateway is preconfigured with a media changer and tape drives. Supported by NetBackup,
Backup Exec, Veeam etc.

When creating virtual tapes, you select one of the following sizes: 100 GB, 200 GB, 400 GB, 800 GB,
1.5 TB, and 2.5 TB.

A tape gateway can have up to 1,500 virtual tapes with a maximum aggregate capacity of 1 PB.

### Amazon fsx

Amazon FSx provides fully managed third-party file systems.

Amazon FSx provides you with the native compatibility of third-party file systems with feature sets
for workloads such as Windows-based storage, high-performance computing (HPC), machine
learning, and electronic design automation (EDA).

You don’t have to worry about managing file servers and storage, as Amazon FSx automates the
time-consuming administration tasks such as hardware provisioning, software configuration,
patching, and backups.

Amazon FSx integrates the file systems with cloud-native AWS services, making them even more
useful for a broader set of workloads.

**Amazon FSx provides you with two file systems to choose from:**

- Amazon FSx for Windows File Server for Windows-based applications
- Amazon FSx for Lustre for compute-intensive workloads.

**AMAZON FSX FOR WINDOWS FILE SERVER**

Amazon FSx for Windows File Server provides a fully managed native Microsoft Windows file
system so you can easily move your Windows-based applications that require shared file storage to
AWS.

Built on Windows Server, Amazon FSx provides the compatibility and features that your Microsoft
applications rely on, including full support for the SMB protocol, Windows NTFS, and Microsoft


Active Directory (AD) integration.

Amazon FSx uses SSD storage to provide fast performance with low latency.

This compatibility, performance, and scalability enables business-critical workloads such as home
directories, media workflows, and business applications.

Amazon FSx helps you optimize TCO with Data Deduplication, reducing costs by 50 - 60% for general-
purpose file shares.

User quotas give you the option to better monitor and control costs. You pay for only the resources
used, with no upfront costs, or licensing fees.

**Details and Benefits**

**High availability:** Amazon FSx automatically replicates your data within an Availability Zone (AZ) it
resides in (which you specify during creation) to protect it from component failure, continuously
monitors for hardware failures, and automatically replaces infrastructure components in the event
of a failure.

**Multi-AZ:** Amazon FSx offers a multiple availability (AZ) deployment option, designed to provide
continuous availability to data, even in the event that an AZ is unavailable. Multi-AZ file systems
include an active and standby file server in separate AZs, and any changes written to disk in your file
system are synchronously replicated across AZs to the standby.

**Supports Windows-native file system features:**

- Access Control Lists (ACLs), shadow copies, and user quotas.
- NTFS file systems that can be accessed from up to thousands of compute instances using
    the SMB protocol.

Works with Microsoft Active Directory (AD) to easily integrate file systems with Windows
environments.

Built on SSD-storage, Amazon FSx provides fast performance with up to 2 GB/second throughput
per file system, hundreds of thousands of IOPS, and consistent sub-millisecond latencies.

Can choose a throughput level that is independent of your file system size.

Using DFS Namespaces, you can scale performance up to tens of gigabytes per second of
throughput, with millions of IOPS, across hundreds of petabytes of data.

Amazon FSx can connect file systems to Amazon EC2, VMware Cloud on AWS, Amazon WorkSpaces,
and Amazon AppStream 2.0 instances.

Amazon FSx also supports on-premises access via AWS Direct Connect or AWS VPN, and access from
multiple VPCs, accounts, and regions using VPC Peering or AWS Transit Gateway.

Amazon FSx automatically encrypts your data at-rest and in-transit.

Assessed to comply with ISO, PCI-DSS, and SOC certifications, and is HIPAA eligible.

Integration with AWS CloudTrail monitors and logs your API calls letting you see actions taken by
users on Amazon FSx resources.


Pay only for the resources you use, with no minimum commitments or up-front fees.

Can optimize costs by removing redundant data with Data Deduplication.

User quotas provide tracking, monitoring, and enforcing of storage consumption to help reduce
costs.

**AMAZON FSX FOR LUSTRE**

Amazon FSx for Lustre provides a high-performance file system optimized for fast processing of
workloads such as machine learning, high performance computing (HPC), video processing, financial
modeling, and electronic design automation (EDA).

These workloads commonly require data to be presented via a fast and scalable file system
interface, and typically have data sets stored on long-term data stores like Amazon S3.

Amazon FSx for Lustre provides a fully managed high-performance Lustre file system that allows
file-based applications to access data with hundreds of gigabytes per second of data, millions of
IOPS, and sub millisecond latencies.

Amazon FSx works natively with Amazon S3, letting you transparently access your S3 objects as files
on Amazon FSx to run analyses for hours to months.

You can then write results back to S3, and simply delete your file system. FSx for Lustre also enables
you to burst your data processing workloads from on-premises to AWS, by allowing you to access
your FSx file system over Amazon Direct Connect or VPN.

You can also use FSx for Lustre as a standalone high-performance file system to burst your
workloads from on-premises to the cloud.

By copying on-premises data to an FSx for Lustre file system, you can make that data available for
fast processing by compute instances running on AWS.

With Amazon FSx, you pay for only the resources you use. There are no minimum commitments,
upfront hardware or software costs, or additional fees.

**Details and Benefits**

Lustre is a popular open-source parallel file system that is designed for high-performance
workloads. These workloads include HPC, machine learning, analytics, and media processing.

A parallel file system provides high throughput for processing large amounts of data and performs
operations with consistently low latencies.

It does so by storing data across multiple networked servers that thousands of compute instances
can interact with concurrently.

The Lustre file system provides a POSIX-compliant file system interface.

Amazon FSx can scale up to hundreds of gigabytes per second of throughput, and millions of IOPS.

Amazon FSx provides high throughput for processing large amounts of data and performs
operations with consistent, sub-millisecond latencies.

Amazon FSx for Lustre supports file access to thousands of EC2 instances, enabling you to provide


file storage for your high-performance workloads, like genomics, seismic exploration, and video
rendering.

**Amazon S3:**

- Amazon FSx works natively with Amazon S3, making it easy to access your S3 data to run
    data processing workloads.
- Your S3 objects are presented as files in your file system, and you can write your results
    back to S3.
- This lets you run data processing workloads on FSx for Lustre and store your long-term data
    on S3 or on-premises data stores.

**On-premises:**

- You can use Amazon FSx for Lustre for on-premises workloads that need to burst to the
    cloud due to peak demands or capacity limits.
- To move your existing on-premises data into Amazon FSx, you can mount your Amazon FSx
    for Lustre file system from an on-premises client over AWS Direct Connect or VPN, and then
    use parallel copy tools to import your data to your Amazon FSx for Lustre file system.
- At any time, you can write your results back to be durably stored in your data lake.

**Security:**

- All Amazon FSx file system data is encrypted at rest.
- You can access your file system from your compute instances using the open-source Lustre
    client.
- Once mounted, you can work with the files and directories in your file system just like you
    would with a local file system.
- FSx for Lustre is compatible with the most popular Linux-based AMIs, including Amazon
    Linux, Red Hat Enterprise Linux (RHEL), CentOS, Ubuntu, and SUSE Linux.
- You access your Amazon FSx file system from endpoints in your Amazon VPC, which enables
    you to isolate your file system in your own virtual network.
- You can configure security group rules and control network access to your Amazon FSx file
    systems.
- Amazon FSx is integrated with AWS Identity and Access Management (IAM).
- This integration means that you can control the actions your AWS IAM users and groups can
    take to manage your file systems (such as creating and deleting file systems).
- You can also tag your Amazon FSx resources and control the actions that your IAM users
    and groups can take based on those tags.


### Storage Quiz Questions

Answers and explanations are provided below after the last question in this section.

**Question 1: You would like to run some code when an object is uploaded to an Amazon S3
bucket. How can this be achieved?**

1. Create an event notification on the S3 bucket that triggers a Lambda function
2. Configure Lambda to poll the S3 bucket for changes and run a function when it finds new
    objects
3. Create an event notification on the S3 bucket that notifies Amazon SNS to trigger a Lambda
    function

**Question 2: Which type Amazon storage service uses standards-based REST web interfaces to
manage objects?**

1. Amazon Elastic File System (EFS)
2. Amazon Elastic Block Store (EBS)
3. Amazon Simple Storage Service (S3)
4. Amazon FSx for Windows File Server

**Question 3: What is the maximum file size allowed in Amazon S3?**

1. 5 terabytes
2. 0 bytes
3. 5 gigabytes
4. Unlimited

**Question 4: What type of consistency model is provided in Amazon S3 when you upload a new
version of an object?**

1. Read after write consistency
2. Eventual consistency

**Question 5: Which Amazon S3 capability uses Amazon CloudFront and enables fast uploads for
objects?**

1. Multipart upload
2. Cross region replication (CRR)
3. BitTorrent
4. Transfer acceleration

**Question 6: How can you create a hierarchy that mimics a filesystem in Amazon S3?**

1. Create buckets within other buckets
2. Use folders in your buckets
3. Upload objects within other objects
4. Use lifecycle rules to tier your data

**Question 7: A US based organization is concerned about uploading data to Amazon S3 as data
sovereignty rules mean they cannot move their data outside of the US. What would you tell
them?**


1. Data never leaves a region unless specifically configured to do so.
2. Data will be replicated globally so they cannot use Amazon S3.

**Question 8: For compliance reasons, an organization needs to retain data for 7 years. If they need
to retrieve data, they have 24 hours to do so. Which Amazon S3 storage class is most cost-
effective?**

1. Amazon S3 One-Zone IA
2. Amazon S3 Intelligent Tiering
3. Amazon S3 Glacier
4. Amazon S3 Glacier Deep Archive

**Question 9: An Architect is designing an application that will use hundreds of EC2 instances across
multiple availability zones. A shared filesystem is required that can be mounted by all instances.
Which storage service is suitable for this requirement?**

1. Amazon Elastic File System (EFS)
2. Amazon Elastic Block Store (EBS)
3. Amazon Instance Store
4. Amazon Simple Storage Service (S3)

**Question 10: How can you control access to files and directories in Amazon EFS filesystems?**

1. Using IAM
2. Using EFS security groups
3. Using Network ACLs
4. Using user and group-level permissions

**Question 11: A High-Performance Computing (HPC) application requires a high-performance
filesystem for running data analysis. The filesystem should transparently access source data
stored as Amazon S3 objects. Which type of filesystem is ideal for this use case?**

1. Amazon FSx for Windows File Server
2. Amazon Elastic File System (EFS)
3. Amazon FSx for Lustre
4. Amazon Elastic Block Store (EBS)

**Question 12: Which AWS storage service provides a NTFS filesystem that can be accessed by
multiple EC2 instances using the SMB protocol?**

1. Amazon FSx for Windows File Server
2. Amazon Elastic File System (EFS)
3. Amazon FSx for Lustre
4. Amazon Elastic Block Store (EBS)


**STORAGE - ANSWERS**

**Question 1, Answer: 1**

**Explanation:**

```
1 is correct. The best way to achieve this is to use an event notification on the S3 bucket that
triggers a function that then runs the code.
2 is incorrect. Lambda does not poll S3.
3 is incorrect. You would not use Amazon SNS in this scenario as it is an unnecessary additional
step.
```
**Question 2, Answer: 3**

**Explanation:**

```
1 is incorrect. EFS is a file-based storage system that is accessed using the NFS protocol.
2 is incorrect. EBS is a block-based storage system for mounting volumes.
3 is correct. Amazon S3 is an object-based storage system that uses standards-based REST web
interfaces to work with objects.
4 is incorrect. Amazon FSx for Windows File Server provides a fully managed Microsoft filesystem
that is mounted using SMB.
```
**Question 3, Answer: 1**

**Explanation:**

```
1 is correct. The maximum file size for Amazon S3 objects is 5 terabytes.
2 is incorrect. This is the minimum file size possible in Amazon S3.
3 is incorrect. 5GB is not the maximum file size possible in Amazon S3.
4 is incorrect. There is a limit on the maximum file size for objects in Amazon S3.
```
**Question 4, Answer: 2**

**Explanation:**

```
1 is incorrect. You do not get read after write consistency for overwrite PUT and DELETES.
2 is correct. In Amazon S3 you get eventual consistency for overwrite PUTS and DELETES.
```
**Question 5, Answer: 4**

**Explanation:**

```
1 is incorrect. Multipart upload is recommended for uploading objects larger than 100MB but it
does not use CloudFront.
2 is incorrect. CRR is used for replicating objects between buckets in different regions.
3 is incorrect. BitTorrent can be used for retrieving objects from Amazon S3. It is not used for
uploading and doesn’t use CloudFront.
4 is correct. Transfer Acceleration speeds up data uploads by using the CloudFront network.
```
**Question 6, Answer: 2**

**Explanation:**

```
1 is incorrect. You cannot nest buckets (create buckets inside other buckets).
2 is correct. You can mimic the hierarchy of a filesystem by creating folder in your buckets.
```

```
3 is incorrect. You cannot upload objects within other objects.
4 is incorrect. Tiering your data is done for performance not to mimic a filesystem.
```
**Question 7, Answer: 1**

**Explanation:**

```
1 is correct. S3 is a global service but buckets are created within a region. Data is never replicated
outside of that region unless you configure it (e.g. through CRR).
2 is incorrect. Data is not replicated globally with Amazon S3.
```
**Question 8, Answer: 4**

**Explanation:**

```
1 is incorrect. This is not the most cost-effective option for these requirements.
2 is incorrect. This is not the most cost-effective option for these requirements.
3 is incorrect. This is not the most cost-effective option for these requirements. It is slightly more
expensive than Deep Archive but faster to retrieve data (which isn’t necessary for this
scenario).
4 is correct. This is the most cost-effective option for these requirements as the data retrieval
time is 24 hours.
```
**Question 9, Answer: 1**

**Explanation:**

```
1 is correct. EFS is a file-based storage system accessed over NFS. You can attach thousands of
instances from multiple AZs to the same filesystem.
2 is incorrect. You cannot attach multiple instances to a single EBS volume or attach volumes
across AZs.
3 is incorrect. Instance Stores are local storage on the EC2 host servers, you cannot attach
multiple instances to the same instance store.
4 is incorrect. Amazon S3 is an object-based storage system, not a filesystem.
```
**Question 10, Answer: 4**

**Explanation:**

```
1 is incorrect. IAM can be used to control who can administer the file system but not control the
access to files and directories.
2 is incorrect. EFS security groups control network traffic that is allowed to reach the filesystem.
3 is incorrect. Network ACLs are not used for file and directory permissions, they restrict traffic
into and out of subnets.
4 is correct. You can control access to files and directories with POSIX-compliant user and group-
level permissions.
```
**Question 11, Answer: 3**

**Explanation:**

```
1 is incorrect. FSx for Windows File Server cannot access data stored on Amazon S3.
2 is incorrect. EFS does not integrate with Amazon S3 to transparently access objects.
3 is correct. This is a good use case for Amazon FSx for Lustre.
```

```
4 is incorrect. EBS is not a filesystem nor does it directly integrate with Amazon S3 for
transparent access of S3 objects.
```
**Question 12, Answer: 1**

**Explanation:**

```
1 is correct. FSx for Windows File Server provides NTFS file systems that can be accessed from up
to thousands of compute instances using the SMB protocol.
2 is incorrect. EFS is not an NTFS filesystem.
3 is incorrect. FSx for Lustre does not provide an NTFS filesystem.
4 is incorrect. EBS does not provide an NTFS filesystem nor can it be accessed by multiple EC2
instances.
```
