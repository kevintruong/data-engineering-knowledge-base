#### SCALABILITY


Push button scaling without downtime.


You can scale down only 4 times per calendar day.


AWS places some default limits on the throughput you can provision.


These are the limits unless you request a higher amount:


DynamoDB can throttle requests that exceed the provisioned throughput for a table.


DynamoDB can also throttle read requests for an Index to prevent your application from consuming too many capacity

units.


When a request is throttled it fails with an HTTP 400 code (Bad Request) and a ProvisionedThroughputExceeded exception.

