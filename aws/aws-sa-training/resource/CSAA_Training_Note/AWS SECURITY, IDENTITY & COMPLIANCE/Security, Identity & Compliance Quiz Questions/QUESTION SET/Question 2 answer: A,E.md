##### Question 2 answer: A,E


Explanation:


```

You can authenticate using an MFA device in the following ways:

```


- Through the AWS Management Console – the user is prompted for a user name, password and authentication code

- Using the AWS API – restrictions are added to IAM policies and developers can request temporary security credentials

  and pass MFA parameters in their AWS STS API requests

- Using the AWS CLI by obtaining temporary security credentials from STS (aws sts get- session-token)
