#### ROUTING POLICIES


Routing policies determine how Route 53 responds to queries.


The following table highlights the key function of each type of routing policy:


**Simple:**


- An A record is associated with one or more IP addresses

- Uses round robin

- Does not support health checks


The following diagram depicts an Amazon Route 53 Simple routing policy configuration:


**Failover:**


- Failover to a secondary IP address.

- Associated with a health check.

- Used for active-passive.

- Routes only when the resource is healthy.

- Can be used with ELB.

- When used with Alias records set Evaluate Target Health to “Yes” and do not use health checks.


The following diagram depicts an Amazon Route 53 Failover routing policy configuration:


**Geo-location:**


- Caters to different users in different countries and different languages.

- Contains users within a particular geography and offers them a customized version of the workload based on their

  specific needs.

- Geolocation can be used for localizing content and presenting some or all of your website in the language of your

  users.

- Can also protect distribution rights.

- Can be used for spreading load evenly between regions.

- If you have multiple records for overlapping regions, Route 53 will route to the smallest geographic region.

- You can create a default record for IP addresses that do not map to a geographic location.


The following diagram depicts an Amazon Route 53 Geolocation routing policy configuration:


**Geo-proximity routing policy (requires Route Flow):**


- Use for routing traffic based on the location of resources and, optionally, shift traffic from resources in one

  location to resources in another.


**Latency based routing:**


- AWS maintains a database of latency from different parts of the world.

- Focused on improving performance by routing to the region with the lowest latency.

- You create latency records for your resources in multiple EC2 locations.


The following diagram depicts an Amazon Route 53 Latency based routing policy configuration:


**Multi-value answer routing policy:**


- Use for responding to DNS queries with up to eight healthy records selected at random.


The following diagram depicts an Amazon Route 53 Multivalue routing policy configuration:


**Weighted:**


- Similar to simple but you can specify a weight per IP address.

- You create records that have the same name and type and assign each record a relative weight.

- Numerical value that favors one IP over another.

- To stop sending traffic to a resource you can change the weight of the record to 0.


The following diagram depicts an Amazon Route 53 Weighted routing policy configuration:

