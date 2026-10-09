# Why is VHF better than UHF in this situation?

*Tags: propagation, vhf, uhf · score 3*

## Question

One of the sample questions for the British foundation level test is:

An amateur has the choice of VHF or UHF for a particular contact of some 25km. Which statement below best describes his choice?

and the correct answer is:

The VHF option is most likely to give a better signal.

There was an equivalent answer with UHF instead of VHF and two almost non-nonsensical ones.

Why is VHF better than UHF in this situation?

## Answer (score 8, by Phil Frost - W8II)

This is an ill-posed question, since "best" could mean so many things. If VHF is so plainly best, why does anyone bother with UHF at all?

If you mean what option has a lower path loss, then sure VHF is the better option. But then HF would be even better. And why not go with ELF? [As the frequency decreases, so do free space path losses](Is%20free%20space%20path%20loss%20dependent%20on%20frequency.md).

Well, an ELF antenna would be many kilometers long. While ELF would certainly be "best" in terms of free space path loss, when considering the entire proposition including constructing such an antenna, ELF isn't "best" by what most people would assume as the criteria.

The difference between UHF and VHF is of course less extreme, but you still have to wonder, what are the optimization criteria? While VHF has a lower free space path loss, it also requires a physically larger antenna to achieve a comparable gain as UHF. So if "best" means "minimum physical size to realize a reliable link", then there's not much difference.

Or perhaps the use case is an interference limited point-to-point link. In this case, for antennas of equal effective aperture, the UHF antenna will have higher directivity, while likely being about the same physical size of a VHF antenna of equal effective aperture. So in this scenario UHF is superior, since the necessary directionality can be achieved by a physically smaller antenna on UHF.

Maybe you desire some degree of privacy. Again, the higher directivity at higher frequencies given a limited physical size makes higher frequencies better.

Or perhaps "best" means lowest equipment cost. Technology is always advancing, but it's generally true that electronics to operate at lower frequencies are older and cheaper, so VHF has an advantage here. In modern times the difference in cost between 144 MHz and 440 MHz isn't much, but if we are pushing the 3 GHz upper limit of "UHF", the opportunities to find cheap, used gear decrease. Unless you can use consumer commodity 2.4 GHz equipment, in which case economies of scale make it the cheaper option.

Or perhaps "best" means there's an available frequency to use. UHF allocations tend to be bigger and newer, and so have more unallocated channels.

Does "best" mean lowest noise floor? The natural noise floor generally decreases at higher frequencies, but man-made noise may be the bigger issue. Depending on what man-made sources you have to contend with, this could go either way. For example if UHF means specifically the 13 cm band, you may need to contend with the 2.4 GHz ISM band, including microwave ovens, cordless phones, and consumer Wi-Fi radios.

Or perhaps you'll consider that for frequencies too high to support ionospheric propagation, the radio horizon imposed by the height of the antennas can be more a limiting factor than raw power or free space path loss. In this case perhaps you would favor UHF for its smaller Fresnel zone, if your link is at the limits of the radio horizon.

Maybe "best" means the signal can penetrate buildings. In this case VHF is the winner, since lower frequencies generally penetrate better.

Or perhaps you need to communicate beyond the radio horizon, or you don't have a direct line of sight. In this case UHF may be better since decreased building penetration means more effective reflection, thus allowing a building to be used as a passive reflector, for example.

Or perhaps your concern is what equipment the other operator has? Or what local repeaters exist? Such simple practical considerations often outweigh more theoretical ones.

I could go on, but the point should be clear: while the question clearly expects an answer framed by free space path loss, this is only but one consideration, and a minor one at that. In practice on VHF and higher, radio horizon and interference are the limiting factors. For digital modulations especially, multipath distortion limits range. And while not much of a problem for hams, the monetary cost of obtaining an allocation is probably the primary factor in selecting a frequency. It's a shame that an amateur radio exam reduces what's actually a multi-faceted problem to rote memorization or just free space path loss, but there you have it.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9333/why-is-vhf-better-than-uhf-in-this-situation, by Pablo Fernandez, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
