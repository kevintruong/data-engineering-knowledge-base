#### GENERAL


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

