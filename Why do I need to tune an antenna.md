# Why do I need to tune an antenna?

*Tags: antenna, impedance, antenna-tuner, impedance-matching · score 21*

## Question

I've heard that when an antenna is set up, it needs to be tuned to reduce reflective power back into the radio. Is this always necessary, and if so how would I go about tuning it?

## Accepted answer (score 14, by user)

There are two different parts to antenna tuning: **transmission line impedance matching** and **resonance**.

The antenna is at *resonance* when it presents a purely resistive load to the transmitter. That is, the reactive component of the load is 0: there exists no inductance or capacitance in the load.

However, *resonance says nothing about the value of the resistive component of the load*. Usually, you also want to reduce the impedance mismatch, because an impedance mismatch causes power to be reflected at the point of the mismatch. Most amateur radio equipment is built to expect a resistive load of 50 ohm impedance, which is the characteristic impedance of most coaxial cables used in radio applications.

An *antenna tuner* or ATU doesn't actually tune the antenna; it provides a matching network. On one side the transmitter sees a nice, orderly, purely resistive 50 ohms. On the other side is an unwieldy antenna, the impedance of which at the given frequency can be anything from purely resistive at 50 ohms to some odd-ball combination of weird resistance and either inductance or capacitance.

This is done by introducing either capacitance or inductance into the feedline, to cancel out the corresponding part of the load impedance. For a fixed antenna installation on a single frequency, you can even determine appropriate component values and use fixed-value components to make up such a matching network, but that lends itself poorly to the applications in which one wants to move frequencies, antennas and so on. *As a matter of fact, that is the approach taken by many electrically short antennas* and it comes at the cost of reduced antenna bandwidth (because the fixed matching network can only compensate, with an acceptable SWR, within a limited range of frequencies).

*The SWR* or Standing Wave Ratio is related to the (mis)match in impedance. This means that your perfectly resonant antenna which happens to present a nice, clean, purely resistive 150 ohms (pulling a number out of thin air here) at the feedpoint and at a given frequency will give you a 3:1 SWR against 50 ohm coax, *despite being at resonance.*

Also, even with an ATU, it's important to remember that the reflected power must go somewhere, and in this case, at least some of it is being dissipated as heat rather than radiated as RF. While you aren't likely to do much harm with some reflected power from an over-the-counter 100W transceiver, this can be a serious consideration if you are running a high-powered transmitter and/or a large amplifier.

## Answer (score 5, by Paul)

Your transmitter has something called an "output impedance" and expects to be loaded with this impedance. The standard is 50 ohms. You don't need to look up the output impedance, it was standardized and anything made in the last 50 years will expect 50 ohms.

The 50 ohms the tranmitter expects is measured at RF frequencies. Many antennas look like short circuits (a loop) or open circuits (two independent wires, like a dipole) at DC, but change at radio frequencies.

Modern transceivers often include an SWR meter. SWR, or standing wave ratio, should be 1 when there is no reflection. Many transceivers will tolerate an SWR of up to 2.0, but the closer this number is to 1.0, the better.

You can also buy an antenna analyzer as a stand alone instrument to measure impedance and SWR.

A dipole antenna (two wires, each 1/4 wavelength, travelling opposite directions) is between 50-70 ohms for its center frequency and can often be used as-is. But you should still check it with an SWR meter or the SWR meter in your radio.

Antennas that do not present 50 ohms require a circuit to transform the antenna impedance, whatever it is, to the 50 ohms expected by the transmitter output. This circuit can sometimes be made by adding funny shaped parts onto the antenna -- not just any funny shaped parts, though -- this is a matter for serious engineering. Other times the transformation is solved by a box called an "antenna tuner", which remains permanently in place. You can find both manual old-timey antenna tuners and automated tuners for HF. For VHF and up, the antenna usually has an adjustable component like a slider.

## Answer (score 2, by Bill - K5WL)

Every location in which you install an antenna will be slightly different. For example there will be different characteristics of the soil, different nearby structures and plants, different heights above ground, different numbers of radials installed, and so on. Each of these factors affects the performance of the antenna, so final adjustments must be made at the site of installation. For the very best performance it is necessary.

The best tool for this is an antenna analyzer, but you can get by with the SWR meter on a transmitter. The important part of this process is to have the antenna in its final operating location when tuning, which might involve raising and lowering it multiple times.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/55/why-do-i-need-to-tune-an-antenna, by berry120, user, Paul, Bill - K5WL. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
