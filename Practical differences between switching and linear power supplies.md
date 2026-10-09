# Practical differences between switching and linear power supplies?

*Tags: dc-power, power-supply · score 6*

## Question

Power supplies for ham radio equipment (and other equipment of course) seem to come in two flavours: switching and linear. The switching gear tends to be cheaper and smaller as well as more efficient.

My understanding is that switching supplies are more prone to creating RFI, but otherwise there is not much functional difference.

Is that the gist of it, or is there more? From the user's perspective, what is the advantage of one versus the other?

## Accepted answer (score 6, by Kevin Reid AG6YO)

The only reason *to* use a linear power supply is to reduce electrical noise (or if as an exercise in electronics you want to build your own power supply without using integrated circuits, or if you need your equipment to double as doorstops).

It is also quite possible that if you do want to reduce noise, you will be better served by adding filters to, or upgrading, other power supplies in your house than by choosing a linear supply for your transceiver. (For example, my apartment's HF noise level went from useless to tolerable by winding the DC cables for my internet equipment (cable modem and WiFi AP) several turns around ferrite cores. The noise from the Alinco switching supply I run my transceivers from is unnoticeable compared to everything else.)

Details on some of the factors:


**Noise.** A switching power supply inherently generates high-frequency signals as it, well, switches. The frequency and power of the noise that is seen at DC output — or the air — depends on the design of the supply. Many cheap switching power supplies as seen in consumer electronics will radiate significant noise compared to one recommended for amateur radio use.

Naively looking at the typical noise frequencies (in the kHz) suggests that this noise may be a problem for HF operation but not typically for VHF, and this is *generally* true, but remember to consider any intermediate frequencies used by your gear, and also the possibility of interference with AF signals (such as your microphone).


**Efficiency.** A linear power supply inherently wastes some energy — it takes the (usually) AC line voltage, reduces it to an unregulated lower voltage (still higher than the desired output) with a transformer, rectifies it, then regulates it precisely using a **linear regulator**. A linear regulator is effectively a variable resistor in series with the output that “drops” the excess voltage — generating heat. Therefore, linear supplies generate lots of heat and require large heat sinks. Switching supplies still generate heat since they are not made of nonexistent ideal components, but much less.

If your “ham shack” is not air-conditioned, you will directly appreciate the efficiency of a switching power supply.


A switching power supply can operate at a much larger range of input voltages. This doesn't mean just not having to pick 110V/220V; it also means that it can compensate for significantly lowered input voltage by drawing more current from the input, whereas a linear power supply will stop regulating because the fixed transformer ratio produces too low a pre-regulation voltage. This is usually not that relevant.


Size and weight, obviously enough.

## Answer (score 3, by Marcus Müller)

You've pretty much hit the nail on it's proverbial head:

Both are power supply *architectures*, and as such generally fulfill the role of providing a constant-as-necessary voltage source (or current source, for some applications, but we're most likely talking about voltage sources).

Now, you can imagine a linear power supply simply as a self-adjusting resistor. It adjusts its resistance exactly as much as to drop enough voltage so that the voltage between its output terminal and its ground terminal is constant.

Of course, that means that $V_{drop}\cdot I_{output} = P_{wasted}$, i.e. all that voltage drop is waste heat. You hence simply can't do that for overly large voltage drops or overly large currents, because *things get hot*. Things getting hot means you need beefier voltage regulator ICs and larger heat sinks. That's expensive. For large voltage drops, and security critical things, you simply can't do that, because no (affordable) semiconductors exist that support both the power and sufficient isolation.

Now, a switch-mode power supply works by having an *energy storage* from which it takes small portions of energy. In a typical topology, this means that you have your input voltage over a coil, which of course starts to build up a magnetic field. Then, you switch the in- or the output off and on again, to bring the voltage across that coil onto your target output voltage. The energy taken by the output in shape of current is taken from the coil's magnetic field, so that the amount of switching on and off needs to accomodate the target voltage and the amount of current drawn, and the fact that a higher input voltage can "recharge" the coil faster.

With a bit of cleverness, you can, that way, even step up voltage! Something that's impossible to do with linear power supplies.

If you look at the power wasted, there theoretically is zero: energy is just being converted from input electrical current to magnetic field and back to output current at a different voltage, and all these processes are theoretically lossless.

In practice, you of course get the resistances in your coil's wires and the losses in the coil's core as well as resistances in the switch (typically, a transistor), so things are maybe 80% to 98% efficient – but that's way, way more efficient then let's say converting 1A of current from 12 V to 5V:

With a linear supply $I_{out}=I_{in}$ (plus losses), so $P_{in}=V_{in}\cdot I_{in}=V_{in}\cdot I_{out} = V_{in}\frac{P_{out}}{V_{out}}=\frac{V_{in}}{V_{out}}P_{out}$, with a switch mode supply $P_{out}=P_{in}$, only! Which means that the linear supply scheme uses $\frac{12}5=2.4$ times as much power!

Regarding noise:

Of course, switching necessarily means that you switch a current on and off, and you'll see that on the output side of your coil, as *ripple*. Typically, a smoothing capacitor takes the job of reducing that ripple to a degree sufficient for the electronics supplied to work.

However, reducing doesn't mean getting totally rid of, and you'll need to design a smoothing stage that fits your need: if your need is just driving a microwave oven's clock display, ripple-rich (hence, noisy) output voltage doesn't matter to you at all. If you're trying to pick up some weak transmission on a frequency close to the frequency your switch mode supply works at (or one of its harmonics), you'll have a harder time.

In professional lab and SDR equipment, which still often is cost-, size- and power-restricted, you'll often actually find a cascade of power supplies; for example:  
A set of switchers to step down the 6 to 9 V (which usually comes from a switch-mode "wall wart", converting grid to something safe for humans to touch) input to 5 V, 3.3 V and 1.8 V; the last voltage to be converted to 1.2 V through a low-drop linear supply for the high-speed digital logic and memories, 3.3 V for direct usage by the digital interface ICs, which don't care about noise nor very exact voltage overly much, and 5V to be regulated with another set of linear supplies for all the analog signal chain, with plenty of RC low pass filters in between the switching power supply, the linear regulator, and if small and constant current draw allows, between linear regulator and the device (amplifier, mixer, adjustable attenuators, microwave switches...).

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10293/practical-differences-between-switching-and-linear-power-supplies, by Jim MacKenzie VE5EV, Kevin Reid AG6YO, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
