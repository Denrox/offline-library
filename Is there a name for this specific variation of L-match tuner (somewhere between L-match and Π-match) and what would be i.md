# Is there a name for this specific variation of L-match tuner (somewhere between L-match and Π-match) and what would be its advantages over L-match?

*Tags: antenna-tuner, end-fed-antenna · score 4*

## Question

So I've been looking at the internals of the Icom AT-141 end-fed antenna tuner which I have, and I've noticed that it has some sort of pre-tuning LC stage before its traditional L-tuner network.

The arrows on the left side of the schematic are supposed to represent tunable components (in reality, series of relay-switched fixed components).  
The C1 has range from 9 pF to 4.79 nF, and I estimate that the L1 has range from 56 nH up to 33 μH.  
On the right side, I've estimated the coil inductivities, since they're not listed in the documentation, and the capacitor capacitance is correct. For extra context, the tuner is designed to tune a wire at least 7 meters long across range starting from 1.6 MHz and going up to 30 MHz.

So my questions are:  
Is there a commonly used name for this tuner topology, and In what way would this topology be more advantageous compared to just a classic L-match tuner with more component values in its L and C stages?

## Answer (score 2, by Marcus Müller)

First of, let's simplify. C2-C5 form just one 100 pF capacitor "Cv" (probably with higher voltage rating), and we can just say "L2+L3 and bypasses make one L, which is either open or has a value between 27.5 and 76.1 µHJ; let's call it Lx".

I'd say this has multiple operation modes:

- SW1 left, SW2 closed: $\Pi$ match (L1-Lx, if not bypassed, simply form one L, C before and after to ground; a $\Pi$ matcher)
- SW1 right, Lx bypassed, SW2 open: L1 and C1 form a low-pass filter, and based on the values, I'd say this is an L matcher
- SW1 right, Lx bypassed, SW2 closed: C1 and Cv form one capacitor, call it Ct, and then we L1 and Ct form a low-pass filter, an L match.
- SW1 right, Lx not completely bypassed, SW2 closed: yeah, some ladder filter.

## Answer (score 2, by Ryuji AB1WX)

Icom AT-141 is a feedpoint antenna tuner meant for wire antennas. That is, the end of a longwire/vertical/inv L/etc. connects directly on the tuner's terminal. This is the critical point in understanding the intention of this circuit.

A property of a monopole antenna of a fixed length (let's say 10m long for simplicity; ICOM specifies 7.0m or longer on the catalog spec case) is that the feedpoint impedance varies hugely depending on the driving frequency. At 7MHz that antenna is roughly 1/4 wavelength and has some 35 ohm impedance. At 14MHz the impedance will be very high. Just undre 14MHz, the impedance will be very high and very inductive. Also, at 1.8MHz and 3.5MHz, the impedance will be very low and very significantly capacitive.

In the frequency range of about 5 to 10 MHz, just the L-match part alone should be able to handle that load impedance. BUT! at 14MHz, the impedance is too high and it is outside the match space of the L-match part. So, engage SW2 and bring the impedance to the capacitive zone, well within the match space of the L-network. Conversely, when the frequency is 1.8 or 3.5MHz, the impedance is way too low and hugely capacitive. A much larger inductor is needed to cancel such a large capacitive reactance. No problem, engage SW3 and SW4. It's basically going to function like a base-loaded antenna.

As you see above, if a piece of coax or any transmission line of an unknown length is allowed between this tuner and the antenna, this scheme would fail. But this works beautifully because it is a feedpoint tuner, and we know the general impedance properties of wire antennas.

What is it called? I think it is still an L-match; it just has an impedance "modifier" for coarse adjustments before the L-match.

The advantage: as discussed above. This circuit expands the match space of an L-network in parts of the impedance space that is most likely encountered by a real wire antenna rather than being ready for a more exhaustive range of load impedances.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20610/is-there-a-name-for-this-specific-variation-of-l-match-tuner-somewhere-between, by AndrejaKo, Marcus Müller, Ryuji AB1WX. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
