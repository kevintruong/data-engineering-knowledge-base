#### Question  26


**An application receives images uploaded by customers and stores them on Amazon S3. An AWS Lambda function then

processes the images to add graphical elements. The processed images need to be available for users to download for 30

days, after which time they can be deleted. Processed images can be easily recreated from original images. The Original

images need to be immediately available for 30 days and be accessible within 24 hours for another 90 days.**


**Which combination of Amazon S3 storage classes is most cost-effective for the original and processed images? (Select

TWO)**


1: Store the original images in STANDARD for 30 days, transition to GLACIER for 90 days, then expire the data


2: Store the original images in STANDARD_IA for 30 days and then transition to DEEP_ARCHIVE


3: Store the processed images in ONEZONE_IA and then expire the data after 30 days


4: Store the processed images in STANDARD and then transition to GLACIER after 30 days


5: Store the original images in STANDARD for 30 days, transition to DEEP_ARCHIVE for 90 days, then expire the data


Answer: 1,3


**Explanation:**


The key requirements for the original images are that they are immediately available for 30 days (STANDARD), available

within 24 hours for 90 days (GLACIER) and then they are not needed (expire them).


The key requirements for the processed images are that they are immediately available for 30 days

(ONEZONE_IA as they can be recreated from the originals), and then are not needed (expire them).


- CORRECT "Store the original images in STANDARD for 30 days, transition to GLACIER for 90 days, then expire the data"

  is a correct answer.


- CORRECT "Store the processed images in ONEZONE_IA and then expire the data after 30 days" is also a correct answer.


- INCORRECT "Store the original images in STANDARD_IA for 30 days and then transition to DEEP_ARCHIVE" is incorrect.

  DEEP_ARCHIVE has a minimum storage duration of 180 days.


- INCORRECT "Store the processed images in STANDARD and then transition to GLACIER after 30 days" is incorrect. There is

  no need to transition the processed images to GLACIER as are not needed after 30 days as they can be recreated if

  needed from the originals.


- INCORRECT "Store the original images in STANDARD for 30 days, transition to DEEP_ARCHIVE for 90 days, then expire the

  data" is incorrect. DEEP_ARCHIVE has a minimum storage duration of 180 days.


**References:**


https://docs.aws.amazon.com/AmazonS3/latest/dev/lifecycle-transition-general-considerations.html


https://aws.amazon.com/s3/storage-classes/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/

