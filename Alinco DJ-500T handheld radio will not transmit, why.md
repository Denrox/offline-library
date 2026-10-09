# Alinco DJ-500T handheld radio will not transmit, why?

*Tags: equipment-operation, alinco · score 6*

## Question

Shows the word OFF on screen when PTT is pressed. In settings "TX" is set to on, what am I missing?

The manual is no use due to poor translation and general incompleteness.

## Answer (score 5, by Glenn W9IQ)

This indicates that you are attempting to transmit out of band. This is typically a symptom of having the wrong offset (+/-) programmed for that channel.

If you visit the Alinco FAQ page you will find this advice for similar models.

## Answer (score 4, by Bernard ''ben'' Tremblay)

Glenn's answer here gave me the nudge I needed. Checking through parameters, I found #11 ... Offset ... **5.000 seemed default setting.**

With Offset at 5.000 the transmitter was stopped because that would mean operating on an Out of Band frequency.

The anonymous OM who posted https://www.youtube.com/watch?v=jPCzJV3gPYQ did an admirable job of walking through initial programming, but everything I tried threw an "***OFF***" error. Simplex gave me full power out, but neither + nor - responded properly.

I painstakingly spooled down all the way from 5.000 to 0.600 and guess what. Yup. Just broke squelch on our repeater!

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10310/alinco-dj-500t-handheld-radio-will-not-transmit-why, by Kevin, Glenn W9IQ, Bernard ''ben'' Tremblay. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
