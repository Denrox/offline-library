# Antenna Design for specific directions

*Tags: antenna, antenna-construction, wire-antenna, physics, loop-antenna · score 4*

## Question

I am designing an antenna for a device and was hoping to gain some insight in the correct design direction for the antenna.

**The Idea:** A receiver & antenna that fits in a 6" diameter by 3" deep cylinder.

**Known:** Frequencies range from 162.400 to 162.550 MHz. The signal will not be coming directly from the top or bottom.

**Goals:** Design the “best” antenna I can given my knowledge of the direction the signal will be coming from, the size constraint of the enclosure and the frequency.

Any advice, recommendations, and/or help would be greatly appreciated. I am specifically interested in the physical layout/design of the antenna.(For example coil wire cylinder)

**Thoughts:** My gut feeling is to enclose the maximum area possible with the antenna. From my initial research the length is not as important as I had previously thought which lead me to start to ponder this even more.

**Notes:** I like math if you are so inclined :)

## Answer (score 2, by Kevin Reid AG6YO)

Given the shape and desired band, I think what you want is a small loop antenna. This would simply be a coil of wire wound in the shape of your cylinder, preferably with a capacitor wired in parallel to make it resonant at the desired frequency and match impedance to the receiver.

Small loops have the type of radiation pattern you are looking for (in the plane of the loop). What makes it a “small" loop is that it is small, both in radius and total length of wire, compared to the wavelength; we can see that a radius of 3 inches (0.07 m) is smaller than your wavelength of 1.85 m but I don't know whether it'd be better to make it even smaller than that. If the loop is too large, comparable to the wavelength, it will have the opposite of the pattern you desire.

Small loops are inefficient antennas not suitable for transmitting, which is why transmitters don't use them to avoid having long antennas sticking out, but since you are receiving that doesn't matter unless your desired signals are particularly weak.

They are commonly seen as antennas for AM broadcast receivers, either as external wire loops on a frame (oriented vertically to have some directionality; in your case, you would orient the loop horizontally because you are asking for an omnidirectional pattern), or very small internal “loopstick” antennas (wire coiled around a ferrite rod).

(Disclaimer: I have made no systematic study of antenna theory; I have never built a small loop antenna; there's probably some caveats I haven't mentioned. I'm writing this answer because I haven't seen a better one yet and I'm reasonably confident the basic idea is OK.)

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2198/antenna-design-for-specific-directions, by Josh Cox, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
