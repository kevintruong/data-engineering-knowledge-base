#### Question  19


**A government agency is using CloudFront for a web application that receives personally identifiable information (PII)

from citizens. What feature of CloudFront applies an extra level of encryption at CloudFront edge locations to ensure

the PII data is secured end-to-end?**


1: Object invalidation


2: Field-level encryption


3: RTMP distribution


4: Origin access identity


**Answer: 2**


**Explanation:**


With Amazon CloudFront, you can enforce secure end-to-end connections to origin servers by using HTTPS. Field-level

encryption adds an additional layer of security that lets you protect specific data throughout system processing so that

only certain applications can see it.


Field-level encryption allows you to enable your users to securely upload sensitive information to your web servers. The

sensitive information provided by your users is encrypted at the edge, close to the user, and remains encrypted

throughout your entire application stack. This encryption ensures that only applications that need the data—and have the

credentials to decrypt it—are able to do so.


- CORRECT "Field-level encryption" is the correct answer.


- INCORRECT "Object invalidation" is incorrect. Object invalidation is a method to remove objects from the cache.


- INCORRECT "RTMP distribution" is incorrect. An RTMP distribution is a method of streaming media using Adobe Flash.


- INCORRECT "Origin access identity" is incorrect. Origin access identity applies to S3 bucket origins, not web servers.


**References:**


https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/field-level-encryption.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-

delivery/amazon-cloudfront/

