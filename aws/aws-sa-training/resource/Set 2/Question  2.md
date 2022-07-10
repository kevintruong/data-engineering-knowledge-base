#### Question  2


**A company requires a solution to allow customers to customize images that are stored in an online catalog. The image

customization parameters will be sent in requests to Amazon API Gateway. The customized image will then be generated

on-demand and can be accessed online.**


**The solutions architect requires a highly available solution. Which solution will be MOST cost-effective?**


- [ ] Use Amazon EC2 instances to manipulate the original images into the requested customization. Store the original and

manipulated images in Amazon S3. Configure an Elastic Load Balancer in front of the EC2 instances


- [x] Use AWS Lambda to manipulate the original images to the requested customization. Store the original and manipulated

images in Amazon S3. Configure an Amazon CloudFront distribution with the S3 bucket as the origin


- [ ] Use AWS Lambda to manipulate the original images to the requested customization. Store the original images in Amazon

S3 and the manipulated images in Amazon DynamoDB. Configure an Elastic Load Balancer in front of the Amazon EC2

instances


- [ ] Use Amazon EC2 instances to manipulate the original images into the requested customization. Store the original

images in Amazon S3 and the manipulated images in Amazon DynamoDB. Configure an Amazon CloudFront distribution with the

S3 bucket as the origin



- hasExplain:: [[explanation_Question  2.md]]

#amazon_cloudfront_distribution #use_aws_lambda #amazon_dynamodb #amazon_s3 #customized_image 