### S3 performance guidelines

AWS provide some performance guidelines for Amazon S3. These are summarized
here:

**Measure Performance -** When optimizing performance, look at network
throughput, CPU, and DRAM requirements. Depending

on the mix of demands for these different resources, it might be worth
evaluating different Amazon EC2 instance types.

**Scale Storage Connections Horizontally -** You can achieve the best
performance by issuing multiple concurrent

requests to Amazon S3. Spread these requests over separate connections to
maximize the accessible bandwidth from Amazon

S3.

**Use Byte-Range Fetches** - Using the Range HTTP header in a GET Object
request, you can fetch a byte-range from an

object, transferring only the specified portion. You can use concurrent
connections to Amazon S3 to fetch different byte

ranges from within the same object. This helps you achieve higher aggregate
throughput versus a single whole-object

request. Fetching smaller ranges of a large object also allows your application
to improve retry times when requests are

interrupted.

**Retry Requests for Latency-Sensitive Applications -** Aggressive timeouts and
retries help drive consistent latency.

Given the large scale of Amazon S3, if the first request is slow, a retried
request is likely to take a different path

and quickly succeed. The AWS SDKs have configurable timeout and retry values
that you can tune to the tolerances of your

specific application.

**Combine Amazon S3 (Storage) and Amazon EC2 (Compute) in the Same AWS Region
-** Although S3 bucket names are globally

unique, each bucket is stored in a Region that you select when you create the
bucket. To optimize performance, we

recommend that you access the bucket from Amazon EC2 instances in the same AWS
Region when possible. This helps reduce

network latency and data transfer costs.

**Use Amazon S3 Transfer Acceleration to Minimize Latency Caused by Distance -**
Amazon S3 Transfer Acceleration manages

fast, easy, and secure transfers of files over long geographic distances between
the client and an S3 bucket. Transfer

Acceleration takes advantage of the globally distributed edge locations in
Amazon CloudFront. As the data arrives at an

edge location, it is routed to Amazon S3 over an optimized network path.
Transfer Acceleration is ideal for transferring

gigabytes to terabytes of data regularly across continents. It's also useful for
clients that upload to a centralized

bucket from all over the world.

