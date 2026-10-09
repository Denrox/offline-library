# How to detect common-mode currents or “RF in the shack”?

*Tags: rfi, grounding, antenna-construction, equipment-design, testing · score 20*

## Question

Let's say we already know that if [your antenna is not suitably constructed or connected](How%20to%20reduce%20RF%20in%20the%20shack%20when%20using%20vertical%20HF%20antenna%20%28no%20radials%29.md) then you can get [current on the shield of your coaxial feed line](How%20do%20I%20prevent%20radio%20signals%20from%20tripping%20a%20GFCI.md) which will flow through the shielding/grounding of your equipment, becoming “RF in the shack”, and that this should be avoided for safety, transmit efficiency, and to avoid interfering with electronic equipment.

If I am not merely connecting together prebuilt equipment, but perhaps constructing an antenna/ground/balun system, **how can I measure this phenomenon, so as to determine whether it has been eliminated**?

[One of the previous questions](How%20to%20reduce%20RF%20in%20the%20shack%20when%20using%20vertical%20HF%20antenna%20%28no%20radials%29.md) mentioned a “FS meter” (I assume field strength meter), but I have not heard of this being a typical part of a ham's test equipment. Can a regular receiver be used? Even if this gives uncalibrated readings, can a reliable “null” (i.e. detection of the lack of current) be obtained?

## Answer (score 15, by Phil Frost - W8II)

One way to tell is by its effects. Do you hear a garbled version of yourself in nearby speakers when you transmit SSB? Do GFCI outlets pop even though no one is being electrocuted? Does handling the transmission line give you RF burns when transmitting, or change what you hear when receiving? If you had these problems and now you don't, you must have been successful in reducing common-mode currents.

If you want a more objective measurement, it's easy to make some test equipment with things you probably already have.

#### snap-on ferrite detector

You can make a detector with a diode, and a current transformer from a snap-on ferrite, such as those used to snap onto cables for EMI suppression. This will work for HF, but at higher frequencies the loss in the ferrite will become significant. Higher frequency ferrites are available, but not usually as snap-on beads.

The component values are not at all critical. I've used a Schottky diode, but an ordinary 1N4148 will also work with reduced sensitivity.

I've made R2 small to maximize the current through the meter. If you are measuring larger currents, or have a very sensitive meter, increase R2.

I just use my digital multimeter, and left the components hanging off the ferrite. It's ugly, but effective. Keep the lead lengths short. The long meter leads are fine because the RF has been rectified to DC by that point.

This device can be roughly calibrated by measuring the current through a known load. I put two half-watt, 100 ohm resistors in parallel, soldered them onto a connector, and plugged them into my transmitter as a 50 ohm dummy load. I set the transmitter power to minimum, clamped the ferrite around the resistors, and keyed up briefly. 5 watts into 50 ohms should give about 316 milliamps, and I read about 3 milliamps on the meter.

The non-linear diode will make the relationship between actual and measured current not linear, but that's good enough for a gross calibration.

#### other ideas

All kinds of devices can be used as detectors and probes.

An oscilloscope can work: try simply laying the probe next to the wire being measured, or making a loop probe. Put more turns in the loop for more sensitivity.

A 2nd radio works also, without an antenna, or with a dummy load to reduce sensitivity.

#### making the measurements

Set up your probe. Transmit, and watch your detector. The strength of the signal it detects is proportional to the strength of the common-mode current. For long wires, take measurements at a few places: there may be standing waves with high impedance (low current) and low impedance (high current) nodes.

Considering reciprocity, if you can measure common-mode currents in a thing when you transmit, then that thing is also helping you to receive. Either isolate these things from the antenna, or make sure they are noise-free. Insufficiently isolated feedlines, and digital electronics injecting noise into home wiring are the biggest offenders.

## Answer (score 6, by De Bohannan KC5ULU)

Another way to detect current on the outside of coax is to run your hand up and down the coax wile an analyzer is connected , if you see a fluctuation on the meter then current is following on the outside. On vhf I built sleeve chokes to remove it with great results. KC5ULU

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1271/how-to-detect-common-mode-currents-or-rf-in-the-shack, by Kevin Reid AG6YO, Phil Frost - W8II, De Bohannan KC5ULU. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
