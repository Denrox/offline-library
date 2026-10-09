# How to design a Local Oscillator for a radio receiver?

*Tags: mixer, oscillator, inductor · score 4*

## Question

I have decided to design a Medium Wave radio with discrete parts which won't include much complex ICs or schematics . I am thinking of designing the radio in Heterodyne mode. Which requires an oscillator for resonance and mixture.

I think Hartley oscillator will be the best for a radio local oscillator.

The oscillator should oscillate between 550KHz to 2MHz with a 25 pf gang condenser. So, two 4mH inductors are required to setup a hartley oscillator.

I have 1mm (diameter) enamelled copper wire and a solenoid of 3mm diameter (screwdriver). I have used an online calculator to get the exact number of turns I will need for 4mH air core inductor. The calculator shows that I am going to need a few thousands of turns to achieve that specified inductance which seems way too much unworthy struggle for me.

I have some ferrite core inductors which have the same value of 4mH, which I need. But I read somewhere in the internet that Air Core inductors are the best for RF applications whereas ferrite cores have a huge amount of losses due to ferrite fluxes.

I have tried to find so many schematics about it online but none of the schematics actually define the number of the turns, coil diameter and solenoid diameter.

Maybe because radios nowdays use ICs for taking care of most of the things, other components like local oscillators and mixers have almost become passive and there is not much information available about them throughout the web.

So I am in need of some help.

So here are my queries...

1.

So should I develop the oscillator with ferrite core chokes? Or get myself to the table to turn an air core coil thousands of times?

2.

Can simple LC circuit be used instead of a Hartley oscillator?

3.

Do I really need to round up coils a few thousands of times or there is another better alternative?

Thanks.

## Accepted answer (score 5, by glen_geek)

A 25pf variable capacitor is unreasonably small to tune such a wide frequency span as 550kHz to 2000kHz. Oscillator design would be far easier if a larger variable capacitor were found - they ARE available.  
If a 25pf variable *must be used*, then there is a technique that allows a wide frequency range to be covered by a single LC oscillator. Such a technique is outlined by the **8640-jr RF signal source**. The requirement of this technique is that oscillator tuning range must cover an octave - that is: maximum frequency must be twice minimum frequency. Let's try a design to see what frequency is possible.  
If a variable capacitor has *maximum capacitance* of 25pf, what is its minimum capacitance that allows an octave frequency range? It is about 6pf. So capacitance range will be 6pf min to 25pf max.  
Some of that 6pf will be taken by stray capacitance from frame to fixed plates - how much depends on physical construction of the capacitor - we wish to minimize this capacitance, because the Hartley oscillator itself will add to this some capacitance of its own.  
The 8640 jr. Hartley oscillator is outlined below. It uses a much larger variable, but adds a smaller variable to set the upper frequency.  
This oscillator is designed to cover at least one octave span, from 13.6MHz to 31MHz. The big question is: could it be adapted to use a 25pf variable substituting for that big 365pf variable?  
C8 should be eliminated, because it violates our minimum requirement of 6pf. The designer actually started C3 at 2.5pf, but found amplitude was feeble at one frequency-end. Perhaps a 2.7pf could work here.  
C2 and C5 would also be left off.  
The 25pf variable substitutes for C1. Unfortunately, the 800nH inductor would now cause oscillation at a very high frequency, so a much larger inductor would be needed, but it should be built so its self-resonant frequency is as high as possible.  
A 5uH inductor combined with 6-25pf variable resonates from 29.1MHz down to 14.2MHz; barely an octave. Building it to achieve this range will be difficult, because of inevitable stray capacitance.  
This octave oscillator operates at a frequency far higher than needed. However, the trick used in the 8640-jr applies an amplified version of **RFout** to flip-flop frequency dividers. With five cascaded flip flops, 550 kHz can be reached. Three stages of flip flops covers 2Mhz.

Texas Instrument **High-speed CMOS Logic Data Book** suggests an alternative oscillator that covers much more than one octave frequency range. It's frequency is varied by means of a variable voltage (it is classed "voltage-controlled-oscillator" VCO):  
This 3-stage ring oscillator provides a square wave output that ranges fairly linearly:

- VCO control voltage 1.5V yields output frequency of ~ 5 MHz
- VCO control voltage 4.8V yields output frequency of ~28 MHz.

Its square wave output should not be an impediment for most types of mixers, although some mixers might want a smaller amplitude than 5V. Output can easily drive the flip-flop chain-of-5 directly. An approximate equation is given relating the control voltage to output frequency:  
$ F_{out} (MHz) = 5.8\times V_{control} $  
I believe that the 74HC00 DC supply pin #14 should also be connected to $ V_{control} $ , however note that the inverter stage should be powered from a fixed +5V DC supply - it converts the VCO's variable amplitude to a standard logic swing appropriate to drive the flip-flop frequency dividers.

## Answer (score 3, by tomnexus)

Your calculation is probably correct - at ~1 MHz, air core inductors won't be much use. You definitely need a ferrite cored inductor.

Don't be afraid of ferrite losses:

- At this frequency the loss will be quite small, in fact up to ~ 10 MHz you get a higher Q inductor *with* ferrite than without, because of the wire resistance. The limitation with ferrites is that they stop working at a fairly low temperature, so if you're designing a kilowatt antenna tuner, it might work better to have bare silver/copper wire.
- Inside the oscillator resonator, the Q isn't as important as in a matching filter, etc.

If this is a one-off project, I recommend going through your junk box, desoldering anything that looks like an inductor, or is called L3 or FB4, and measuring them. I've found a useful selection of low-loss inductors, 100 nH to 20 uH, in old modems, power supplies, computer gadgets, usually in their many power supplies. I test them with a NanoVNA over the frequency range of interest, [calibrate carefully](Measuring%20actual%20feedpoint%20impedance%20for%20a%20given%20frequency.md). Sometimes the inductors are macroscopic enough to be able to remove a few turns to reduce the inductance, which is nice. Round-cable ferrite cores, added later to solve EMC problems, may be less useful as the material is designed to be lossy, but try them too.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/22129/how-to-design-a-local-oscillator-for-a-radio-receiver, by CoderBittu, glen_geek, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
