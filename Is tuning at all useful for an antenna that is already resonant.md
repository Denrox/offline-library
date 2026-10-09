# Is tuning at all useful for an antenna that is already resonant?

*Tags: antenna, impedance-matching, antenna-tuner · score 5*

## Question

Say you have a resonant antenna that also has a tuner. Does this help at all? Can your antenna be "fine tuned" ?

## Accepted answer (score 5, by webmarc)

This is one of those areas where "words matter"

The typical "tuner" may actually accomplish one or more of several functions:

- matches impedance between two "things", for ex a radio to a feed line or a feed line to an antenna;
- tranforms a balanced line to an unbalanced line, or vice versa
- introduces complimentary complex impedance to maximize power transfer
- other stuff that doesn't immediately come to mind

SO, the answer is: it depends on the characteristics of the antenna system.

If the characteristics of your antenna for all of the above concerns are optimized for your frequency of choice and antenna installation particulars, then a "tuner" doesn't do anything for you.

In fact, since any real tuner has some kind of insertion loss, there may be a net-negative effect by introducing it into an already resonant and well matched system.

If the antenna system is of sufficiently high Q, and you want to choose another frequency, then one or more of the above concerns will become interesting and some kind of "tuner" may become helpful.

For example, depending upon the Q of the antenna and the size of the band and the operator's definition of acceptable. From 3.5 MHz to 4 MHz is only 500 KHz... but ±250 KHz/3.75 MHz (the center of the 80m band) is about 7%. A tuner would almost certainly required (preferably at the feed point) to operate the entire band.

At 2m, ±2 MHz / 146 MHz is a little more than 1%, and a tuner wouldn't be required to operate over the entire band.

See also this excellent answer regarding [the bandwidth of a dipole](Calculating%20bandwidth%20of%20antenna.md)

## Answer (score 3, by Andrew)

This question is more complicated than it seems.

If the antenna in question is only being used at one frequency, and at that frequency the SWR is already low, then in terms of obtaining a good match to transmission line and radio there is no advantage in using an antenna tuner. In fact the tuner would introduce a very small amount of insertion loss, and this loss would be higher for higher frequencies.

But, a tuner will probably have a higher Q and so a narrower bandwidth than the antenna, so using a tuner might help a bit with reducing out of band interference or noise.

If the antenna is being used over a band of frequencies such as an amateur band, then if the antenna has a bandwidth such that the SWR isn't good over the entire band, then the tuner is useful because you can adjust to make the SWR perfect over the entire band.

As a rule of thumb, a tuner would not be required if the SWR is less than abupt 1.5:1 over the entire band, where the added messing around of having to adjust the tuner very time you change frequency a bit isn't worth the very small increase in performance obtained by making the SWR exactly perfect.

To be technically accurate, an antenna that is resonant at the frequency of operation isn't necessarily matched to the transmission line and radio. Such an antenna can be resonant and have a resistive impedance which doesn't match the rest of the system and in this case a tuner could be used to match the impedance of the antenna / transmission line to that of the radio.

In general, as soon as a tuner is included, the bandwidth of the entire system will be reduced, and for transmitting, any significant change (more than about 100 kHz) in frequency will probably require re-adjustment of the tuner.

If you are a perfectionist and must always have a perfect SWR regardless of how much difference it makes because it makes you feel better, then if you can live with having to re-adjust every time you change frequency, then using a tuner won't cause any problems and can be left in line.

But in my opinion in general if you can get away with using an antenna which is resonant on it's own without a tuner, that seems to be the cleanest approach with the least messing around.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/19958/is-tuning-at-all-useful-for-an-antenna-that-is-already-resonant, by NonYaBidnezz, webmarc, Andrew. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
