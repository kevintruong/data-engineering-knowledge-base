#### CACHE BEHAVIOR

Allows you to configure a variety of CloudFront functionality for a given URL
path pattern.

**For each cache behavior you can configure the following functionality:**

- The path pattern (e.g. /images/*.jpg, /images*.php).

- The origin to forward requests to (if there are multiple origins).

- Whether to forward query strings.

- Whether to require signed URLs.

- Allowed HTTP methods.

- Minimum amount of time to retain the files in the CloudFront cache (regardless
  of the values of any cache-control

  headers).

The default cache behavior only allows a path pattern of /*.

Additional cache behaviors need to be defined to change the path pattern
following creation of the distribution.

**You can restrict access to content using the following methods:**

- Restrict access to content using signed cookies or signed URLs.

- Restrict access to objects in your S3 bucket.

A special type of user called an Origin Access Identity (OAI) can be used to
restrict access to content in an Amazon S3

bucket.

By using an OAI you can restrict users so they cannot access the content
directly using the S3 URL, they must connect

via CloudFront.

**You can define the viewer protocol policy:**

- HTTP and HTTPS

- Redirect HTTP to HTTPS

- HTTPS only

**You can define the Allowed HTTP Methods:**

- GET, HEAD

- GET, HEAD, OPTIONS

- GET, HEAD, OPTIONS, PUT, POST, PATCH, DELETE

For web distributions you can configure CloudFront to require that viewers use
HTTPS.

**Field-Level Encryption:**

- Field-level encryption adds an additional layer of security on top of HTTPS
  that lets you protect specific data so

  that it is only visible to specific applications.

- Field-level encryption allows you to securely upload user-submitted sensitive
  information to your web servers.

- The sensitive information is encrypted at the edge closer to the user and
  remains encrypted throughout application

  processing.

**Origin policy:**

- HTTPS only.

- Match viewer – CloudFront matches the protocol with your custom origin.

- Use match viewer only if you specify Redirect HTTP to HTTPS or HTTPS only for
  the viewer protocol policy.

- CloudFront caches the object once even if viewers makes requests using HTTP
  and HTTPS.

**Object invalidation:**

- You can remove an object from the cache by invalidating the object.

- You cannot cancel an invalidation after submission.

- You cannot invalidate media files in the Microsoft Smooth Streaming format
  when you have enabled Smooth Streaming for

  the corresponding cache behavior.

Objects are cached for the TTL (always recorded in seconds, default is 24 hours,
default max is 1 year).

Only caches for GET requests (not PUT, POST, PATCH, DELETE).

Dynamic content is cached.

Consider how often your files change when setting the TTL.

Invalidation can be used to immediately revoke cached objects – chargeable.

Deletions propagate.

