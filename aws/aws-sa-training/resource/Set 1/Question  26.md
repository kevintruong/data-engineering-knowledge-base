#### Question  26


**An application receives images uploaded by customers and stores them on Amazon S3. An AWS Lambda function then

processes the images to add graphical elements. The processed images need to be available for users to download for 30

days, after which time they can be deleted. Processed images can be easily recreated from original images. The Original

images need to be immediately available for 30 days and be accessible within 24 hours for another 90 days.**


**Which combination of Amazon S3 storage classes is most cost-effective for the original and processed images? (Select

TWO)**


- [x] Store the original images in STANDARD for 30 days, transition to GLACIER for 90 days, then expire the data


- [ ] Store the original images in STANDARD_IA for 30 days and then transition to DEEP_ARCHIVE


- [x] Store the processed images in ONEZONE_IA and then expire the data after 30 days


- [ ] Store the processed images in STANDARD and then transition to GLACIER after 30 days


- [ ] Store the original images in STANDARD for 30 days, transition to DEEP_ARCHIVE for 90 days, then expire the data



- hasExplain:: [[explanation_Question  26.md]]

#storage #s3 #aws #deep_archive #glacier 