# What does the spark-gap do in a spark-gap transmitter?

*Tags: transmitter, history · score 12*

## Question

I read the Wikipedia article about spark-gap transmitters and I have to admit that I’m even more confused as to what the spark-gap actually did.

The article references this simplified circuit diagram:

So it seems to me (and correct me where I’m confused):

- the power source is a battery so the spark itself is a DC spark and not AC of any frequency
- there’s an antenna so the spark-gap isn’t the EMF radiator

So what is the spark gap exactly doing? I had originally thought it was acting as an oscillator / signal generator but if it’s a DC spark that doesn’t seem to be the case. And if it’s the EMF generator then what’s the antenna doing? And why is here an inductor and capacitor on the right side in an LC configuration?

Some light would be appreciated.

## Accepted answer (score 11, by tomnexus)

The spark gap is a simple, low-tech way of generating high frequencies. It was the only way of generating them before valves and transistors were invented.

As C1 charges up through R1, eventually the air in the spark gap breaks down, becoming a short circuit. The breakdown of a spark gap happens over just a few nanoseconds. (It turns off much more slowly when voltages on C1 and C2 become equal).

The current through the spark gap is a sort of square up, exponential down. The leading edge contains frequency components up to at least 100 MHz. The bandwidth of a step change is roughly 0.35 / the rise time.

These high frequency components are what excite the tuned circuit, or if you like, are filtered by the tuned circuit, so that only the kHz or MHz component passes through the circuit.

The frequency might have been 500 kHz (Titanic) or later a few MHz. If the loaded Q of the LC circuit is 50, at the frequency of interest, the resonant circuit will "Ring" for 50 cycles, decaying to about half its initial amplitude. This is called a damped wave. At each spark the transmitter sends one of these short, wide, damped RF pulses. (I think as they often had resonant antennas, the loaded Q would have been much lower). The decay process takes about 100 microseconds.

Note also that a Q of 50 will lead to a transmitted signal bandwidth of perhaps 10 kHz, much more depending on what threshold you use for bandwidth, which is quite wide by today's standards and much more than required for morse code. This is why Damped Wave emissions are not allowed by modern radio amateur laws.

Spark gaps up to 1910 simply triggered themselves again and again as C1 charged up enough to cause breakdown. This lead to a random pattern of the bursts of RF, which made a hissing sound in the headphones when detected by a simple AM receiver like a crystal set. You probably know the hissing sound of a randomly triggered spark.

The Titanic was one of the first ships to have a new rotary spark gap, triggered by a rotating disc with metal studs, between the terminals of the spark gap. This made the breakdown happen at regular intervals, a few hundred times per second. These make a new buzzing sound in the receiving headphones.

Lots more about the radios on Titanic, here.

## Answer (score 4, by niels nielsen)

the spark gap's purpose is to very suddenly change the current in the LC circuit to which the antenna is, in fact, directly connected. the sudden change produces a very strong inductive kick in that circuit, producing a suddenly-rising voltage in it. that sudden rise gets filtered by the capacitor and inductor, causing them to resonate at the transmitting frequency with an amplitude that exponentially decays as RF energy gets radiated out of the circuit and into space via the antenna. Careful choice of the circuit components and spark gap length then cause the spark breakdown to occur at a repetition rate in the audio frequency range, thus producing a wave train consisting of successive mHz oscillations that decay and get replaced by fresh oscillations at a rate of hundreds of Hz. the waveform is heard at the receiver as an amplitude-modulated carrier with significant sideband widths.

Dozens of refinements to this basic idea were made over the years before vacuum tubes were eventually invented, to stabilize the spark, quench it purposefully, allow it to be easily keyed to produce morse code, and couple the oscillations to the antenna so as to maximize the efficiency of the process.

## Answer (score 3, by Steve Richards)

Step 1, short out the spark gap.

Step 2, lots of current flows through the inductor L, building up magnetic lines of flux (magnetic field) around the inductor L.

Step 3, remove the short.

Step 4, the current stops flowing through L, causing the magnetic field to collapse, causing a massive reverse voltage across the coil (Back EMF), charging the capacitor C2.

Step 5, the field around L has collapsed to 0V, the capacitor C2 now discharges into L the inductor.

Step 6, this oscillation, L -> cap -> L -> Cap -> L carries on slowly reducing in size as power is lost due to the resistance of L the inductor.

Step 7, This is 'kicking' a tuned circuit (L and C2) causing it to oscillate. As others have mentioned the frequency of oscillation depends upon the value of L and C2. How long the oscillation lasts for before it decays to zero volts, depends mainly upon the value of the resistance of L the inductor.

Step 8, Once amplifiers became available, it could be arranged for a small pulse to be sent to the L and the C, to keep it oscillating.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10379/what-does-the-spark-gap-do-in-a-spark-gap-transmitter, by RoboKaren, tomnexus, niels nielsen, Steve Richards. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
