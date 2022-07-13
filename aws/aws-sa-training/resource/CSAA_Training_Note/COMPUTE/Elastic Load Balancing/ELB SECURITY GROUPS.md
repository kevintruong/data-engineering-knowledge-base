#### ELB SECURITY GROUPS

Security groups control the ports and protocols that can reach the front-end
listener.

In non-default VPCs you can choose which security group to assign.

You must assign a security group for the ports and protocols on the front-end
listener.

You need to also allow the ports and protocols for the health check ports and
back-end listeners.

**Security group configuration for ELB:**

**Inbound to ELB (allow)**

- Internet-facing ELB:

  o Source: 0.0.0.0/0. o Protocol: TCP.

```

o Port: ELB listener ports.

```

**Internal-only ELB:**

- Source: VPC CIDR.

- Protocol: TCP.

- Port: ELB Listener ports.

**Outbound

(allow, either type of ELB):**

- Destination: EC2 registered instances security group.

- Protocol: TCP.

- Port: Health Check/Listener.

**Security group configuration for registered instances:**

Inbound to registered instances (Allow, either type of ELB).

- Source: ELB Security Group.

- Protocol: TCP.

- Port: Health Check/Listener.

**Outbound

(Allow, for both types of ELB).**

- Destination: ELB Security Group.

- Protocol: TCP.

- Port: Ephemeral.

It is also important to ensure NACL settings are set correctly.

**Distributed Denial of Service (DDoS) protection:**

- ELB automatically distributes incoming application traffic across multiple
  targets, such as Amazon Elastic Compute

  Cloud (Amazon EC2) instances, containers, and IP addresses, and multiple
  Availability Zones, which minimizes the risk

  of overloading a single resource.

- ELB, like CloudFront, only supports valid TCP requests, so DDoS attacks such
  as UDP and SYN floods are not able to

  reach EC2 instances.

- ELB also offers a single point of management and can serve as a line of
  defence between the internet and your backend,

  private EC2 instances.

