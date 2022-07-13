#### VPC FLOW LOGS

Flow Logs capture information about the IP traffic going to and from network
interfaces in a VPC.

Flow log data is stored using Amazon CloudWatch Logs.

**Flow logs can be created at the following levels:**

- VPC.

- Subnet.

- Network interface.

You can’t enable flow logs for VPC’s that are peered with your VPC unless the
peer VPC is in your account.

You can’t tag a flow log.

You can’t change the configuration of a flow log after it’s been created.

After you’ve created a flow log, you cannot change its configuration (you need
to delete and re- create).

**Not all traffic is monitored, e.g. the following traffic is excluded:**

- Traffic that goes to Route53.

- Traffic generated for Windows license activation.

- Traffic to and from 169.254.169.254 (instance metadata).

- Traffic to and from 169.254.169.123 for the Amazon Time Sync Service.

- DHCP traffic.

- Traffic to the reserved IP address for the default VPC router.

