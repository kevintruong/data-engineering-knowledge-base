#### BUILDING LAMBDA APPS

You can deploy and manage your serverless applications using the AWS Serverless
Application Model (AWS SAM).

AWS SAM is a specification that prescribes the rules for expressing serverless
applications on AWS.

This specification aligns with the syntax used by AWS CloudFormation today and
is supported natively within AWS

CloudFormation as a set of resource types (referred to as “serverless
resources”).

You can automate your serverless application’s release process using AWS
CodePipeline and AWS CodeDeploy.

You can enable your Lambda function for tracing with AWS X-Ray.

**LAMBDA@EDGE**

Lambda@Edge allows you to run code across AWS locations globally without
provisioning or managing servers, responding to

end users at the lowest network latency.

Lambda@Edge lets you run Node.js and Python Lambda functions to customize
content that CloudFront delivers, executing

the functions in AWS locations closer to the viewer.

The functions run in response to CloudFront events, without provisioning or
managing servers.

**You can use Lambda functions to change CloudFront requests and responses at
the following points:**

- After CloudFront receives a request from a viewer (viewer request).

- Before CloudFront forwards the request to the origin (origin request).

- After CloudFront receives the response from the origin (origin response).

- Before CloudFront forwards the response to the viewer (viewer response).

You just upload your Node.js code to AWS Lambda and configure your function to
be triggered in response to an Amazon

CloudFront request.

The code is then ready to execute across AWS locations globally when a request
for content is received, and scales with

the volume of CloudFront requests globally.

