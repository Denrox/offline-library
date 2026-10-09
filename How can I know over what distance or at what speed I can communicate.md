# How can I know over what distance or at what speed I can communicate?

*Tags: antenna, propagation, modes · score 3*

## Question

Given some description of some parameters like:

- transmitter power
- frequency
- antenna
- location
- time of day

how can I know over what distance communication is possible? Can I know the limits to these things, like:

- Simplest, smallest antenna for tuning WWV, WWVH?
- [What bands and modes will give me voice at 3,000 miles?](What%20bands%20and%20modes%20will%20give%20me%20voice%20at%203%2C000%20miles.md)
- [Best QRP HF band for small antenna?](Best%20QRP%20HF%20band%20for%20small%20antenna.md)
- [Smallest HF antenna for DX?](Smallest%20HF%20antenna%20for%20DX.md)

## Accepted answer (score 3, by hotpaw2)

Shannon's law on information communication provides statistical upper limits on data rate given a signal to noise ratio: *S/N*.

There may be nice physics models on the power coupled between a pair of dipoles in free space, to get a best case on signal power received.

Unfortunately, the transmission channel is usually not in outer space, but contains a huge number of absorptive and reflective bodies (perhaps including the upper atmosphere), often in unknown or nearly randomly changing configurations, ruining any nice clean closed form equation for the the received *S* in *S/N*.

Also unfortunately, the noise floor (the *N* in *S/N*) is almost always quite indeterminate in the real world, and has to be found by experimentation. Background noise, interfering signals, receiver front-end noise, and etc.

You can test yourself, or perhaps make a reasonable guess at what might be possible based on prior published results. Assuming conditions are fairly similar and don't change much.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1438/how-can-i-know-over-what-distance-or-at-what-speed-i-can-communicate, by Phil Frost - W8II, hotpaw2. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
