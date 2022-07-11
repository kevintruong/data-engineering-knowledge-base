**Explanation:**

The key requirements for the original images are that they are immediately available for 30 days (STANDARD), available

within 24 hours for 90 days (GLACIER) and then they are not needed (expire them).

The key requirements for the processed images are that they are immediately available for 30 days

(ONEZONE_IA as they can be recreated from the originals), and then are not needed (expire them).

- ✅ :  "Store the original images in STANDARD for 30 days, transition to GLACIER for 90 days, then expire the data"

  is a correct answer.

- ✅ :  "Store the processed images in ONEZONE_IA and then expire the data after 30 days" is also a correct answer.

- ❌ :  "Store the original images in STANDARD_IA for 30 days and then transition to DEEP_ARCHIVE" is incorrect.

  DEEP_ARCHIVE has a minimum storage duration of 180 days.

- ❌ :  "Store the processed images in STANDARD and then transition to GLACIER after 30 days" is incorrect. There is

  no need to transition the processed images to GLACIER as are not needed after 30 days as they can be recreated if

  needed from the originals.

- ❌ :  "Store the original images in STANDARD for 30 days, transition to DEEP_ARCHIVE for 90 days, then expire the

  data" is incorrect. DEEP_ARCHIVE has a minimum storage duration of 180 days.

**References:**

<https://docs.aws.amazon.com/AmazonS3/latest/dev/lifecycle-transition-general-considerations.html>

<https://aws.amazon.com/s3/storage-classes/>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/>

----

- #glacier #<https://docs.aws.amazon.com/amazons3/latest/dev/lifecycle-transition-general-considerations.html> #minimum_storage_duration #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/> #deep_archive
