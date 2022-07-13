##### Question 7, Answer: 1

**Explanation:**

```

1 is correct. To forward based on the path (e.g. /orders or /account) you can use the ALB with

path-based routing.

2 is incorrect. Host-based routing uses the host name (e.g. dctlabs.com or amazon.com) rather

than the path (e.g. /orders or /account).

3 is incorrect. The NLB can forward based on different ports/listeners. However all of this traffic

will be coming on the single port for HTTPS (443).

4 is incorrect. The CLB is a layer 7 router but there is not concepts of path-based routing.

```

