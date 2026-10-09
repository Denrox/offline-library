# how does this collinear antenna work?

*Tags: vhf, uhf, vertical-antenna, phased-array · score 3*

## Question

I was looking for a cheap and easy to build 2M/70cm vertical. I found this: http://vk2zoi.com/articles/dual-band-high-gain-flower-pot/

Here are the plans to build it:

But I don't really understand how it works. Here are my doubts, starting from the bottom:

1. the lower coil seems to be an "ugly balun", a choke made out of coax, is this it?
2. the 447/457mm section, I don't understand. The 457mm section seems to be a radiator. According to some calculator, this should resonate at around 156mhz, which is what I observed when I built this antenna. Lengthening this 457mm section by 32mm helped me lower the resonance to 146mhz. What is the 447mm "covered" section, though? Is it some sort of quarter-wave matching? should it also be extended if i try to match the antenna to a lower frequency?
3. the 7 turns middle coil, what does it do? I have read about phasing coils, but I've seen them implemented as coils that are part of the antenna. this is just a section of coax, like a choke balun. does this also work as a phasing coil?
4. now there is a 920mm section of radiator. why is this different from the bottom part, not "half covered"? it also seems related to a half-wavelength. when trying to make this antenna resonant for 146mhz, I also extended this section by 60mm
5. finally the sleeves. what are they? they do work, though, for UHF frequencies. moving them up and down makes the UHF resonance (and SWR) move. I was able to tune the antenna in UHF by moving these sleeves and got a very good match in the 70cm band, withouth affecting the 2M match

This antenna promises 6dBd of gain in 70cm and 3dBd in 2M. Is this realistic? What would be the pattern for this?

## Accepted answer (score 2, by hobbs - KC2G)

the lower coil seems to be an "ugly balun", a choke made out of coax, is this it?

Sure looks like it.

What is the 447mm "covered" section, though? Is it some sort of quarter-wave matching? should it also be extended if i try to match the antenna to a lower frequency?

Yes, it's definitely intended as a kind of quarter-wave transformer akin to the lower segment of a J-pole. The fact that it's a little shorter than expected might have something to do with the physical extent of the "ugly balun", or something to do with the mystery "sleeves".

the 7 turns middle coil, what does it do? I have read about phasing coils, but I've seen them implemented as coils that are part of the antenna. this is just a section of coax, like a choke balun. does this also work as a phasing coil?

Yes, it's a phasing coil. At a guess, the braid and jacket are left on this section to give the coil the right spacing or the right amount of parasitic capacitance. It's not "working like coax" since the braid is left unconnected at both ends.

now there is a 920mm section of radiator. why is this different from the bottom part, not "half covered"?

Because it is what it is, just a half wavelength of radiator.

finally the sleeves. what are they?

I have no idea what the theory on these is supposed to be. Obviously they have some effect on the impedance of the antenna in the area where they're placed, and moving them between lower- and higher- impedance points along the length of the antenna. But the author doesn't offer any real explanation of what they're doing, and I can't come up with one on my own.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16634/how-does-this-collinear-antenna-work, by hjf, hobbs - KC2G. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
