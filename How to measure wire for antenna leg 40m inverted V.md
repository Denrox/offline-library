# How to measure wire for antenna leg | 40m inverted V

*Tags: hf, inverted-vee · score 5*

## Question

I am building the antenna for the first time and I have choosen to start with 40m inverted-v. I am almost done with the center insulator made of PVC piping elements, three eye hooks and SO 239 connector at the bottom.

Now I am getting ready to measure and attach legs and I have a bit of a question here.

I found an online calculator and according to it, for 40m Inverted-V with 22 degrees angle from horizontal, each leg should be around 31ft 10inch. Now I am trying to figure is that the distance between the eye hook on center insulator and end insulator or that is the total length of wire that should be used. I am working on the theory that I will need around 10 inches of wire to tie it to both ends so if I were to use the exact length of wire, the distance between the center point and end insulator would be a bit shorter?

Is my dipole leg length the actual length of wire used or the distance between the center point and end insulator.

## Answer (score 5, by Scott Earle)

If I were making an antenna like that, I would add the extra 10" (25cm) first anyway, because when you come to tune it it's much easier to trim the wire than it is to add wire to it later.

Also, because the antenna is an inverted V (a kind of dipole - a balanced antenna) and you are using coaxial cable to feed it, you should consider using a **balun** at the feedpoint. This will effectively stop the outside of the coax from carrying unwanted (common-mode) currents and being part of the antenna, and will help keep RF out of the shack.

**EDIT**: To answer the question, it is my understanding that it's basically the length of the wire between the centre and the tip of each leg, and any additional wire you use to tie it off or to wrap around an anchor does not count in the length calculation.

## Answer (score 3, by Phil Frost - W8II)

The length is measured between the center and the end insulator.

I'd further add: don't overthink it. Common practice is to cut the wire a bit long, then iteratively make it shorter until you get a good match at your target frequency. Things like proximity to ground or other conductive objects can cause some deviation from the idealized conditions used by generic calculators, so an iterative empirical approach is often best.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/13334/how-to-measure-wire-for-antenna-leg-40m-inverted-v, by Bogdan YU2DBC, Scott Earle, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
