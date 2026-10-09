# How does a Faraday cage block an EMP?

*Tags: theory, faraday-cage · score 8*

## Question

If you search the Internet for Faraday cages, you'll find a lot of information about using homemade cages to protect radios from EMP damage while in storage. A lot of that information is either contradictory or isn't backed up by satisfactory explanations.

It's not my intent to debate the usefulness of storing equipment in Faraday cages. There aren't a lot of nuclear wars or lightning strikes where I live, so odds are really good that I don't need to worry about it. But, I am curious about the theory of operation and practical design considerations.

As I understand it, radio waves can't penetrate into a space that's fully enclosed by a sufficient thickness of conductive material. The radio waves induce a current in the conductor, which results in the energy being re-released as a mix of radio waves and heat, right? What stops the radio waves from being released to the inside of the container? (I'm guessing it's related to the skin effect.) Does it matter to any electronics inside the cage if they're in physical contact with the cage?

Is a DIY Faraday cage as simple as using a metal suitcase or a foil-wrapped box, or is there more to it than that?

## Accepted answer (score 8, by Phil Frost - W8II)

Faraday cages block EMP in the same way they block all other time-varying electromagnetic fields. The only difference between blocking EMP versus blocking an ordinary radio transmission is the EMP is many orders of magnitude stronger.

A Faraday cage works because metals consist of a "sea" of mobile electrons among the protons in the atomic nuclei. That is, metals are good conductors. When an electromagnetic field approaches the metal, the mobile electrons will be attracted to the locations where the electric potential is higher, leaving behind excess protons where the electric potential is lower.

The mobile electrons do this because they seek the lowest potential arrangement, just as a boulder rolls down a hill, or water in a vessel in any shape tends towards level.

To the extent that the Faraday cage is made of a perfect conductor, the electrons will rearrange themselves such that the redistribution of the electrons and the external field cancel exactly, so there is no change to the electromagnetic field inside the cage. No energy is lost in the process.

This animation absurdly exaggerates the distance the electrons travel (in practice they barely move, since if the protons were left all alone like that the box would tear itself apart into individual atoms), but it does a fair job of getting the idea across:

In practice metals aren't perfect conductors so a little energy is lost to resistance and converted to heat, and the electrons are unable to perfectly cancel the field so some of the electromagnetic wave makes it inside the cage, so we just say the Faraday cage attenuates the external field.

Skin effect does indeed limit the currents to the outside surface of the metal, but that's not really necessary to explain how a Faraday cage works. Consider: Faraday cages are also effective in blocking static electric fields, where skin effect does not apply. Insulating the protected contents from the cage is probably still a good idea if the very highest attenuation is required.

It is essential that the cage forms a continuous conductive shield fully enclosing the device to be protected. For example, cutting a slot in a Faraday cage renders it ineffective if that slot is an appreciable fraction of wavelength. This is because the slot presents a barrier to the motion of the electrons, and consequently the electric field associated with the mobile electrons must "flow around" the slot, making it no longer able to cancel the external field. A slot antenna exploits this effect to make a waveguide (which is not so different from an inside-out Faraday cage) radiate.

For this reason, metal boxes with lids don't always work as a Faraday cage, since often the lid does not make good electrical contact with the rest of the box.

Foil works OK as long as care is taken to make good electrical contact at all seams. And the thinness of foil means less attenuation, but depending on the power of the EMP and the sensitivity of the contents, perhaps it's sufficient.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/14900/how-does-a-faraday-cage-block-an-emp, by mrog, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
