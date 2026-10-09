# Portable radio antenna measurement

*Tags: antenna, measurement · score 3*

## Question

Just purchased a HP 8711A and have "upgraded" the bootrom to enable vector measurements. I am now trying to learn more about how to make better measurements and understand what's going on.  
One of the things I wanted to try is to measure the return loss of some portable antennas (for use on portable radios).

The radio and user are necessary parts as some kind of counterpoise for these antennas, which makes measurements rather difficult.

Can I:  
- Take a metal plate  
- Mount a flange mount connector on it  
- Make sure the the plate is connected to the braid  
- Mount the antenna on this contraption  
- Use this as a substitution for the body + radio ?

Any other thoughts? Pitfalls I should keep in mind?

## Accepted answer (score 3, by Kevin Reid AG6YO)

You should also **put an unun/choke on the feed line** at the back side of your plate to ensure that only the plate and not the plate+coax+analyzer are involved. Once you've done that, I see no reason why your proposed measurement strategy wouldn't work to give you a repeatable number.

Of course, that number won't exactly reflect the antenna's behavior in actual operation, because even if your metal plate happens to match one particular HT+arm+body configuration it won't match others. You could have several different fixtures to model different situations, but even then you have the problem of validating your model.

The only way I can see to do that validation is to measure the reflected power in the real configuration — i.e. either a handheld radio with a suitable meter built-in, a physically compact meter inserted in-line at the antenna port, or an analyzer in a handheld form factor.

If you don't have this reference, then you can still make repeatable measurements, but you don't know what measured values correspond to the *best* real-world performance.

For what it's worth, some rough measurements about the size of the variation:

I have a handheld antenna analyzer which can read R, X, SWR, and return loss. The primary way in which it is different from a handheld radio is a very different case design (large and plastic rather than small and coated metal), which affects the amount of coupling to the hand.


I attached a 1/4 wave whip (no additional ground plane) and measured return loss values between 3 and 6 dB at 146 MHz depending on how I held the unit.


A more “rubber duck” style antenna (about half length) varied between 10 and 35 dB and was much more obviously sensitive to exact positioning.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6792/portable-radio-antenna-measurement, by Dieter Vansteenwegen, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
