#### Question  44


**Some Amazon ECS containers are running on a cluster using the EC2 launch type. The current configuration uses the

container instance’s IAM roles for assigning permissions to the containerized applications.**


**A Solutions Architect needs to implement more granular permissions so that some applications can be assigned more

restrictive permissions. How can this be achieved?**


- [ ] This cannot be changed as IAM roles can only be linked to container instances


- [x] This can be achieved using IAM roles for tasks, and splitting the containers according to the permissions required to

different task definition profiles


- [ ] This can be achieved by configuring a resource-based policy for each application


- [ ] This can only be achieved using the Fargate launch type


*

- hasExplain:: [[explanation_Question  44.md]]