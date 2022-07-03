### **S3 data is made up of:**

- Key (name)
- Value (data)
- Version ID
- Metadata
- Access Control Lists

Amazon S3 automatically scales to high request rates.

For example, your application can achieve at least 3,500 PUT/POST/DELETE and 5,500 GET requests per second per prefix in a bucket.

There are no limits to the number of prefixes in a bucket. It is simple to increase your read or write performance exponentially.

For read intensive requests you can also use CloudFront edge locations to offload from S3.