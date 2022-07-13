#### RECORDS

**Amazon Route 53 currently supports the following DNS record types:**

- A (address record)

- AAAA (IPv6 address record)

- CNAME (canonical name record)

- CAA (certification authority authorization)

- MX (mail exchange record)

- NAPTR (name authority pointer record

- NS (name server record)

- PTR (pointer record)

- SOA (start of authority record)

- SPF (sender policy framework)

- SRV (service locator)

- TXT (text record)

- Alias (an Amazon Route 53 - specific virtual record)

The Alias record is a Route 53 specific record type.

Alias records are used to map resource record sets in your hosted zone to Amazon
Elastic Load Balancing load balancers,

Amazon CloudFront distributions, AWS Elastic Beanstalk environments, or Amazon
S3 buckets that are configured as

websites.

You can use Alias records to map custom domain names (such as api.example.com)
both to API

Gateway custom regional APIs and edge-optimized APIs and to Amazon VPC interface
endpoints.

The Alias is pointed to the DNS name of the service.

You cannot set the TTL for Alias records for ELB, S3, or Elastic Beanstalk
environment (uses the service’s default).

Alias records work like a CNAME record in that you can map one DNS name (e.g.
example.com) to another ‘target’ DNS

name (e.g. elb1234.elb.amazonaws.com).

An Alias record can be used for resolving apex / naked domain names (e.g.
example.com rather than sub.example.com).

A CNAME record can’t be used for resolving apex / naked domain names.

Generally, use an Alias record where possible. The following table details the
differences between Alias and CNAME

records:

Route 53 supports wildcard entries for all record types, except NS records.

