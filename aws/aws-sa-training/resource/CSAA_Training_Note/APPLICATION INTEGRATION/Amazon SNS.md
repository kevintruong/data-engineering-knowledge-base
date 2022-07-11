### Amazon SNS


Amazon Simple Notification Service (Amazon SNS) is a web service that makes it easy to set up, operate, and send

notifications from the cloud.


Amazon SNS is used for building and integrating loosely-coupled, distributed applications.


Provides instantaneous, push-based delivery (no polling).


Uses simple APIs and easy integration with applications.


Flexible message delivery is provided over multiple transport protocols.


Offered under an inexpensive, pay-as-you-go model with no up-front costs.


The web-based AWS Management Console offers the simplicity of a point-and-click interface.


Data type is JSON.


SNS supports a wide variety of needs including event notification, monitoring applications, workflow systems,

time-sensitive information updates, mobile applications, and any other application that generates or consumes

notifications.


**SNS Subscribers:**


- HTTP

- HTTPS

- Email

- Email-JSON

- SQS

- Application

- Lambda


**SNS supports notifications over multiple transport protocols:**


- HTTP/HTTPS – subscribers specify a URL as part of the subscription registration.

- Email/Email-JSON – messages are sent to registered addresses as email (text-based or JSON- object).

- SQS – users can specify an SQS standard queue as the endpoint.

- SMS – messages are sent to registered phone numbers as SMS text messages.


Topic names are limited to 256 characters.


SNS supports CloudTrail auditing for authenticated calls.


SNS provides durable storage of all messages that it receives (across multiple AZs).


Users pay $0.50 per 1 million Amazon SNS Requests, $0.06 per 100,000 notification deliveries over HTTP, and $2.00 per

100,000 notification deliveries over email.

