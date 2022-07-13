##### Question 3 answer: A,B

Explanation:

```

A password policy can be defined for enforcing password length, complexity etc. (applies to all

users).

You can allow or disallow the ability to change passwords using an IAM policy and you should

attach this to the group that contains the users, not to the individual users themselves.

You cannot use an IAM role to perform this function.

The AWS STS is not used for controlling password policies.

```

