# Can there be (long range) propagation of HF from satellites?

*Tags: hf, propagation, satellites, theory · score 9*

## Question

HF transmissions from the ground can be reflected by the ionosphere leading to very long distance propagation. Satellites in low Earth orbit (160 km to 2,000 km) fly within the ionosphere (60 km to 1,000 km); with the F layer at 150 km to 500+ km.

So if a satellite is under, over or in the F layer, do the signals get absorbed, reflected away from the earth, or skim around/under the ionosphere (i.e. propagate a long distance)?

This would also depend on the incidence angle, presumably.

The reason I ask is I am wondering if HF would be useful for in CubeSats, which at UHF frequencies can only downlink/load during short pass windows. HF would probably be a lower bandwidth connection, but the time available, and the more constant connection might outweigh the low bandwidth.

## Accepted answer (score 10, by tomnexus)

Satellites can and do use HF for communications.

The first example would of course be Sputnik, which transmitted at 20 and 40 MHz.

Amateurs use HF to communicate with satellites. According to Amsat,

mode A: This mode requires a 2 meter SSB/CW transmitter and a 10 meter SSB/CW receiver...

Mode K; This mode requires a 15 meter SSB/CW transmitter and a 10 meter SSB/CW receiver... This mode is unique in that it can be done with a simple HF rig.

HF has advantages in its smaller Doppler shift, and reduced path loss, allowing omnidirectional antennas to be used more easily.

For the physics part of your question: the reflection from a layer of the ionosphere depends on electron density, frequency and angle of incidence (which changes its effective thickness).

At normal incidence, frequencies of below about 7-10 MHz are reflected, higher frequencies pass through. See Wikipedia for a graph of reflection against height.  
This page gives a great overview; (written with communication in mind, but what isn't reflected is transmitted). The equation for MUF is F_normal / ( sec θ ). So it's only for very long paths, grazing reflection, that the ionosphere ever reflects a 28 MHz signal. It would usually pass straight through the ionosphere, down to a fairly shallow angle.

Your last question makes it sound like you hope to use HF from a cubesat when it's *over the horizon*, not in *line of sight*. This would be highly unusual and would certainly not help with your data rate problem.

1. If you choose a frequency which easily penetrates the ionosphere, then it won't bounce around inside, to get to you, it'll just reflect out again.
2. Cubesats have very limited power, HF requires plenty of power to communicate around the world, 10s or 100s of watts.
3. If you're trying to send more data during a pass, then the right solution is to go *higher* in frequency, where antenna gains are higher, there's less atmospheric noise, and more bandwidth available. HF modems run at 1200 bps, WiFi runs at 11 Mbps and more.

That all said, there is one tiny balloon project, launched to fly around the southern hemisphere, that uses HF to phone home. It's only 30 km high, but it transmits just a few mW using wspr, and can be heard around the world, with luck. Bear in mind that it sends nothing but its position and callsign.

## Answer (score 2, by SDsolar)

HF from space is nothing new. In fact, the very first artificial satellite, Sputnik-1 (Wikipedia) was heard by many hams as it transmitted on both HF (20 Mc) and VHF (40 Mc).

Now the military is going a step further with what they call next-gen HF from space.

Rockwell Collins demonstrates next-gen HF satellite signals

Excerpt:

Rockwell Collins has demonstrated a next-generation high-frequency satellite communications system.

Rockwell used a wideband high-frequency (WBHF) system over a 5,000-mile distance, according to a company news release. The demonstration was part of an Air Force Research Laboratory project to maintain satellite communications when communications have been disrupted.

“Over the course of 30 days, Rockwell Collins’ next-generation HF [high-frequency] network reliably and rapidly passed data files of various sizes up to 1 megabyte,” the company said.

“The demonstration, which showed significant improvement over standard satellite and legacy HF systems, also tested ‘store and forward’ split site capabilities, which is a foundational element of next-generation HF networks.”

The project will continue exploring the optimum network configuration and waveform technologies for the new HF communications system.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5010/can-there-be-long-range-propagation-of-hf-from-satellites, by DarcyThomas, tomnexus, SDsolar. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
