# Can two diodes be parallelled in RB to get double the capacitance?

*Tags: diy, varicap · score 9*

## Question

It's a fact of life that air-gang capacitors, are increasingly more difficult to come by - having been superseded by the far more compact varactor diodes.

My part of the world components such as the venerable BB212, MPN3700, MV1662 are almost unheard of at the local stores; anyway I'm only getting started at attempting home-brew. Real VCO stuff will *hopefully* happen sometime in the future.

Basic theory tells me applying multiple capacitors in parallel adds up the effective capacitance a circuit will see.

Would I see the same behavior if several make-shift varicaps (say, 1N4007) were connected in parallel? i.e. does capacitance add up using varicaps in a tank that it does for any other capacitor?

## Accepted answer (score 6, by WPrecht)

The short answer is yes, they do add in parallel. But remember, the Cmin is doubled as well as the Cmax, so the tuning ratio hasn't changed. Depending on what you are using them for, this may or may not matter. Of course you can offset this with an inductor.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/540/can-two-diodes-be-parallelled-in-rb-to-get-double-the-capacitance, by VU2NHW, WPrecht. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
