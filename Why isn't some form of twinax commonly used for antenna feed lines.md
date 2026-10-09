# Why isn't some form of twinax commonly used for antenna feed lines?

*Tags: feed-line · score 4*

## Question

Twinax (shielded controlled impedance balanced line pairs) is said to be used in 10G ethernet signaling for greater noise immunity that other cabling types. Why isn't twinax (or similar) commonly used for amateur radio antenna feed lines, where noise immunity on receive is also quite important? Rather than unbalanced coax or unshielded twin-lead?

(Added: Especially when dealing with a balanced antenna (dipole), balanced differential inputs, or balanced push-pull final RF amplifier stage.)

## Answer (score 3, by Caleb)

Why isn't twinax (or similar) commonly used for amateur radio antenna feed lines

It's always hard to say why something *isn't* done, but after looking around at the options I'd say cost has to be one factor. A 100' spool of 18AWG or 20AWG twinaxial cable costs around $220, which is five or six times the cost of coax or ladder line. The connectors are also much more expensive than typical coax connectors.

## Answer (score 3, by user10489)

Why coax or twin lead or ladder line?

- Because the others are traditional.
- Because twinax is relatively rare and expensive.
- Because unless you are dealing with high frequencies (>5GHz) twinax is overkill. Most amateur radio is <1GHz where coax and twin lead make more sense. Above 5GHz, more commonly I see wave guide and hardline used.

Having said that, I have seen twinax used for short runs in situations where twin lead was inappropriate — like passing through a metal window frame.

Also, it has been pointed out (in another question) that twinlead is not better (lower loss) than high end coax, so I suspect that twinax may also not be better, and possibly waveguide and hardline are better than twinax already.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16122/why-isn-t-some-form-of-twinax-commonly-used-for-antenna-feed-lines, by hotpaw2, Caleb, user10489. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
