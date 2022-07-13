*

**Explanation:**

Multipart upload can be used to speed up uploads to S3. Multipart upload uploads objects in parts independently, in

parallel and in any order. It is performed using the S3 Multipart upload API and is recommended for objects of 100MB or

larger. It can be used for objects from 5MB up to 5TB and must be used for objects larger than 5GB.

* ✅ :  "Use Amazon S3 multipart upload" is the correct answer.

* ❌ :  "Turn off versioning on the destination bucket" is incorrect. Turning off versioning will not speed up the

  upload.

* ❌ :  "Randomize the object names when uploading" is incorrect. Randomizing object names provides no value in this

  context, random prefixes are used for intensive read requests.

* ❌ :  "Upload the files using the S3 Copy SDK or REST API" is incorrect. Copy is used for copying, moving and

  renaming objects within S3 not for uploading to S3.

**References:**

<https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/>

----
* #amazon_s3_multipart_upload #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/> #s3_multipart #s3_copy_sdk #s3
