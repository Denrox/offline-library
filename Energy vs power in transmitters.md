# Energy vs power in transmitters

*Tags: physics · score 5*

## Question

Higher frequencies have a higher energy, simply stated by Planck's constant. When I am transmitting 100 watts on 500 kHz, and transmitting 100 watts on 5 GHz, is there an energy difference in the wave?

## Answer (score 5, by Phil Frost - W8II)

If the birthrate in Canada is 400 thousand babies per year, and the birthrate is Russia is 1680 thousand babies per year, is there a population difference in the nations?

Just as birthrate is a rate of stuff (births), power is a rate of energy. A watt is one joule per second, by definition. The frequency is irrelevant. To answer your question we need to know about *time*.

If you transmit 100 watts on 500 kHz for 1 second, and 100 watts on 5 GHz for 1 second, then each has transmitted the same energy:

$$ 100 \mathrm W \cdot 1 \mathrm s = 100 \mathrm J $$

It doesn't matter what the frequency is, or even that this is electromagnetic power. It could have been mechanical power. 100 watts of any kind for one second is 100 joules.

If by "the wave", you mean "per cycle", then our notion of time is something else. At 500 kHz ($500\cdot 10^3 \text{cycles}/\mathrm s$), each cycle is one 500,000th of a second, or 2 microseconds. Transmitting at 100W, each cycle then carries the energy:

$$ 100 \mathrm W \left ( \frac{1 \mathrm s}{500\cdot 10^3 \: \text {cycle}} \right ) = \frac{100 \mathrm W \cdot 2 \mu \mathrm s}{\text{cycle}} = \frac{200 \mu \mathrm J}{\text{cycle}} $$

At 5GHz ($5\cdot 10^9 \text{cycle}/\mathrm s$):

$$ 100 \mathrm W \left ( \frac{1 \mathrm s}{5\cdot 10^9 \: \text {cycle}} \right ) = \frac{100 \mathrm W \cdot 0.0002 \mu \mathrm s}{\text{cycle}} = \frac{0.02 \mu \mathrm J}{\text{cycle}} $$

Thus, the energy per cycle at higher frequencies is less, which makes sense because there are more of them per unit time.

As Kevin Reid explains, Planck's constant relates to the energy of individual photons, which is relevant to quantum physicists, but not to amateur radio operators.

## Answer (score 4, by Kevin Reid AG6YO)

Higher frequencies of electromagnetic radiation have higher energy *per photon*; “the wave” you transmit is made up of huge numbers of (coherent) photons — for example, at 5 GHz, 100 watts corresponds to $10^{25}$ photons per second. Therefore, the individual photons' energy is not all that relevant.

For the same power (energy per time), count and frequency are inversely proportional; at a higher frequency, there are fewer photons emitted, each carrying more energy. We can derive this from the Planck relation which contains Planck's constant ($ν$ = frequency):

$$E_{\text{photon}}=hν$$

This is a relation of *individual photon energy* $E_{\text{photon}}$ to frequency; to consider multiple photons we need to take further steps. First, let's relate a total energy by defining $n$ such that $nE_{\text{photon}}$ is the total energy of the transmission, and then using the Planck relation:

$$E_{\text{transmission}} = nE_{\text{photon}} = nhν$$

Second, the example you asked about is in *power*, not *energy*, so we need to introduce time; dividing both sides by a time interval $t$ gives us:

$$P_{\text{transmission}} = \frac{E_{\text{transmission}}}{t} = \frac{n}{t}hν$$

Note that $\frac{n}{t}$ is the *rate* of photons per time.

Then if we divide by $hν$ and rearrange we get:

$$\frac{P_{\text{transmission}}}{h\nu} = \frac{n}{t}$$

Plugging in your example values gives us values for $\frac{n}{t}$ of:

$$\frac{100\, \mathrm{watts}}{h \cdot 5\,\mathrm{GHz}} \approx 3\cdot 10^{25} \text{ photons per second}$$

$$\frac{100\, \mathrm{watts}}{h \cdot 500\,\mathrm{kHz}} \approx 3\cdot10^{29} \text{ photons per second}$$

On the other hand, if we want to find out the energy-per-photon of your transmission, the total power is irrelevant and we simply use the Planck relation by itself:

$$h \cdot 5 \,\mathrm{GHz} \approx 3.3×10^{-24} \,\mathrm{J}$$

$$h \cdot 500 \,\mathrm{kHz} \approx 3.3×10^{-28} \,\mathrm{J}$$

This is everything that Planck's constant tells us about the properties of your transmissions.

However, these figures are almost irrelevant to the practice of radio.

Often in discussions of the energies of photons the topic is photons of much higher individual energies, which become significant; for example, by being absorbed by individual atoms at specific energies.

The photons in the "radio" portion of the electromagnetic spectrum are comparatively so low-energy that these “quantum” effects are not usually of interest, as opposed to the net effect of many coherent photons making up a field which pushes electrons around in antennas.

The “energy in the wave” (provided we define such a quantity, either by choosing a duration in time or a volume of space) is entirely independent of the frequency of the wave.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1826/energy-vs-power-in-transmitters, by Skyler 440, Phil Frost - W8II, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
