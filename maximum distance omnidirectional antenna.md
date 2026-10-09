# maximum distance omnidirectional antenna

*Tags: antenna, wire-antenna, wifi, loop-antenna · score 3*

## Question

I want to know this omnidirectional antenna's maximum distance:

- gain 15 dBi
- frequency 2400 GHz
- power 50 watts

## Answer (score 3, by Kevin Reid AG6YO)

**Antennas don't have ranges.** The maximum range of a link is determined by many factors in addition to the information you have about the antenna, among them:

- the power output of the transmitter (not the power rating of the antenna)
- the minimum usable signal of the *receiver*
- the strength of interfering signals
- the amount and type of obstacles (e.g. trees, building walls) between the two antennas

The only information you need about the antenna is its gain *in the relevant direction* (an “omnidirectional” antenna necessarily has less gain than a directional one).

Once you have gathered enough information, you can do a *link budget* calculation to model the expected performance. Have a look at the answers to this question: [What is a link budget, and how do I make one?](What%20is%20a%20link%20budget%2C%20and%20how%20do%20I%20make%20one.md)

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5308/maximum-distance-omnidirectional-antenna, by minthike, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
