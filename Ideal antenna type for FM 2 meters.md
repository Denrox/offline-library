# Ideal antenna type for FM 2 meters?

*Tags: antenna, antenna-construction, 2m-band · score 4*

## Question

Clearly, building a Yagi tuned for 2 meters will likely have the best *directional* performance. Putting that aside, I'm trying to get information on what antenna type will have the best overall performance in the 2 meter band in an NFM mode.

I have a 5/25 watt 2 meter FM transceiver that I'm currently using. I've been experimenting with a ground plane antenna that I built with 4 radials. Just using it here in the office (rather than up high and outside) reception seems "ok". SWR is currently 3:1, but I'm not using it for TX at the moment. I'm also hesitant to try to tune it since I'm not sure if the ground plane radials are too long... or too short. :) I'm afraid that I could make things worse by trimming them.

I'm on a bit of a budget, so I'm currently building gear. In your experience (or if you can back it up with some theory), which type of antenna would provide the best overall (non-directional) performance? Building a dipole is definitely within my capabilities. I'm sure I can handle a j-pole too... but I'd rather not end up in an endless cycle of antenna building. :) I'd rather build the thing just once!

**Update**: Just for clarification, "working ok" means that I'm reading a signal off of a repeater that's 43 miles away in Hartford, CT with the antenna sitting on the floor of my office. Perhaps I just need to scale up, tune it and get it up above my roof.

## Accepted answer (score 6, by Kevin Reid AG6YO)

Fundamental questions in a choice of antenna design are:

- Does it have the proper polarization (vertical, horizontal, or circular)?
- Does it have the proper radiation pattern?

Some secondary issues are:

- Will the antenna be small enough for the space available, at the desired frequency?
- How will it be mechanically supported, without interfering with the electrical properties?
- Will nearby objects interfere with it, or assist it (e.g. car roof as ground plane)?
- What type of matching network will it require?

The **mode** does not matter at all. The **frequency** only matters as it affects the size and therefore what is feasible.

You've said you want to do 2 meter FM, and that means that you will want **vertical polarization**. (This mainly means you don't want to build a horizontal dipole, which is a shame because it's really simple. Vertical dipoles work fine, but you need a horizontal structure to keep the feed line running away perpendicularly, which is why it's rarely done.)

This leaves you with a wide variety of vertical antenna designs — ground plane (with radials, or mounted on a metal roof), J-pole, bazooka dipole, coaxial collinear, et cetera. These can all work; it's largely a matter of what you want to build.

However, one factor we haven't yet addressed is the radiation pattern. You said “non-directional”, but there's no such thing as a truly omnidirectional (*isotropic*) antenna. Any so-called omnidirectional vertical antenna will in fact have a null pointing directly upward. In between directly up and horizontal, the pattern depends on the antenna design, as well as how high above the earth it is. What you want depends on the environment you're in and how stably actually-vertical your antenna is: if you have it mounted in a fixed location *with an unobstructed horizontal view* then you can benefit from using a higher-gain antenna (more horizontal, less vertical pattern).

Overall: Don't worry about it too much. Given that you're *building* your antenna, it's likely much more important to pick a design that you can build accurately and tune easily (because small variations in length can matter a lot for VHF).

## Answer (score 2, by Doc)

From the intended operating or design frequency point that you made the 3:1 swr reading go down 1 mhz and measure the swr. Did the swr go up or down? If the swr reading went down then the radials are too long and can be clipped 1/8" ata a time until <1.5:1 swr is accomplished.

If on the other hand when you change frequency down by 1 mhz the swr goes up, then go up 1 mhz from the intended operating or design frequency. If the swr goes down then the antenna is too short and you must add length.

K2PHD

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5211/ideal-antenna-type-for-fm-2-meters, by David Hoelzer, Kevin Reid AG6YO, Doc. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
