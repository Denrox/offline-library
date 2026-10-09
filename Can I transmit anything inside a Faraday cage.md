# Can I transmit anything inside a Faraday cage?

*Tags: united-states, legal, license, faraday-cage · score 13*

## Question

Can I perform any transmission regardless of my license as long as I'm inside an RF sealed enclosure, such that no RF will be detectable from my transmissions off my property?

I imagine the answer is yes, but I'd like to be sure I understand.

## Accepted answer (score 8, by Kevin Reid AG6YO)

I don't have an answer actually clearly applicable to this situation, but a couple of related scenarios come to mind:


Every shielded digital electronic device is radiating "inside a RF sealed enclosure". Your scenario is different in that it's not a discrete device with built-in shielding.


Part 15 §15.211 permits *tunnel radio systems* to “operate on any frequency” provided that the emissions meet usual limits as measured at the tunnel mouth. However, this specifically applies to “a tunnel, mine or other structure that provides attenuation to the radiated signal due to the presence of naturally surrounding earth and/or water”, and not artificial shielding.

These are two cases where analogous things are occurring; neither one applies specifically here but they're both precedents which match the common sense “if no one else can receive it, it's OK”. This does **not** mean that it's actually legal.

## Answer (score 9, by WPrecht)

This is pretty much the same as transmitting into a dummy load (or using the stock rubber duck antennas :) ).

I don't think a canonical answer is possible; Part 97 is silent on the issue. But, if no one can hear you, you can't be interfering with anyone or "using" the spectrum, so I would say sure. Depending on what you are planning on doing (and on which bands), you might want to make some RF checks at the edge of your property to be sure you aren't leaking RF.

## Answer (score 7, by PearsonArtPhoto)

I'm trying to find a better source, but according to this letter from Boeing petitioning the FCC in 2011, an experimental license is technically required to operate even within a Faraday cage, although they have an unofficial policy of permitting such actions.

Finally, the Commission should codify its policy of permitting entities to conduct experiments within RF enclosures, such as anechoic chambers or Faraday cages, without an experimental license.

This makes sense as someone would have to complain before the FCC was involved. And such a chamber should be able to reduce the RF power going out to almost nothing, making the odds that someone complains very miniscule. Still, it could happen. If you use low power in such a device, you probably will be fine.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1052/can-i-transmit-anything-inside-a-faraday-cage, by Adam Davis, Kevin Reid AG6YO, WPrecht, PearsonArtPhoto. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
