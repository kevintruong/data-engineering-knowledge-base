**Explanation:**

The Architect requires a solution that removes the need to manage instances. Therefore it must be a serverless service

which rules out EC2. The two remaining options use AWS Lambda at the back-end for processing. Though CloudFront can

trigger Lambda functions it is more suited to customizing content delivered from an origin. Therefore, API Gateway with

AWS Lambda is the most workable solution presented.

This solution will likely require other services such as S3 for content and a database service. Refer to the link below

for an example scenario that uses API Gateway and AWS Lambda with other services to create a serverless web application.

- ✅ :  "Amazon API Gateway and AWS Lambda" is the correct answer.

- ❌ :  "Elastic Load Balancing with Auto Scaling groups and Amazon EC2" is incorrect as this option requires

  managing instances.

- ❌ :  "Amazon CloudFront and AWS Lambda" is incorrect as API Gateway is a better fit for the front end of this

  serverless web application.

- ❌ :  "Amazon API Gateway and Amazon EC2" is incorrect as this option requires managing instances.

**References:**

<https://aws.amazon.com/getting-started/projects/build-serverless-web-app-lambda-apigateway-s3>- dynamodb-cognito/

----

- #<https://aws.amazon.com/getting-started/projects/build-serverless-web-app-lambda-apigateway-s3>-_dynamodb> #aws_lambda #amazon_api_gateway #amazon_cloudfront #cloudfront
