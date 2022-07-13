#### MULTIPART UPLOAD

Can be used to speed up uploads to S3.

Multipart upload uploads objects in parts independently, in parallel and in any
order.

Performed using the S3 Multipart upload API.

It is recommended for objects of 100MB or larger.

Can be used for objects from 5MB up to 5TB.

Must be used for objects larger than 5GB.

If transmission of any part fails it can be retransmitted.

Improves throughput.

Can pause and resume object uploads.

Can begin upload before you know the final object size.

