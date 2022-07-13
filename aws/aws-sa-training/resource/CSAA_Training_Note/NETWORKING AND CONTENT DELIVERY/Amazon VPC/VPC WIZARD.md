#### VPC WIZARD

**VPC with a Single Public Subnet:**

- Your instances run in a private, isolated section of the AWS cloud with direct
  access to the Internet.

- Network access control lists and security groups can be used to provide strict
  control over inbound and outbound

  network traffic to your instances.

- Creates a /16 network with a /24 subnet. Public subnet instances use Elastic
  IPs or Public IPs to access the Internet.

**VPC with Public and Private Subnets:**

- In addition to containing a public subnet, this configuration adds a private
  subnet whose instances are not

  addressable from the Internet.

- Instances in the private subnet can establish outbound connections to the
  Internet via the public subnet using Network

  Address Translation (NAT).


- Creates a /16 network with two /24 subnets.

- Public subnet instances use Elastic IPs to access the Internet.

- Private subnet instances access the Internet via Network Address Translation (
  NAT).

**VPC with Public and Private Subnets and Hardware VPN Access:**

- This configuration adds an IPsec Virtual Private Network (VPN) connection
  between your Amazon VPC and your data center

  – effectively extending your data center to the cloud while also providing
  direct access to the Internet for public

  subnet instances in your Amazon VPC.

- Creates a /16 network with two /24 subnets.

- One subnet is directly connected to the Internet while the other subnet is
  connected to your corporate network via an

  IPsec VPN tunnel.

**VPC with a Private Subnet Only and Hardware VPN Access:**

- Your instances run in a private, isolated section of the AWS cloud with a
  private subnet whose instances are not

  addressable from the Internet.

- You can connect this private subnet to your corporate data center via an IPsec
  Virtual Private Network (VPN) tunnel.

- Creates a /16 network with a /24 subnet and provisions an IPsec VPN tunnel
  between your Amazon VPC and your corporate

  network.

