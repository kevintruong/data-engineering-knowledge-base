#### Question  39


**A Solutions Architect is designing a mobile application that will capture receipt images to track expenses. The

Architect wants to store the images on Amazon S3. However, uploading the images through the web server will create too

much traffic.**


**What is the MOST efficient method to store images from a mobile application on Amazon S3?**


- [ ] Expand the web server fleet with Spot instances to provide the resources to handle the images


- [ ] Upload to a second bucket, and have a Lambda event copy the image to the primary bucket


- [ ] Upload to a separate Auto Scaling Group of server behind an ELB Classic Load Balancer, and have the server instances

write to the Amazon S3 bucket


- [x] Upload directly to S3 using a pre-signed URL



- hasExplain:: [[explanation_Question  39.md]]