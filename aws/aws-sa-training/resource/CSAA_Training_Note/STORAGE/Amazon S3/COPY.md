#### COPY

You can create a copy of objects up to 5GB in size in a single atomic operation.

For files larger than 5GB you must use the multipart upload API.

Can be performed using the AWS SDKs or REST API.

**The copy operation can be used to:**

- Generate additional copies of objects.

- Renaming objects.

- Changing the copy’s storage class or encryption at rest status.

- Move objects across AWS locations/regions.

- Change object metadata.

Once uploaded to S3 some object metadata cannot be changed, copying the object
can allow you to modify this information.

