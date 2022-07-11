### Amazon S3


**GENERAL**


Amazon S3 is object storage built to store and retrieve any amount of data from anywhere on the Internet.


It’s a simple storage service that offers an extremely durable, highly available, and infinitely scalable data storage

infrastructure at very low costs.


Amazon S3 is a distributed architecture and objects are redundantly stored on multiple devices across multiple

facilities (AZs) in an Amazon S3 region.


Amazon S3 is a simple key-based object store.


Keys can be any string, and they can be constructed to mimic hierarchical attributes.


Alternatively, you can use S3 Object Tagging to organize your data across all of your S3 buckets and/or prefixes.


Amazon S3 provides a simple, standards-based REST web services interface that is designed to work with any

Internet-development toolkit.


Files can be from 0 bytes to 5TB.


The largest object that can be uploaded in a single PUT is 5 gigabytes.


For objects larger than 100 megabytes use the Multipart Upload capability.


Updates to an object are atomic – when reading an updated object, you will either get the new object or the old one, you

will never get partial or corrupt data.


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


For example, your application can achieve at least 3,500 PUT/POST/DELETE and 5,500 GET requests per second per prefix in

a bucket.


There are no limits to the number of prefixes in a bucket. It is simple to increase your read or write performance

exponentially.


For read intensive requests you can also use CloudFront edge locations to offload from S3.


**ADDITIONAL CAPABILITIES**


Additional capabilities offered by Amazon S3 include:


**USE CASES**


**Typical use cases include:**


- Backup and Storage – Provide data backup and storage services for others.

- Application Hosting – Provide services that deploy, install, and manage web applications.

- Media Hosting – Build a redundant, scalable, and highly available infrastructure that hosts video, photo, or music

  uploads and downloads.


- Software Delivery – Host your software applications that customers can download.

- Static Website – you can configure a static website to run from an S3 bucket.


S3 is a persistent, highly durable data store.


Persistent data stores are non-volatile storage systems that retain data when powered off.


This is in contrast to transient data stores and ephemeral data stores which lose the data when powered off.


The following table provides a description of persistent, transient and ephemeral data stores and which AWS service to

use:


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


URL is in this format: <https://s3>- **_eu-west- 1_** .amazonaws.com/ **_<bucketname>._**


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


Objects stored in a bucket will never leave the region in which they are stored unless you move them to another region

or enable cross-region replication.


You can define permissions on objects when uploading and at any time afterwards using the AWS Management Console.


**SUB-RESOURCES**


- Sub-resources are subordinate to objects, they do not exist independently but are always associated with another

  entity such as an object or bucket.

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


Objects stored in the S3 One Zone-IA storage class are stored redundantly within a single Availability Zone in the AWS

Region you select.


**ACCESS AND ACCESS POLICIES**


**There are four mechanisms for controlling access to Amazon S3 resources:**


- IAM policies.

- Bucket policies.

- Access Control Lists (ACLs).

- Query string authentication (URL to an Amazon S3 object which is only valid for a limited time).


Access auditing can be configured by configuring an Amazon S3 bucket to create access log records for all requests made

against it.


For capturing IAM/user identity information in logs configure AWS CloudTrail Data Events.


By default, a bucket, its objects, and related sub-resources are all private.


By default, only a resource owner can access a bucket.


The resource owner refers to the AWS account that creates the resource.


With IAM the account owner rather than the IAM user is the owner.


Within an IAM policy you can grant either programmatic access or AWS Management Console access to Amazon S3 resources.


Amazon Resource Names (ARN) are used for specifying resources in a policy.


**The format for any resource on AWS is:**


arn:partition:service:region:namespace:relative-id.


**For S3 resources:**


- aws is a common partition name.

- s3 is the service.

- You don’t specify Region and namespace.

- For Amazon S3, it can be a bucket-name or a bucket-name/object-key. You can use wild card


**The format for S3 resources is:**


arn:aws:s3:::bucket_name.


arn:aws:s3:::bucket_name/key_name.


A bucket owner can grant cross-account permissions to another AWS account (or users in an account) to upload objects.


The AWS account that uploads the objects owns them.


The bucket owner does not have permissions on objects that other accounts own, however:


- The bucket owner pays the charges.

- The bucket owner can deny access to any objects regardless of ownership.

- The bucket owner can archive any objects or restore archived objects regardless of ownership.


**Access to buckets and objects can be granted to:**


- Individual users.

- AWS accounts.

- Everyone (public/anonymous).

- All authenticated users (AWS users).


Access policies define access to resources and can be associated with resources (buckets and objects) and users.


You can use the AWS Policy Generator to create a bucket policy for your Amazon S3 bucket.


The categories of policy are resource-based policies and user policies.


**Resource-based policies:**


- Attached to buckets and objects.

- ACL-based policies define permissions.

- ACLs can be used to grant read/write permissions to other accounts.

- Bucket policies can be used to grant other AWS accounts or IAM users permission to the bucket and objects.


**User policies:**


- Can use IAM to manage access to S3 resources.

- Using IAM you can create users, groups and roles and attach access policies to them granting them access to resources.

- You cannot grant anonymous permissions in an IAM user policy as the policy is attached to a user.

- User policies can grant permissions to a bucket and the objects in it.


**ACLs:**


- S3 ACLs enable you to manage access to buckets and objects.

- Each bucket and object has an ACL attached to it as a subresource.

- Bucket and object permissions are independent of each other.

- The ACL defines which AWS accounts (grantees) or pre-defined S3 groups are granted access and the type of access.

- A grantee can be an AWS account or one of the predefined Amazon S3 groups.

- When you create a bucket or an object, S3 creates a default ACL that grants the resource owner full control over the

  resource.


**Cross account access:**


- You grant permission to another AWS account using the email address or the canonical user ID.

- However, if you provide an email address in your grant request, Amazon S3 finds the canonical user ID for that account

  and adds it to the ACL.

- Grantee accounts can then then delegate the access provided by other accounts to their individual users.


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

- AWS recommends that you never grant the All Users group WRITE, WRITE_ACP, or FULL_CONTROL permissions.


**Log Delivery group:**


- Providing WRITE permission to this group on a bucket enables S3 to write server access logs.

- Not applicable to objects.


**The following table lists the set of permissions that Amazon S3 supports in an ACL:**


- The set of ACL permissions is the same for an object ACL and a bucket ACL.


- Depending on the context (bucket ACL or object ACL), these ACL permissions grant permissions for specific buckets or

  object operations.

- The table lists the permissions and describes what they mean in the context of objects and buckets.


**Note the following:**


- Permissions are assigned at the account level for authenticated users.

- You cannot assign permissions to individual IAM users.

- When Read is granted on a bucket it only provides the ability to list the objects in the bucket.

- When Read is granted on an object the data can be read.

- ACP means access control permissions and READ_ACP/WRITE_ACP control who can read/write the ACLs themselves.

- WRITE is only applicable to the bucket level (except for ACP).


Bucket policies are limited to 20 KB in size.


Object ACLs are limited to 100 granted permissions per ACL.


The only recommended use case for the bucket ACL is to grant write permissions to the S3 Log Delivery group.


**There are limits to managing permissions using ACLs:**


- You cannot grant permissions to individual users.

- You cannot grant conditional permissions.

- You cannot explicitly deny access.


When granting other AWS accounts the permissions to upload objects, permissions to these objects can only be managed by

the object owner using object ACLs.


**You can use bucket policies for:**


- Granting users permissions to a bucket owned by your account.

- Managing object permissions (where the object owner is the same account as the bucket owner).

- Managing cross-account permissions for all Amazon S3 permissions.


**You can use user policies for:**


- Granting permissions for all Amazon S3 operations.

- Managing permissions for users in your account.

- Granting object permissions to users within the account.


**For an IAM user to access resources in another account the following must be provided:**


- Permission from the parent account through a user policy.

- Permission from the resource owner to the IAM user through a bucket policy, or the parent account through a bucket

  policy, bucket ACL or object ACL.


If an AWS account owns a resource it can grant permissions to another account, that account can then delegate those

permissions or a subset of them to uses in the account (permissions delegation).


An account that receives permissions from another account cannot delegate permissions cross- account to a third AWS

account.


**CHARGES**


No charge for data transferred between EC2 and S3 in the same region.


Data transfer into S3 is free of charge.


Data transferred to other regions is charged.


Data Retrieval (applies to S3 Standard-IA and S3 One Zone-IA, S3 Glacier and S3 Glacier Deep Archive).


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


Once uploaded to S3 some object metadata cannot be changed, copying the object can allow you to modify this information.


**TRANSFER ACCELERATION**


Amazon S3 Transfer Acceleration enables fast, easy, and secure transfers of files over long distances between your

client and your Amazon S3 bucket.


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


Pre-signed URLs can be used to provide temporary access to a specific object to those who do not have AWS credentials.


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


Deletion with versioning replicates the delete marker. But deleting the delete marker is not replicated.


**Bucket versioning states:**


- Enabled

- Versioned

- Un-versioned


Objects that existed before enabling versioning will have a version ID of NULL.


**Suspension:**


- If you suspend versioning the existing objects remain as they are however new versions will not be created.

- While versioning is suspended new objects will have a version ID of NULL and uploaded objects of the same name will

  overwrite the existing object.


**LIFECYCLE MANAGEMENT**


Used to optimize storage costs, adhere to data retention policies and to keep S3 volumes well- maintained.


A _lifecycle configuration_ is a set of rules that define actions that Amazon S3 applies to a group of objects. There

are two types of actions:


- **Transition actions** —Define when objects transition to another storage class. For example, you might choose to

  transition objects to the STANDARD_IA storage class 30 days after you created them, or archive objects to the GLACIER

  storage class one year after creating them.


There are costs associated with the lifecycle transition requests. For pricing information, see Amazon S3 Pricing.


- **Expiration actions** —Define when objects expire. Amazon S3 deletes expired objects on your behalf.


Lifecycle configuration is an XML file applied at the bucket level as a subresource.


Can be used in conjunction with versioning or independently.


Can be applied to current and previous versions.


Can be applied to specific objects within a bucket: objects with a specific tag or objects with a specific prefix.


**Supported Transitions and Related Constraints**


**Amazon S3 supports the following lifecycle transitions between storage classes using a lifecycle configuration:**


- You can transition from the STANDARD storage class to any other storage class.

- You can transition from any storage class to the GLACIER or DEEP_ARCHIVE storage classes.

- You can transition from the STANDARD_IA storage class to the INTELLIGENT_TIERING or ONEZONE_IA storage classes.

- You can transition from the INTELLIGENT_TIERING storage class to the ONEZONE_IA storage class.

- You can transition from the GLACIER storage class to the DEEP_ARCHIVE storage class.


**The following lifecycle transitions are not supported:**


- You can't transition from any storage class to the STANDARD storage class.

- You can't transition from any storage class to the REDUCED_REDUNDANCY storage class.

- You can't transition from the INTELLIGENT_TIERING storage class to the STANDARD_IA storage class.

- You can't transition from the ONEZONE_IA storage class to the STANDARD_IA or INTELLIGENT_TIERING storage classes.

- You can transition from the GLACIER storage class to the DEEP_ARCHIVE storage class only.

- You can't transition from the DEEP_ARCHIVE storage class to any other storage class.


**The lifecycle storage class transitions have the following constraints:**


- From the STANDARD or STANDARD_IA storage class to INTELLIGENT_TIERING. The following constraints apply:

  o For larger objects, there is a cost benefit for transitioning to INTELLIGENT_TIERING. Amazon S3 does not transition

  objects that are smaller than 128 KB to the INTELLIGENT_TIERING storage class because it's not cost effective.

- From the STANDARD storage classes to STANDARD_IA or ONEZONE_IA. The following constraints apply:

  o For larger objects, there is a cost benefit for transitioning to STANDARD_IA or ONEZONE_IA. Amazon S3 does not

  transition objects that are smaller than 128 KB to the STANDARD_IA or ONEZONE_IA storage classes because it's not cost

  effective. o Objects must be stored at least 30 days in the current storage class before you can transition them to

  STANDARD_IA or ONEZONE_IA. For example, you cannot create a lifecycle rule to transition objects to the STANDARD_IA

  storage class one day after you create them. o Amazon S3 doesn't transition objects within the first 30 days because

  newer objects are


```

often accessed more frequently or deleted sooner than is suitable for STANDARD_IA or

ONEZONE_IA storage.

o If you are transitioning noncurrent objects (in versioned buckets), you can transition

only objects that are at least 30 days noncurrent to STANDARD_IA or ONEZONE_IA

storage.

```


- From the STANDARD_IA storage class to ONEZONE_IA. The following constraints apply:

  o Objects must be stored at least 30 days in the STANDARD_IA storage class before you can transition them to the

  ONEZONE_IA class.


**ENCRYPTION**


You can securely upload/download your data to Amazon S 3 via SSL endpoints using the HTTPS protocol (In Transit –

SSL/TLS).


**Encryption options:**


**Server side encryption options:**


- **SSE-S3 – Server Side Encryption with S3 managed keys**

  o Each object is encrypted with a unique key. o Encryption key is encrypted with a master key. o AWS regularly rotate

  the master key. o Uses AES 256.

- **SSE-KMS – Server Side Encryption with AWS KMS keys**

  o KMS uses Customer Master Keys (CMKs) to encrypt. o Can use the automatically created CMK key. o OR you can select

  your own key (gives you control for management of keys). o An envelope key protects your keys. o Chargeable.

- **SSE-C – Server Side Encryption with client provided keys**

  o Client manages the keys, S3 manages encryption. o AWS does not store the encryption keys. o If keys are lost data

  cannot be decrypted.


The following diagram depicts the options for enabling encryption and shows you where the encryption is applied and

where the keys are managed:


**EVENT NOTIFICATIONS**


Amazon S3 event notifications can be sent in response to actions in Amazon S3 like PUTs, POSTs, COPYs, or DELETEs.


Amazon S3 event notifications enable you to run workflows, send alerts, or perform other actions in response to changes

in your objects stored in S3.


To enable notifications, you must first add a notification configuration that identifies the events you want Amazon S3

to publish and the destinations where you want Amazon S3 to send the notifications.


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

- Publish event messages to AWS Lambda by invoking a Lambda function and providing the event message as an argument.


Need to grant Amazon S3 permissions to post messages to an Amazon SNS topic or an Amazon SQS queue.


Need to also grant Amazon S3 permission to invoke an AWS Lambda function on your behalf. For information about granting

these permissions.


**OBJECT TAGS**


S3 object tags are key-value pairs applied to S3 objects which can be created, updated or deleted at


any time during the lifetime of the object.


Allow you to create Identity and Access Management (IAM) policies, setup S3 Lifecycle policies, and customize storage

metrics.


Up to ten tags can be added to each S3 object and you can use either the AWS Management Console, the REST API, the AWS

CLI, or the AWS SDKs to add object tags.


**S3 CLOUDWATCH METRICS**


You can use the AWS Management Console to enable the generation of 1 - minute CloudWatch request metrics for your S3

bucket or configure filters for the metrics using a prefix or object tag.


Alternatively, you can call the S3 PUT Bucket Metrics API to enable and configure publication of S3 storage metrics.


CloudWatch Request Metrics will be available in CloudWatch within 15 minutes after they are enabled.


CloudWatch Storage Metrics are enabled by default for all buckets and reported once per day.


**The S3 metrics that can be monitored include:**


- S3 requests

- Bucket storage

- Bucket size

- All requests

- HTTP 4XX/5XX errors


**CROSS REGION REPLICATION**


CRR is an Amazon S3 feature that automatically replicates data across AWS Regions.


With CRR, every object uploaded to an S3 bucket is automatically replicated to a destination bucket in a different AWS

Region that you choose.


Provides automatic, asynchronous copying of objects between buckets in different regions.


CRR is configured at the S3 bucket level.


You enable a CRR configuration on your source bucket by specifying a destination bucket in a different Region for

replication.


You can use either the AWS Management Console, the REST API, the AWS CLI, or the AWS SDKs to enable CRR.


Versioning must be enabled for both the source and destination buckets.


With CRR you can only replication between regions, not within a region (see SRR below for single region replication).


Replication is 1:1 (one source bucket, to one destination bucket).


You can configure separate S3 Lifecycle rules on the source and destination buckets.


You can replicate KMS-encrypted objects by providing a destination KMS key in your replication configuration.


You can set up CRR across AWS accounts to store your replicated data in a different account in the target region.


Provides low latency access for data by copying objects to buckets that are closer to users.


**To activate CRR you need to configure the replication on the source bucket:**


- Define the bucket in the other region to replicate to.

- Specify to replicate all objects or a subset of objects with specific key name prefixes.


The replicas will be exact replicas and share the same key names and metadata.


You can specify a different storage class (by default the source storage class will be used).


AWS S3 will encrypt data in-transit with SSL.


AWS S3 must have permission to replicate objects.


Bucket owners must have permission to read the object and object ACL.


Can be used across accounts but the source bucket owner must have permission to replicate objects into the destination

bucket.


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


- If a DELETE request is made without specifying an object version ID a delete marker will be added and replicated.

- If a DELETE request is made specifying an object version ID the object is deleted but the delete marker is not

  replicated.


**Charges:**


- Requests for upload

- Inter-region transfer


- S3 storage in both regions


**SAME REGION REPLICATION (SRR)**


As the name implies you can use SRR to replication objects to a destination bucket within the same region as the source

bucket.


This feature was released in September 2018.


Replication is automatic and asynchronous.


New objects uploaded to an Amazon S3 bucket are configured for replication at the bucket, prefix, or object tag levels.


Replicated objects can be owned by the same AWS account as the original copy or by different accounts, to protect from

accidental deletion.


Replication can be to any Amazon S3 storage class, including S3 Glacier and S3 Glacier Deep Archive to create backups

and long-term archives.


When an S3 object is replicated using SRR, the metadata, Access Control Lists (ACL), and object tags associated with the

object are also part of the replication.


Once SRR is configured on a source bucket, any changes to the object, metadata, ACLs, or object tags trigger a new

replication to the destination bucket.


**S3 ANALYTICS**


Can run analytics on data stored on Amazon S3.


This includes data lakes, IoT streaming data, machine learning, and artificial intelligence.


The following strategies can be used:

