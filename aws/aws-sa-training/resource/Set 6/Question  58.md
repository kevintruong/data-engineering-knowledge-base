#### Question  58


**An application receives a high traffic load between 7:30am and 9:30am daily. The application uses an Auto Scaling

group to maintain three instances most of the time but during the peak period it requires six instances.**


**How can a Solutions Architect configure Auto Scaling to perform a daily scale-out event at 7:30am and a scale-in event

at 9:30am to account for the peak load?**


1: Use a Simple scaling policy


2: Use a Scheduled scaling policy


3: Use a Dynamic scaling policy


4: Use a Step scaling policy


**Answer: 2**


**Explanation:**


The following scaling policy options are available:


**Simple** – maintains a current number of instances, you can manually change the ASGs min/desired/max and attach/detach

instances.


**Scheduled** – Used for predictable load changes, can be a single event or a recurring schedule


**Dynamic** (event based) – scale in response to an event/alarm.


Step – configure multiple scaling steps in response to multiple alarms.


- CORRECT "Use a Scheduled scaling policy" is the correct answer.


- INCORRECT "Use a Simple scaling policy" is incorrect. Please refer to the description above.


- INCORRECT "Use a Dynamic scaling policy" is incorrect. Please refer to the description above.


- INCORRECT "Use a Step scaling policy" is incorrect. Please refer to the description above.


**References:**


https://docs.aws.amazon.com/autoscaling/ec2/userguide/schedule_time.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/aws-auto-

scaling/

