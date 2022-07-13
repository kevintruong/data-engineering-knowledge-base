#### CLUSTERS


ECS Clusters are a logical grouping of container instances the you can place tasks on.


A default cluster is created but you can then create multiple clusters to separate resources.


ECS allows the definition of a specified number (desired count) of tasks to run in the cluster.


Clusters can contain tasks using the Fargate and EC2 launch type.


For clusters with the EC2 launch type clusters can contain different container instance types.


Each container instance may only be part of one cluster at a time.


“Services” provide auto-scaling functions for ECS.


Clusters are region specific.


You can create IAM policies for your clusters to allow or restrict users’ access to specific clusters.

