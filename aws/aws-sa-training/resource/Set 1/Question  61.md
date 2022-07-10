#### Question  61


**Your company shares some HR videos stored in an Amazon S3 bucket via CloudFront. You need to restrict access to the

private content so users coming from specific IP addresses can access the videos and ensure direct access via the Amazon

S3 bucket is not possible.**


**How can this be achieved?**


- [ ] Configure CloudFront to require users to access the files using signed cookies, create an origin access identity (

OAI) and instruct users to login with the OAI


- [x] Configure CloudFront to require users to access the files using a signed URL, create an origin access identity

(OAI) and restrict access to the files in the Amazon S3 bucket to the OAI


- [ ] Configure CloudFront to require users to access the files using signed cookies, and move the files to an encrypted

EBS volume


- [ ] Configure CloudFront to require users to access the files using a signed URL, and configure the S3 bucket as a

website endpoint



- hasExplain:: [[explanation_Question  61.md]]

#cloudfront #s3 #amazon #access #videos 