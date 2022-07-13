#### SCALABILITY

You can only scale RDS up (compute and storage).

You cannot decrease the allocated storage for an RDS instance.

You can scale storage and change the storage type for all DB engines except MS
SQL.

For MS SQL the workaround is to create a new instance from a snapshot with the
new configuration.

Scaling storage can happen while the RDS instance is running without outage
however there may be performance

degradation.

Scaling compute will cause downtime.

You can choose to have changes take effect immediately, however the default is
within the maintenance window.

Scaling requests are applied during the specified maintenance window unless
“apply immediately” is used.

All RDS DB types support a maximum DB size of 64 TiB except for Microsoft SQL
Server (16 TiB).

