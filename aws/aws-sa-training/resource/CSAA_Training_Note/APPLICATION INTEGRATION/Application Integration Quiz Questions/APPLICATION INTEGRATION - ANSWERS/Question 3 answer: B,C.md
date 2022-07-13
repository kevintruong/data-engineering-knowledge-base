##### Question 3 answer: B,C

Explanation:

```

Note that the questions asks you which transport protocols are supported, NOT which

subscribers - therefore Lambda is not supported

SNS supports notifications over multiple transport protocols:

```

- HTTP/HTTPS – subscribers specify a URL as part of the subscription
  registration

- Email/Email-JSON – messages are sent to registered addresses as email (
  text-based or JSON- object)

- SQS – users can specify an SQS standard queue as the endpoint

- SMS – messages are sent to registered phone numbers as SMS text messages

