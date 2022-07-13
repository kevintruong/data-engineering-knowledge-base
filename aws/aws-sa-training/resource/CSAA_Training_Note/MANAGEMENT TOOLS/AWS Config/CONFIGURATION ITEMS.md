#### CONFIGURATION ITEMS

A Configuration Item (CI) is the configuration of a resource at a given
point-in-time. A CI consists of 5 sections:

1. Basic information about the resource that is common across different resource
   types (e.g., Amazon Resource Names,

   tags).

2. Configuration data specific to the resource (e.g., EC2 instance type).

3. Map of relationships with other resources (e.g., EC2::Volume vol-3434df43 is
   “attached to instance” EC2 Instance

   i-3432ee3a).

4. AWS CloudTrail event IDs that are related to this state.

5. Metadata that helps you identify information about the CI, such as the
   version of this CI, and when this CI was

   captured.

