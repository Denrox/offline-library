# When would we ever want to use a voltage balun in ham radio?

*Tags: balun, choke-balun · score 9*

## Question

In a world where common mode current is the enemy, and we're constantly doing what we can to avoid RF in the shack, why would we ever choose a voltage type balun over a current balun?

I understand that, in general, one uses a voltage balun to keep the voltages equal and opposite. But what would be an example of a real world application of that in ham radio?

Even the DX Engineering site says that a current balun is almost always the better choice. So then why are they even selling voltage baluns? What's this rare condition where a voltage balun is the better choice?

## Accepted answer (score 12, by Phil Frost - W8II)

You'll find voltage baluns in plenty of circuits. For example,

the QRP Labs receiver module:

HPSDR Pennywhistle (twice, T1 and T3):

The Elecraft KX3:

A voltage balun can do some things a current balun can not.

Firstly, the turns ratio can be varied to provide impedance transformation. Some of these circuits use something other than a 1:1 turns ratio to optimally load the transistors.

Also, a voltage balun provides galvanic isolation. This can be useful for example to avoid ground loops which might be problematic with audio interfaces. It also allows a DC bias to be added: all three of these designs make use of that feature.

One advantage of a common-mode choke as a balun is the core needs to be sized only to handle the common-mode current, not the full current of the signal. This is a significant advantage when designing a balun for a 1 kW antenna, but in a receiver or at the output of a 20 W amplifier, this particular advantage isn't of much value.

Furthermore, in these applications the load is a circuit with equal impedances, and not an antenna which could be mounted asymmetrically or even deliberately unbalanced such as an off-center fed dipole. Thus another advantage of current baluns is again not especially needed in this application.

As for why companies continue to sell voltage baluns *for antennas*, I suspect they do so because people continue to buy them. A solution does not need to be technically the best to be economically viable.

I haven't done a rigorous cost analysis, but I'd suspect 4:1 voltage baluns may be cheaper to manufacture:

- they require only 1 core where a 4:1 current balun requires 2
- for powers of 100W or less, the necessary core may be smaller than what's required to get a useful choking impedance from a common-mode choke

A voltage balun works fine when the load really is balanced. This isn't always the case so a voltage balun may not be a robust solution, but there will always be buyers that value low cost over robustness, or may not even be aware of the issues. So I'm not surprised manufacturers continue to make voltage baluns.

## Answer (score 2, by Mike Waters)

I attended a seminar on baluns --as applied to antennas-- at a local hamfest, given by no less a guru than Glenn Shultz, W9IQ.

He nicely explained that *the only place we need to use a voltage balun in an antenna system is **for end-fed antennas***.

Every place else, use a current balun. And the simpler, the better.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16941/when-would-we-ever-want-to-use-a-voltage-balun-in-ham-radio, by Paul, Phil Frost - W8II, Mike Waters. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
