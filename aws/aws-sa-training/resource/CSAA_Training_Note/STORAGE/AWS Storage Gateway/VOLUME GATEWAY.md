#### VOLUME GATEWAY

The volume gateway represents the family of gateways that support block-based
volumes, previously referred to as

gateway-cached and gateway-stored modes.

Block storage – iSCSI based.

Cached Volume mode – the entire dataset is stored on S3 and a cache of the most
frequently accessed data is cached

on-site.

Stored Volume mode – the entire dataset is stored on-site and is asynchronously
backed up to S3

(EBS point-in-time snapshots). Snapshots are incremental and compressed.

Each volume gateway can support up to 32 volumes.

In cached mode, each volume can be up to 32 TB for a maximum of 1 PB of data per
gateway (32 volumes, each 32 TB in

size).

In stored mode, each volume can be up to 16 TB for a maximum of 512 TB of data
per gateway (32 volumes, each 16 TB in

size).

