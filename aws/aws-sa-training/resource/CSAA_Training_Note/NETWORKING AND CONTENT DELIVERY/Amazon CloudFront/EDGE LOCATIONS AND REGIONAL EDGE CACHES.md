#### EDGE LOCATIONS AND REGIONAL EDGE CACHES

An edge location is the location where content is cached (separate to AWS
regions/AZs).

Requests are automatically routed to the nearest edge location.

Edge locations are not tied to Availability Zones or regions.

Regional Edge Caches are located between origin web servers and global edge
locations and have a larger cache.

Regional Edge Caches have larger cache-width than any individual edge location,
so your objects remain in cache longer

at these locations.

Regional Edge caches aim to get content closer to users.

Proxy methods PUT/POST/PATCH/OPTIONS/DELETE go directly to the origin from the
edge locations and do not proxy through

Regional Edge caches.

Dynamic content goes straight to the origin and does not flow through Regional
Edge caches.

Edge locations are not just read only, you can write to them too.

The diagram below shows where Regional Edge Caches and Edge Locations are placed
in relation to end users:

