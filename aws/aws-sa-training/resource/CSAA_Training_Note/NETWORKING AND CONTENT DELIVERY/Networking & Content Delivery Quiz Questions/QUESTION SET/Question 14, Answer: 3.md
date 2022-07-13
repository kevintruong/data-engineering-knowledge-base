##### Question 14, Answer: 3

**Explanation:**

```

1 is incorrect. To provide low-latency access with Amazon S3 you would need to copy the videos

to buckets in different regions around the world and then create a mechanism for directing

employees to the local copy.

2 is incorrect. AWS Global Accelerator is used for directing users of applications to local points of

presence around the world. It is not used for accessing content in S3, it’s used with ELB and

EC2.

3 is correct. CloudFront is a content delivery network and is ideal for this use case as it caches

the content around the world, provides a single endpoint address, and uses a single source for

the videos.

4 is incorrect. AWS Lambda is a compute service and not suited to this use case.

```

