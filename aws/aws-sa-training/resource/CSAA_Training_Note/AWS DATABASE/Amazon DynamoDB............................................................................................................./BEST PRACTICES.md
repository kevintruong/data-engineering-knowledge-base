#### BEST PRACTICES

Keep item sizes small.

If you are storing serial data in DynamoDB that will require actions based on
date/time use separate tables for days,

weeks, months.

Store more frequently and less frequently accessed data in separate tables.

If possible, compress larger attribute values.

Store objects larger than 400KB in S3 and use pointers (S3 Object ID) in
DynamoDB.

