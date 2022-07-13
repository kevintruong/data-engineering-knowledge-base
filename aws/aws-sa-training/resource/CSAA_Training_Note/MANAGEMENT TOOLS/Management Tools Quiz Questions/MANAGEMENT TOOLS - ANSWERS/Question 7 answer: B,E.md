##### Question 7 answer: B,E


Explanation:


```

EC2 status checks are performed every minute and each returns a pass or a fail status. If all

checks pass, the overall status of the instance is OK. If one or more checks fail, the overall status

is impaired.

System status checks detect (StatusCheckFailed_System) problems with your instance that

require AWS involvement to repair whereas Instance status checks (StatusCheckFailed_Instance)

detect problems that require your involvement to repair.

The action to recover the instance is only supported on specific instance types and can be used

only with StatusCheckFailed_System.

Configuring an action to terminate the instance would not help resolve system software issues as

the instance would be terminated.

```

