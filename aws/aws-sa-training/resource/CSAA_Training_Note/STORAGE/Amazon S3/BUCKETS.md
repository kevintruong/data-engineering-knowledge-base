#### BUCKETS

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

URL is in this format: https://s3- **_eu-west- 1_**
.amazonaws.com/ **_<bucketname>._**

Can backup a bucket to another bucket in another account.

Can enable logging to a bucket.

**Bucket naming:**

- Bucket names must be at least 3 and no more than 63 character in length.

- Bucket names must start and end with a lowercase character or a number.

- Bucket names must be a series of one or more labels which are separated by a
  period.

- Bucket names can contain lowercase letters, numbers and hyphens.

- Bucket names cannot be formatted as an IP address.

For better performance, lower latency, and lower cost, create the bucket closer
to your clients.

