##### Question 12, Answer: 4

**Explanation:**

```

1 is incorrect. An EC2 instance is not cost-effective for a workload that needs to run only

occasionally for 10 minutes.

2 is incorrect. An ECS task is not the most operationally effective option as you must spin up the

ECS task to run the code and then manage the deletion of the task.

3 is incorrect. AWS Batch is used for running batch computing jobs on many EC2 instances. It’s

not cost-effective or operationally effective for this use case.

4 is correct. This is the most cost-effective and operationally effective option. Remember that

the maximum execution time is 900 seconds (15 minutes) so you are well within that

timeframe here.

```

