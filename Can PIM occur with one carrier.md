# Can PIM occur with one carrier?

*Tags: antenna · score 5*

## Question

the literature talks about PIM occuring with two or more carriers: can it not happen in a single carrier antenna? e.g. creating second harmonic (2*f)?

## Answer (score 2, by JSH)

It's true the only thing to worry about with just one carrier is harmonics as you and Kevin suggest. However, when one modulates the carrier we generate a variety of frequencies near the carrier that can play off each other as many little carriers. The classic check to see how well our radio transmitters keep IMD at bay is the two-tone test. In theory this two tone test applies to our antenna system as well.

The likely reason we don't hear more about single-system PIM is those who worry about PIM are generally concerned with PIM generation at sites with many radio services all with strong signals. Two strong signals into a non-linear junction is no joke and can throw a mix-product signal on top of another radio service.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5384/can-pim-occur-with-one-carrier, by user5448, JSH. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
