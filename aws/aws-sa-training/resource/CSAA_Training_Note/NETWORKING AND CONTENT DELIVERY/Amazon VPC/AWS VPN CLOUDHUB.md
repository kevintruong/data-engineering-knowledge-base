#### AWS VPN CLOUDHUB

The AWS VPN CloudHub operates on a simple hub-and-spoke model that you can use
with or without a VPC.

Use this design if you have multiple branch offices and existing internet
connections and would like to implement a

convenient, potentially low-cost hub-and-spoke model for primary or backup
connectivity between these remote offices.

VPN CloudHub is used for hardware-based VPNs and allows you to configure your
branch offices to go into a VPC and then

connect that to the corporate DC (hub and spoke topology with AWS as the hub).

Can have up to 10 IPSec tunnels on a VGW by default.

Uses eBGP.

Branches can talk to each other (and provides redundancy).

Can have Direct Connect connections.

Hourly rates plus data egress charges.

The diagram below depicts an AWS VPN CloudHub configuration:

