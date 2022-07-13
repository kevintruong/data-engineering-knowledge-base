#### DOMAIN NAMES

CloudFront typically creates a domain name such as a232323.cloudfront.net.

Alternate domain names can be added using an alias record (Route 53).

For other service providers use a CNAME (cannot use the zone apex with CNAME).

**Moving domain names between distributions:**

- You can move subdomains yourself.

- For the root domain you need to use AWS support.

