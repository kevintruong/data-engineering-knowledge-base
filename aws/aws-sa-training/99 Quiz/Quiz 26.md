## Quiz 26: An application receives images uploaded by customers and stores them on Amazon S3. An AWS Lambda function then processes the images to add graphical elements. The processed images need to be available for users to download for 30 days, after which time they can be deleted. Processed images can be easily recreated from original images. The Original images need to be immediately available for 30 days and be accessible within 24 hours for another 90 days.**

**Which combination of Amazon S3 storage classes is most cost-effective for the original and processed images? (Select TWO)**

- [x] Store the original images in STANDARD for 30 days, transition to GLACIER for 90 days, then expire the data

- [ ] Store the original images in STANDARD_IA for 30 days and then transition to DEEP_ARCHIVE

- [x] Store the processed images in ONEZONE_IA and then expire the data after 30 days

- [ ] Store the processed images in STANDARD and then transition to GLACIER after 30 days

- [ ] Store the original images in STANDARD for 30 days, transition to DEEP_ARCHIVE for 90 days, then expire the data

----
Answer: 1,3

- [x] Store the original images in STANDARD for 30 days, transition to GLACIER for 90 days, then expire the data

- [x] Store the processed images in ONEZONE_IA and then expire the data after 30 days
  **Explanation:**
  The key requirements for the original images are that they are immediately available for 30 days (STANDARD), available within 24 hours for 90 days (GLACIER) and then they are not needed (expire them). The key requirements for the processed images are that they are immediately available for 30 days

(ONEZONE_IA as they can be recreated from the originals), and then are not needed (expire them).
![](aws-solution-architecture-practice-quiz-1641092865943.png)

- ✅: "Store the original images in STANDARD for 30 days, transition to GLACIER for 90 days, then expire the data" is a correct answer.

- ✅: "Store the processed images in ONEZONE_IA and then expire the data after 30 days" is also a correct answer.

- ❌: "Store the original images in STANDARD_IA for 30 days and then transition to DEEP_ARCHIVE" is incorrect. DEEP_ARCHIVE has a minimum storage duration of 180 days.

- ❌: "Store the processed images in STANDARD and then transition to GLACIER after 30 days" is incorrect. There is no need to transition the processed images to GLACIER as are not needed after 30 days as they can be recreated if needed from the originals.

- ❌: "Store the original images in STANDARD for 30 days, transition to DEEP_ARCHIVE for 90 days, then expire the data" is incorrect. DEEP_ARCHIVE has a minimum storage duration of 180 days.
  **References:**
  https://docs.aws.amazon.com/AmazonS3/latest/dev/lifecycle-transition-general-considerations.html
  https://aws.amazon.com/s3/storage-classes/



----
#quiz 
- relateTo:: [[Domain 1 Design Resilient Architectures]]