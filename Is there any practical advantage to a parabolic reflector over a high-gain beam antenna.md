# Is there any practical advantage to a parabolic reflector over a high-gain beam antenna?

*Tags: antenna, uhf, gain · score 6*

## Question

I've been looking at options for a high-gain directional antenna recently, and I've noted that there are commercially available parabolic antennae for the shorter bands -- specifically 70 cm, with an antenna that probably doubles as a UHF OTA television receiving antenna. The size of these antennae, however, not much bigger than the microwave dishes used for satellite TV, makes me suspicious of their effectiveness.

It's my understanding that a Yagi-Uda can pretty readily exceed a gain of 10 dBi in its forward lobe; I've seen commercial ones advertised at 13 dBi. Even the seller's rating of these very small parabolics barely exceeds that figure, if at all, but can a parabolic antenna in the 440 band of manageable size (say, no more than 2 meters in any dimension) give enough additional forward gain to be worth the extra cost to purchase or effort to build?

## Accepted answer (score 6, by Scott Earle)

The issue with using a parabolic dish antenna at UHF is one of size. The 60cm dishes you see on the side of people’s houses are picking up signals at 10GHz, and if you scaled them up for the 70cm band you would have a dish around 14m across.

Those satellite TV dishes have a gain of around 35-40dB (source), which is very impressive - but you’re not going to build a 14-meter dish for use on 70cm (you’re really not).

Many people use stacked and bayed arrays of multiple-element yagi antennas for EME (moonbounce) work, rather than a dish. With four 13dBi yagis you will get around 19dBi of gain, which is pretty good going. With eight you will get around 22dBi. Any more than that and you’ll probably wish you’d just built the 14-meter dish.

EDIT: here is an array of eight stacked and bayed yagis for EME (moonbounce):

Source here

## Answer (score 3, by Phil Frost - W8II)

[Gain, wavelength, and effective aperture](Why%20is%20antenna%20aperture%20a%20function%20of%20wavelength.md) are related by:

$$ A_\mathrm{eff} = {G \lambda^2 \over 4\pi} $$

As such, a gain of 10 dBi ($G = 100$) for 440 MHz ($\lambda = 0.68\:\mathrm m$) means an effective aperture of:

$$ {100 \times 0.68^2 \over 4\pi} = 3.68\:\mathrm m^2 $$

Assuming we could build reflector antennas with 100% [aperture efficiency](What%20is%20the%20aperture%20efficiency%20of%20an%20antenna.md), this means you'd need a dish with an area of 3.68 square meters to achieve 10 dBi of gain at 440 MHz. This isn't impossible, but such an antenna would be heavy, expensive, and have quite a high wind load, so a Yagi might be a better choice.

Moreover, aperture efficiency isn't 100%, so the dish would need to be somewhat larger.

Most real parabolic antennas have an aperture efficiency between 50% and 75%. One of the factors limiting the efficiency is diffraction around the edges of the dish. As the dish becomes smaller relative to wavelength, this diffraction becomes more significant. So in practice, the dish must be several times larger than the wavelength to achieve a decent aperture efficiency. This is another reason you won't see a common rooftop dish used for 440 MHz: the dish is simply too small to be effective at that wavelength.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/14617/is-there-any-practical-advantage-to-a-parabolic-reflector-over-a-high-gain-bea, by Zeiss Ikon, Scott Earle, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
