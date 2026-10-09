# Coaxial Folded Dipole Antenna Matching Impedance

*Tags: impedance, folded-dipole · score 4*

## Question

In http://www.nsw.wicen.org.au/technical/projects/coaxial-folded-dipole-antenna, the guy is using a 50 ohm coax cable to build a folded dipole antenna and claims that this will enable use at 50 ohm (I assume the required matching impedance).

Now, from my understanding, the impedance of a folded dipole is based on the theoretical radiation resistance of a dipole (73 ohm) multiplied by 4 since folded. This is roughly 300 ohm and does not depends on the cable itself.

Is that correct?

## Accepted answer (score 5, by tomnexus)

The site above depicts a regular dipole, with a simple matching system.  
First, a bit about dipole impedance. The impedance of a dipole is 73 Ohms at resonance, but away from the resonant frequency the impedance is different. At frequencies lower than resonance, i.e. when the antenna is too short, it is capacitive, and its resistance is lower.  
The Smith Chart is the usual way of plotting this. 50 ohms is in the middle, short circuit on the left, open circuit is on the right.  
  
If it makes more sense, you can see them on a regular X-Y chart.  
  
It's fairly simple to choose a point where the impedance is 50 -j something ohms. Then to match the antenna, only a series inductor is required. Please excuse my wobbly inductors.  
Now a bit about the stubs.  
The impedance of a short-circuited coaxial cable, like this:  
  
is given by the equation

$Zin = j * Z_0 * tan(\beta x)$  
where $\beta = 2 \pi / \lambda$  
and $Z_0$ is the impedance of the line, in this case $50 \Omega$.

This can also be done on the Smith chart.

The two short-circuited stubs each need to contribute about 80 ohms of reactance, so they will be a bit over 1/8 of a wavelength long. They're further contracted by the velocity factor of the coax.

The inductive reactance cancels the antenna capacitive reactance, resulting in a perfect 50 Ohm match.

That's how it works. Now for some comments about the antenna.

First, about bandwidth: The capacitance of the antenna and inductance of the stubs both change over frequency. The antenna gets more capacitive at frequencies below resonance, requiring more inductance to match, but the inductance of the stub *drops* at lower frequencies. This leads to a reduced bandwidth from this antenna, as compared to one matched with a transformer or some other way. Note the narrow VSWR curve on the left. In fact, if your radio could tolerate a VSWR of 2:1 or more, you'd be better off *not* using any coax stub to match it.  
This makes me think this isn't such a great choice of antenna - the ham bands are already wide enough that a regular dipole isn't perfectly matched across the band, so this one will be even narrower.

Second, about the balun: The site doesn't mention any Balun. This is a huge problem!! The feed cable of these antennas will carry current, perhaps half as much as the antenna itself, and so the VSWR will be affected by the length of the cable, the equipment connected to it, the ham moving around in the shack, everything. This is just bad practice. With any antenna design, the balun should be the first problem you solve, and then worry about the matching.  
[See this very comprehensive answer](Using%20a%20balun%20with%20a%20resonant%20dipole.md) for more about why you need a balun when connecting an dipole to coax.

Finally, the impedance of a dipole like this will only be $50 \Omega$ in free space. An antenna is *never* in free space, unless it's hanging off a cubesat. The supporting mast, or just the feedline, will affect its impedance. A good design starts by considering those effects, mechanical support, grounding for static, safety and lighting, then the balun, and finally the matching.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/3829/coaxial-folded-dipole-antenna-matching-impedance, by user4575, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
