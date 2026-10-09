# Understanding coax impedance

*Tags: feed-line, coaxial-cable, impedance · score 17*

## Question

I keep doing research, and trying to grasp it, but when it comes to RF impedances, and coax, I still have trouble trying to grasp it.

So first, I think you have to have a 50 ohm coax for a 50 ohm transmitter to keep the impedances matched. I think I also need a tuner to make the antenna look like a 50 ohm resistor.

After trying really hard to understand, I still don't know what "50 ohm coax" means; I know it's not 50 DC ohms in any way, but when RF is added, I just get totally confused.

Second, people are always like "OMG DON'T USE 75 OHM", but then they use 300 ohm ladder line!?! I understand that they use a tuner to match the 300 ohm, but why wouldn't a tuner work for 75 ohm?

Then there's connectors. Why would a little piece of metal screw have that much effect on the antenna, and how can a connector have an ohm rating at all?

## Answer (score 8, by Kevin Reid AG6YO)

It looks like you're looking for an intuitive, practical understanding rather than precise definitions, so I'll see what I can do with that, with my own recent learning.

The reason you care about impedance matching is that *impedance mismatches cause the signal to be partially reflected* — some of the energy is going the opposite direction than you want it to go. For transmission, this results in excessive voltage at the transmitter output, which can damage solid-state transmitters; in any case, even if the reflected component is reflected back again (standing waves), you have additional loss and effective multipath propagation (some of the signal took longer to exit the system through the antenna or receiver).

The characteristic impedance of a transmission line depends on the space between the conductors — its shape, and what it is filled with (the dielectric). A connector needs to be (electrically) *shaped like* a simple continuation of the lines it joins, otherwise it's mismatched just like a piece of transmission line of a different characteristic impedance. This is also why you should avoid sharply bending coaxial cable — it distorts the cable and causes a change in impedance.

Why ohms? Lots of ways to describe this, but a good enough one is this: in the simplest case, an impedance is like a resistance, and resistances are measured in ohms. A resistor — a dummy load — is a simple load which has a constant impedance at all frequencies. Two facts:


If you connect a resistor of a certain impedance (resistance) to the end of a transmission line with the matched characteristic impedance, then there will be no mismatch and no reflections, and it will be measured as 50 ohms no matter the frequency. This is *termination* of a transmission line.


If you had — theoretically speaking — an infinitely long transmission line, and you connected a DC ohmmeter to it, the ohmmeter *would* read the line's characteristic impedance. You can see this as being sort of like the reason we want to match impedances: so that the signal goes into the line without having to consider what is on the other end.

(If you have a transmission line with mismatches — say, an open circuit at the other end, or damage in the middle — then you can use the reflections to measure exactly how long the section before the reflection is. A *time-domain reflectometer* is an instrument for doing this. There's a nifty video about how you can see this effect with a signal generator and an oscilloscope that I haven't found again.)

That's *why*; everything else is *how*.


There's nothing wrong with using 75 ohm coax in particular. It's just that it is conventional for amateur radio equipment to be designed with 50 ohms characteristic impedance, so if you substitute 75 ohm coax without doing anything else you will have mismatches.


The reason for using 300 ohm balanced line is that it is a good match for certain types of antennas, and has lower loss than a typical coaxial line (because the EM field passes through more empty air than solid dielectric materials). This allows you to avoid placing a matching device at the antenna itself; instead, you must do so at the transmitter (assuming the transmitter has a 50 ohm output).


When a load has a different impedance from a connected transmission line, the input end of the transmission line will appear to have a different impedance than its characteristic impedance. Furthermore, antennas have frequency-dependent impedance. Together, these are one of the main reasons why antenna tuners are used, as opposed to simply designing the entire system around fixed impedances: to increase the band over which an antenna can be used without excessive mismatch at the transmitter. However, even with a tuner, this results in *standing waves* on the transmission line, which increase loss in the line.


Specifically designed changes in impedance can be used to produce specific effects, including impedance matching and baluns. However, such devices only work in a narrow band because they have to be a specific length relative to the wavelength of the signal. Conversely, if you want wideband performance you avoid mismatches so that the characteristics of the system don't change with frequency.

The main things I have *not* mentioned here are is how impedance corresponds to a ratio of current and voltage (in accordance with Ohm's Law), and the concept of *reactance* (or complex impedance). These matter for understanding the behavior of systems with mismatches; equal or matched impedance is a simple case which results in behavior which is independent of frequency and length of the line.

## Answer (score 5, by Phil Frost - W8II)

Here's the problem: information can only travel at the speed of light. So, say you have a resistor, connected to your ohmmeter by a pair of very long wires. When you connect the ohmmeter to the wires, it applies some voltage, but how much current flows? When this voltage is first connected, it sets off a wave in the electric field, but that wave hasn't yet reached the resistor. The resistor doesn't "know" there's an ohmmeter, and the ohmmeter doesn't yet "know" there's a resistor. So how much current flows in the instant the ohmmeter is connected?

The *characteristic impedance* of a transmission line answers this question. If a transmission line has a 50Ω characteristic impedance, it means that for every 50V you apply, you get 1A. An ohm is a volt per amp ($R=E/I$ and $\Omega=V/A$), remember.

Eventually the wave set up when the ohmmeter was connected to the wires reaches the resistor at the end. If the resistor has the same impedance as the transmission line, then the current that flowed into the line initially works against the resistor to make the same voltage that the ohmmeter applied. Now voltage is the same throughout the circuit, and everything is in equilibrium. That was easy.

If the resistor at the end has a different impedance than the transmission line, then the current will work against it to create a *different* voltage than the ohmmeter initially applied. The ohmmeter at this point is displaying the impedance of the transmission line, not the resistor at the end. Since the voltage at the resistor end is now different than everywhere else in the line, another wave is set in motion, propagating back to the ohmmeter. If the ohmmeter is maintaining a constant voltage, then when this reflected wave arrives, the current at the ohmmeter will have to change (and consequently, the measured resistance on the display changes) to keep the voltage at its end constant. Thus, another wave is sent towards the resistor.

These reflections go back and forth, each time getting closer to the equilibrium solution of dictated by the resistor on the end. You don't usually notice it because it happens at the speed of light. Try playing with a transmission line simulator to see what happens on a more observable timescale.

It doesn't matter if the thing at the end of the example above is a resistor, or another transmission line, antenna, or a connector. Each of these things, in fact *anything* that can have an electric field, has a characteristic impedance, and if this impedance doesn't match that of the transmission line, a wave is reflected back.

Thus, there's nothing wrong with 75Ω coax, as long as everything else is 75Ω, or you have added matching devices where there are impedance changes. This is exactly what is done when 300Ω ladder-line is used. The advice against using 75Ω coax is simply because cable TV is usually a 75Ω system, so people have a lot of it around and might ignorantly think it looks the same, so it should work the same as 50Ω coax.

## Answer (score 3, by Adam Davis)

Transmission line theory is complicated by many factors. Here's one simplified explanation that might help you understand a little better what you're asking about.

When you send a wave down a line, it doesn't appear instantly on the other end; the electrons push each other, and in a measurable, finite amount of time the wave is present on the other end of the line.

The line has a capacitance and an inductance, though, so when you start sending the wave, the cable's capacitance and inductance absorb and release that energy as the wave travels down the line.

Since all lines feature capacitance and inductance, then we have to treat them as part of the overall circuit. If we ignore them then we may lose some of our wave, or it may be altered in some undesirable way.

We could quantify the capacitance and inductance separately, and then call each cable according to those parameters, but we've come up with a simplification called impedance.

If you send a fast wave down the line and measure the voltage and current, then apply Ohm's law, regardless of what's connected at the other end of the line, during the fast transition you will see 50 ohms of load on the line for the wave. This is the line's natural capacitance and inductance reacting to the AC wave you sent.

If nothing is attached to the other end, or the other end is shorted out, the wave will be reflected back.

If you attach a 50 ohm resistor on the other end, then the waveform will be completely consumed by the resistor. This is because the cable's capacitance and inductance only consumed enough current at the transmitter's voltage and waveform type to provide the wave at that same current at the output. Since you put it in at a certain voltage, and it consumed enough current for a 50 ohm load, then the voltage, and more importantly waveform shape, are preserved at the output.

If you put too small a resistor, then it'll eat the current too quickly - faster than the waveform is actually traveling on the inductor/capacitor chain that the line is made of, and this will distort the waveform and voltage, and will reflect some of the waveform back. You'll have lost energy, not everything you sent on the line will have been consumed at the other end.

If you put too large a resistor, then it won't eat the current fast enough, and again the voltage and waveform will be altered, and again some of it will be reflected back.

This leads to two problems - energy loss, and changed waveform. So if your transmitter is designed for a 50 ohm impedance, you use a 50 ohm cable, and a 50 ohm antenna, then the majority of your transmitter's energy will go into the antenna, and will be radiated into the air, with the waveform shape the transmitter intended.

If you instead replace your 50 ohm cable with a 75 ohm cable, the cable will consume less current than expected, which alters the way the waveform travels down the line, and when it's received by the 50 ohm antenna, not all of that energy will be properly coupled into the antenna.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1291/understanding-coax-impedance, by Skyler 440, Kevin Reid AG6YO, Phil Frost - W8II, Adam Davis. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
