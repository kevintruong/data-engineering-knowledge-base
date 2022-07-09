#### Question  54


**You need to configure an application to retain information about each user session and have decided to implement a

layer within the application architecture to store this information.**


**Which of the options below could be used? (Select TWO)**


1: Sticky sessions on an Elastic Load Balancer (ELB)


2: A block storage service such as Elastic Block Store (EBS)


3: A workflow service such as Amazon Simple Workflow Service (SWF)


4: A relational data store such as Amazon RDS


5: A key/value store such as ElastiCache Redis


Answer: 1,5


**Explanation:**


In order to address scalability and to provide a shared data storage for sessions that can be accessible from any

individual web server, you can abstract the HTTP sessions from the web servers themselves. A common solution to for this

is to leverage an In-Memory Key/Value store such as Redis and Memcached.


Sticky sessions, also known as session affinity, allow you to route a site user to the particular web server that is

managing that individual user’s session. The session’s validity can be determined by a number of methods, including a

client-side cookie or via configurable duration parameters that can be set at the load balancer which routes requests to

the web servers. You can configure sticky sessions on Amazon ELBs.


- CORRECT "Sticky sessions on an Elastic Load Balancer (ELB)" is the correct answer.


- CORRECT "A key/value store such as ElastiCache Redis" is the correct answer.


- INCORRECT "A block storage service such as Elastic Block Store (EBS)" is incorrect. In this instance the question

  states that a caching layer is being implemented and EBS volumes would not be suitable for creating an independent

  caching layer as they must be attached to EC2 instances.


- INCORRECT "A workflow service such as Amazon Simple Workflow Service (SWF)" is incorrect. Workflow services such as

  SWF are used for carrying out a series of tasks in a coordinated task flow. They are not suitable for storing session

  state data.


- INCORRECT "A relational data store such as Amazon RDS" is incorrect. Relational databases are not typically used for

  storing session state data due to their rigid schema that tightly controls the format in which data can be stored.


**References:**


https://aws.amazon.com/caching/session-management/

