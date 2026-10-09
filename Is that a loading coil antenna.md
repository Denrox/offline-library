# Is that a loading coil antenna

*Tags: antenna, antenna-theory, antenna-construction, receiver, uhf · score 4*

## Question

I came across one WiFi receiver of my wireless keyboard and after opening the USB receiver, I saw a strange looking printed antenna on the PCB.

It's like a series of square waves printed on the PCB.

Is that a loading coil antenna or something else?

I have attached the snapshot of the PCB.

## Answer (score 8, by Marcus Müller)

This is a variant of an inverted-F antenna.

"Loading coil" is a term *usually* used with dipole antennas (and slight variations thereof). The idea is that you "load" the antenna to change its resonant frequency with something "small", "discrete" added to the antenna construction.

As you can see, the meanders here are *not* small compared to the antenna length.

Transferring terminology between different types of antennas (and different approaches to antenna design) is usually a bit of a futile attempt:

I saw a strange looking printed antenna on the PCB.

Together with the rectangular patch, the inverted-F is probably *the* most common antenna type for microwave PCB antennas. So, I wouldn't call it "strange", it's just not like the antennas you encounter built from masts and wires for much lower frequencies.

This highlights why it's bad to try and transfer terminology from one antenna type to the other, rather than understanding the "target" antenna type.

Here, sure, the meander also serves change the resonant frequency by electrically changing the length of the "horizontal arm" in your picture, but among a lot of other things, it also completely changes the geometry of the antenna, bringing the arm closer to the ground plane, shifting phase centers and directions of beams … none of which could be described as an effect of "inductive loading" of the antenna.

For small PCB antennas like these, a lot of the simplifications made when explaining large antennas *do not hold*. The relative width of the traces, the thickness of the insulating material, the surface quality of the trace don't matter to an HF antenna, but they are what define the inverted-F.

The most important simplification for calling something a "loaded" antenna is that you can identify the "loading" element, and that element must be a thing that has a concrete place on the antenna emitting element. Here, the emitting element is *not* the horizontal trace alone, it's the aperture between the trace and the (green) ground planecloser to the connector in your photo. An inverted-F is, in radiation mechanics, closer to a slot in a waveguide (a *slot antenna*) than to a monopole! Hence, this is more like shaped slot than a coil-loaded antenna.

Why do I talk about **terminology** so much, if the purpose (meander causes inductance, causes change in resonant frequency) is the same?

Because for all practical purposes, you can't just say, "this meander is X pH, so it changes the resonant frequency by Y Hz when we add it to the antenna". The design process will have to incorporate the resulting change in distances; where you can add loading to a monopole HF antenna just fine and get the result you were expecting, this doesn't work here. *Terminology* is useful when it describes how you can *understand* and *use* some concept – but the "loading coil" terminology implies properties that just don't apply here.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/23058/is-that-a-loading-coil-antenna, by Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
