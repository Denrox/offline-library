# Antenna tuner design

*Tags: diy, antenna-tuner, loop-antenna · score 4*

## Question

In a [related question](Broadband%20antenna%20for%20SDR%20radio.md) about a broadband antenna for SDR it was suggested me to build or buy an antenna tuner.

**Since maybe it was not clear to everybody, I'm designing an antenna tuner for reception, not transmission.**

Searching around I concluded that most designs are variations on two main ideas.

The first is presented, among others, in a nice video by Stan Gibilisco but applies to wire antennas, whereas I would like to have a loop or dipole antenna.

The second is presented here although is designed for transmission and not reception.

As far as my understanding goes, the one from Gibilisco is essentially a tank circuit defined by L and C that can be tuned to a specific resonant frequency and the inductor is used for impedance matching with the radio.

*The other is a series LC circuit (T-network) but I don't understand why a second capacitor is needed. There is a sort of explanation on the link but I can't wrap my head around it.*

Furthermore I would like feedback on what I'm thinking of building:

The loop (about 1m diameter) is placed outside and is directly connected to a 1:1 current balun (ferrite ring) that feeds to a coax cable going inside. The variable capacitor (50-1000pF, two gang connected together) is in parallel with a rotary switch that can insert different inductors to have different tank circuits for different bands. A variable inductor is in parallel with the tank circuit and gives the impedance matching for the radio (since I don't have one or I will need to buy one this will be inserted later in the circuit).

1. Is it a sensible design?
2. If 1., is the value of the last inductor (the "matching" inductor) relevant?
3. Is the balun going to change its transformer ratio (that right now is 1:1) when different inductors are switched in the circuit?

**4. Related to the second design (the VK5AJL design), why there are two capacitors? Wouldn't a L or tank circuit also work?**

## Answer (score 4, by Marcus Müller)

So, yes, to tune a resonant antenna, you'll need an adjustable capacitor or inductor. You'd usually go the capacitor route, since adjustable caps are smaller, cheaper, and more exact, usually.

Bonus: There's *electronically* variable capacitors! They're called *varactors* or *varicaps* (or just *variable capacitance diode*), and they're a very mature (read: old & well-tested and used everywhere) and thus, cheap, method of tuning receivers.

You probably have heard of what a diode does in reverse bias: it doesn't conduct. Of course, that means that there's then two conductive pieces isolated from each other. Since the blocking layer is relatively thin in a diode, these work as a capacitor. By changing the voltage bias, you can make that layer thinner or thicker, and thus, you can change the capacity of that "accidental" capacitor with a DC voltage. Awesome!

When you design a diode for exactly that purpose, you can make sure that this effect is very well-controlled. These diodes then are sold as varicaps/varactors.

http://www.radio-electronics.com/info/data/semicond/varactor-varicap-diodes/circuits.php has a few very minimal circuits illustrating the usage of varicaps. The back-to-back configuration is what you usually encounter:

Now, when you look at a typical *small loop* (that's actually a specific term for an antenna that is *small in comparison to the wavelength*, not generally for *small* antennas) antenna, you'll notice it's usually simply a loop, in parallel with a capacitor.

Now, a loop is a coil is an inductor. Inductor in parallel with capacitor makes resonant circuit. The frequency of resonance is

$$ f = \frac1{2\pi\sqrt{CL}}$$.

L scales with size and length of the coil, and C is usually made adjustable. Thus, in the place where in the classical small-loop antenna you'd find the manually adjustable capacitor, you could place the adjustable capacity circuit I mentioned above. Battery operation is a good idea here, for both noise and potential separation reasons; that doesn't mean you couldn't also use a bog-normal 230 V -> 12 V transformer, rectify the resulting voltage, smoothen the hell out of that voltage and then add a simple voltage divider or adjustable voltage regulator to drive the varicaps, *as long as everything float* relative to your receiver – you'll be the ground of your voltage source to one end of your receiver coil, and you don't want that to be "accidentally" connected to real ground.

Regarding practical varicaps that you can buy:

well, look in the places where you'd buy electronic components. I've got good experiences with Mouser, shipping was 5–6€, I think. The BB 640 series (datasheet) looks like a good match for you – nearly 20 times the maximum capacity than minimum capacity means that you can change the resonant frequency over a range of $\sqrt{20}$ (see above formula for resonant frequency). If the maximum achievable capacity is too low for you, just put multiple in parallel.

Just throwing together a few numbers: I looked for an online one-turn loop inductance calculator. Found it, and put in a radius 0.5m loop made of 0.5mm diameter copper wire. Got a 2 µH inductance.

Then I said, ok, let's do hundred turns of that. We'll end up with 200 µH inductance. I'm neglecting nonidealities a bit, so we'll throw in a security margin of 50% afterwards.

Now, according to

$$ f = \frac1{2\pi\sqrt{LC}}\implies C = \frac1{(2\pi)^2 f^2 L}$$

and plugging in our L = 200 µH and f = 150 kHz, we get a maximum needed C of –including some margin– 6 nF.

For f=1 MHz, we'd need 0.13 nF = 130 pF.

That's bad news since 6 nF is 85 times the maximum capacity of the BB 640. That means you'd either need

- 85 parallel pairs of BB 640, so 170 BB 640 in total,
- a lot more turns on our coil (which isn't the worst solution, by any means!), or
- go up in frequency.

We see that f contributes *square-inversely* to the needed capacity. So, if we double the frequency we want to reach, we need to take one fourth of the capacity. Since our reliable capacity range is 19x, we can only accomodate frequencies of ca 4.2x the minimum frequency.

We can, however, switch capacitors in and out of our system – and that allows for higher frequencies, should we need them! Lower frequencies need linearly more turns of coil or linearly more varicaps.

You bring up the adjustable air capacitor – of course, that's the easiest solution here, but judging from the mini-whip, I was assuming you'd be looking for a non-mechanical, remotely operatable system.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/8963/antenna-tuner-design, by Luca, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
