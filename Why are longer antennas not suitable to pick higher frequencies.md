# Why are longer antennas not suitable to pick higher frequencies?

*Tags: antenna, antenna-theory, long-wire · score 9*

## Question

I know that the length of an antenna depends on the wavelength of the frequency it's trying to receive.

A higher frequency needs a shorter antenna and vice versa.

I can see that with a high frequency like 500 kHz, an antenna should be around 28,000 cm (280 m) in length, otherwise the EM waves are too long to resonate your antenna properly: *Dipole Calculator*

But I don't understand the issue with lower frequency antennas. Why can't the same antenna as above be used for a 900 MHz frequency? Doesn't the EM wave end up hitting the electrons somewhere on that long antenna?

Also, how come radios in cars can pick up AM 500 kHz frequencies with ease having such small antennas on the roof of the car? Their length is nowhere near 28,000 cm.

## Accepted answer (score 10)

This is sort of two questions, but they are related.

The first question asks why a car AM receiving aerial works to receive 500kHz when mathematically speaking the electrical length of a $1/4\lambda$ for 500kHz should be something like 143m.

The obvious answer is that receiving is different than transmitting. Broadcast AM stations use all sorts of clever tricks to get their megawatt signal out without burning up their finals, and all of them centre around providing that real or pretend electrical length of 10s of metres of antenna to blanket their area with enough energy so little bits of metal on receivers can be used to recover that energy and turn it into intelligence. Receiving antennas just have to be good enough to pick up the $\mu$w signal for the front-end to amplify it. Building your own station to *transmit* even a modest amount of wattage at lower frequencies would work great as an air and ground warmer if you used a little car antenna -- even if you could convince your modern transmitter to send more than a few milliwatts of power to the antenna.

(Also, the fact is that the metal aerial on your car is probably only used for FM reception. The AM receiver probably still uses an internal ferrite loopstick antenna, which is much longer [electrically]. The outside aerial is much closer to a $1/4\lambda$ for the FM band.)

Receiving is different from transmitting in another fundamental manner: radiation patterns. For receiving (HF, at least) we don't really care about the pattern. We stick our metal flag into the RF breeze and hope for the best. But for this to work the transmitter has to sweat the details about the radiation pattern and take-off angle, especially if we are talking multi-hop propagation. And the nodes of RF along a radiating antenna, along with how that interacts with the ground and other objects around it, is going to result in very different radiation patterns at different resonances (and non-resonances). And, therefore, how well you are heard at that frequency.

As for why longer antennas are bad for higher frequencies, the short answer is that they aren't. At least not necessarily. If you can find the right electrical length (either by tuning the actual length, or by using traps or coils) then experimentation has shown that (with the right feedpoint) some number of $1/2\lambda$ lengths of wire can work ok with a variety of frequencies. But there are practical limits to how many $1/2\lambda$ multiples can be present, which means longer (physically or electrically) antennas will never work very well for VHF.

The physics and theory for why this is so I will leave up to the experts here. But my understanding is that resonance is hand-in-glove with feedpoint impedance. And impedance directly affects how much RF energy you can push into an antenna system and expect to radiate into free space in some manner that means you'll be heard.

But Amateur radio is full of enterprising hams who threw any old length of wire out the window and used that (along with a tuner, ideally, at least to protect the transmitter), trimming as necessary, to make contacts on a number of lower bands. The sheer amount of space in ham periodicals over the decades dedicated to multi-band compromise antennas is proof enough of this.

In fact, this (and concerns about harmonics which were a common problem with early transmitters) is why the bands are arranged and separated as they are; the frequencies across the bands often relate to each other as whole number factors from each other.

I've not gone into real-world considerations like velocity factors and copper losses and free-space behaviour of a wire antenna and grounding, all of which affect electrical length, impedance, and radiation patterns, as these are whole subjects on their own.

## Answer (score 5, by hotpaw2)

A long antenna acts like a lot of little short antennas, all wired together.

Note that depending on the angle of the signal to the big antenna, the distance to each short antenna from the source can be different. For a big antenna the difference between these distances to each short antenna can be half a wavelength or longer.

Note also that the electrical distance from each short antenna to the longer antenna's feedpoint will also vary, for a big enough antenna by half a wavelength or more.

If the total variation in these distances for any two short antennas is an odd multiple of half a wavelength, the signals can cancel out, resulting in those portions not adding up to being a good antenna.

A large antenna has a lot more opportunities than a short antenna for these cancellations, depending on the frequency and the angle to the incoming EM wavefront, because more portions of a large antenna are farther apart, often by a half wavelength or more. (for a given finite element size partitioning)

There can also be signal reinforcements as well as cancellations, making the antenna pattern and aiming it a very hard problem to solve, with slight differences in antenna geometry or aim often making a good very long antenna into a dummy load that receives very little of some desired signal at some desired frequency.

AM radios in pockets or cars usually use an internal ferrite rod loopstick antenna, where the permeability of the ferrite core in conjunction with a very large number of turns (windings) capture as much magnetic energy from an MF RF EM field as a many magnitudes larger (much longer than the whip on the hood) wire antenna in free space.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20860/why-are-longer-antennas-not-suitable-to-pick-higher-frequencies, by Dan, hotpaw2. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
