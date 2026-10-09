# Does a 1/2 wavelength end-fed antenna need a good RF ground?

*Tags: antenna-theory, end-fed-antenna, counterpoise · score 8*

## Question

I was searching for *DIY end-fed antenna.*  
Some of the articles I found say that for a 1/2 wavelength end-fed I need a "small to no counterpoise" (with a lambda*0.05 m counterpoise), but some other articles say that I need "a good RF ground in close proximity to the end of the antenna".  
Initially, I thought that a good RF ground is required for a random wire antenna but not for 1/2 wavelength one. But I just got an answer here saying that it is needed.  
What is the truth? What type of end-fed requires a "small to zero counterpoise"?

## Accepted answer (score 4, by Sterling N0SSC)

No, it is not needed, but it can improve the antenna system.

An EFHW is simply a half-wave length of wire and a matching device, and that's it. Counterpoises are commonly added to shunt common mode reflections when operating outside of the wire's resonant frequency to avoid RFI issues ("RF in the shack"). An RF ground (defined here as either very conductive ground, or a radial or grid system of wires beneath the antenna with a radius at least 1/4λ from the antenna center) isn't required.

However, that ground system improves the conductivity of the ground, which can have a positive effect on the radiation pattern, but little to no beneficial effect on the VSWR. It can also serve the purpose of the counterpoise if the ground side (shield) of the coax is connected to it near the antenna's feedpoint, but that's far more effort than it's worth.

## Answer (score 12, by hobbs - KC2G)

An end-fed half-wave operates on a principle that, for lack of a better name, I will call "voodoo".

If you look at the standing wave on a half-wave element in isolation, you see that the center is the point of highest current and lowest voltage (therefore lowest impedance), and the ends are the points of highest voltage and zero current (therefore infinite impedance). The factors that make the impedance *less* than infinite, and therefore make it possible to feed the antenna at all, are the same parasitic/environmental factors that we usually ignore in a quick-and-dirty analysis of an antenna because they're unpredictable and hard to quantify — things like stray capacitance with nearby objects, losses in the matching system, the fact that things we model as zero size actually have physical extent, and (especially) interaction with the feedline. A great many end-fed systems are dependent on feedline radiation to really work; since feedline radiation is generally a cause of RFI problems, operators try to use chokes to raise the common-mode impedance of their feedline, only to find that the feed impedance of their antenna has gone up as well, and they can no longer get a good match.

These issues lead to all sorts of creative solutions to try to make end-feds behave, and one of the simplest ways to make an end-fed behave less like an end-fed and more like a dipole is to make it less of an end-fed and more of a dipole. By adding a "counterpoise" to an end-fed, you are adding some kind of an element on the "other side" of the feedpoint. In other words, you're moving the feedpoint away from the end. In other other words, you've turned your end-fed into something more like a (very) off-center fed dipole. The current at this new feedpoint is greater, the impedance is merely *large*, and with proper matching, power will actually *want* to go into the antenna. This makes the antenna's behavior more predictable based on its own characteristics, and less sensitive to where it's placed, how it's fed, and other "voodoo" factors.

## Answer (score 5, by Glenn W9IQ)

The EFHW (end fed half wave) needs to be classified as a specific case of the class of end fed wire antennas. The name is even a bit of a misnomer since the EFHW is often operated on multiple bands and therefore is no longer a half wave antenna. And due to the implementation details, the antenna is in fact often not even a half wave at its design frequency.

But let's start with the general situation of a half wavelength long piece of wire. As long as it remains a half wavelength long, the gain and radiation pattern of the antenna is the same even if we feed this half wave wire at various points along its length. At nearly every point that we choose to feed it, the antenna will ***not*** be resonant - that is to say at nearly every feedpoint, there will be reactance. Technically speaking, even a center fed half wave antenna is not resonant - we shorten it slightly from a true half wavelength in order to make it resonant when center fed.

When you feed a half wave antenna in its center, the antenna feedpoint is balanced - that is to say that each half of the antenna has the same impedance and so the same current would naturally flow into each half of the dipole. At any other feedpoint, the two parts of the antenna exhibit different impedances which results in different effective currents in the two sections. This can present challenges as it relates to the feed system. The corrective action is often a current balun that "forces" the same current into each part of the antenna in an effort to reduce the inevitable common mode current on the feedline.

The extreme case of imbalance when feeding a half wave antenna occurs when it is fed from the end. The impedance at the end of the antenna will be quite high - typically 5,000 ohms or more. To tame this high impedance, an impedance transformer of at least 9:1 and as high as 49:1 is often used. This transformer is a simple autotransformer so it can do nothing to reduce common mode current on the feedline. It also tends to be quite lossy when used over a wide frequency range. This helps improve the SWR due to the lower Q but this comes at the expense of reducing the efficiency, and thus gain, of the antenna.

What is often overlooked in an end fed antenna design is that the current that is present on the half wave element needs a method of returning to the transmitter in order to allow the antenna to efficiently radiate. There are erroneous claims on the Internet that the autotransformer somehow provides this path but that is simply not true. The autotransformer provides a return path for some of the current on the feedline (in the form of a reflection) but not for the current on the antenna.

Yet we know that an EFHW "works" to some degree as many people have success with this style of antenna - so where is the path for the return current? The answer is highly dependent on the installation. In most cases, the external braid of the coax provides the return path. When this happens, the braid is actually part of the radiating antenna. So it transpires in this case that the claimed half wave antenna is no longer a half wave at all! This also means that the antenna pattern is likely not what would be suggested by the spacial orientation of its half wavelength piece of wire.

In other installations, if the shield connection of the autotransformer is directly grounded to an earth ground system, the return path will largely be through the lossy earth (although some shield current can still exist). Due to the lossy earth, the antenna system efficiency, and therefore gain, is reduced.

The third installation variation is to install counterpoise wires that drop from the elevated transformer down to the ground and then run along the ground. In this case, these wires will typically also form part of the radiating antenna but at least a good part of the return current comes via these wires instead of the lossy earth.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12391/does-a-1-2-wavelength-end-fed-antenna-need-a-good-rf-ground, by Hose Dias, Sterling N0SSC, hobbs - KC2G, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
