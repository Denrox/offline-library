# Have hams ever used (clusters of) geostationary satellites as passive microwave reflectors?

*Tags: satellites, microwave · score 9*

## Question

A number of geostationary satellites are quite large and/or appear in clusters. Moreover, many of them have large reflectors pointing to Earth (e.g. satellite TV sats). Finally, these satellites are located at roughly $\frac{1}{10}$ the distance Earth-Moon.

This made me wonder: Have hams ever used (clusters of) geostationary satellites as passive microwave reflectors? What equipment would be necessary?

## Answer (score 10, by Phil Frost - W8II)

I'm going to make an educated guess and say *no*. Here's my reasoning:

Consider the difficulty in just communicating with a satellite. See [What is a link budget, and how do I make one?](What%20is%20a%20link%20budget%2C%20and%20how%20do%20I%20make%20one.md) or [What gain do I need to talk to SO-50 with my HT?](What%20gain%20do%20I%20need%20to%20talk%20to%20SO-50%20with%20my%20HT.md)

Geostationary orbit is much farther away than SO-50 and thus requires more gain, or more power.

Now if we are using this as a passive reflector, reasonable assumptions are that:

1. even with a pretty high gain antenna, most of our transmitted energy will miss the satellite.
2. most of the reflected energy won't be reflected back at the intended receiver back on Earth.

We can estimate both of these effects. Let's say we are transmitting with an isotropic antenna. (We wouldn't actually, but we can then work backwards to figure out how much gain we would need actually). Say we transmit with 1W. Any sphere centered on that transmitter will have 1W of power in it. By the time that sphere reaches the satellite at geostationary orbit, the sphere will be 35,786km in radius, and its area will be:

$$ A = 4 \pi (35786km)^2 \approx 1.6 \cdot 10^{16} m^2 $$

Thus, our power density at geostationary orbit is

$$ \frac{1W}{1.6 \cdot 10^{16} m^2} = \frac{6.3 \cdot 10^{-17}W}{m^2} $$

How much of this might be intercepted? Let's say we have something really big, like Envisat. It's largest face is 26m by 10m, for an area of $260m^2$. Let's say everyone is launching huge satellites into geostationary orbit for us to use as reflectors, and we can hit 100 of them. We then have an area of $26000m^2$ to intercept our transmission. Given our power density at that distance, the power intercepted is then:

$$ \require{cancel} \frac{6.3 \cdot 10^{-17}W}{\cancel{m^2}} \cdot 26000\cancel{m^2} \approx 1.6 \cdot 10^{-12}W $$

Compared to the 1W we were transmitting with, our loss is:

$$ 10 \cdot \log_{10} \frac{1.6 \cdot 10^{-12}W}{1W} \approx -118dB $$

You can make up for some of this with antenna gain. You can increase transmitter power. But then, you have to have enough power left to communicate from the satellite reflectors back to Earth, which is a similar problem to talking to an ordinary communication satellite. Only, you must do it without the benefit of antenna gain on the satellite, since they are just pieces of trash unlikely to be pointed in the right direction. Plus, they probably aren't very efficient reflectors.

Say you transmit with 1000W and have a 40dBi antenna. The reflected signal is like a transmitter with an isotropic antenna in geostationary orbit with a power of:

$$ 1000W \cdot 10^{(-118dB + 40dB)/10} = 0.015mW $$

Do you think you could hit a satellite without any antenna gain and 0.015mW? I'm thinking no.

This might seem an odd conclusion, when moon bounce and meteor scatter work. However, the problem is that satellites in geostationary orbit have such a *tiny* angular diameter compared to the moon or the ionization left by meteors. There simply isn't enough area up there to intercept RF energy, so most of it goes uselessly into space.

## Answer (score 4, by PearsonArtPhoto)

There was a conversation that I saw once about what it would take to bounce a signal off of the ISS, which is much closer and larger than GEO satellites. The area is approximately $400\,\mathrm{m}^2$, but varies significantly depending on the orientation of the arrays. That figure should be good enough for now.

Let's assume a distance of between 400 and 3000 km, similar to the SO-50 [link budget](What%20gain%20do%20I%20need%20to%20talk%20to%20SO-50%20with%20my%20HT.md). Assuming an isotropic antenna, 1 W, and perfect reflection, the power reflected will be between

$\frac{4\cdot10^5}{5\cdot10^{6\cdot2}} = -77\,\mathrm{dBm}$ and

$\frac{4\cdot10^5}{5\cdot10^{7\cdot2}} = -93\,\mathrm{dBm}$.

The loss will follow a similar $r^2$, and thus be anywhere from an additional

$10\cdot\log_{10}(\frac{1}{5\cdot10^6})=-133\,\mathrm{dB}$ to

$10\cdot\log_{10}(\frac{1}{6\cdot10^7})=-149\,\mathrm{dB}$.

Bottom line, the path loss is very high, on a very fast moving target. Add it together, best case that's a 200 dB loss, worst case that's 242 dB loss. And that assumes perfect reflection and orientation! A typical EME is around 220 dB loss, with a stationary target and world wide communication possible, I'd just stick with that.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/702/have-hams-ever-used-clusters-of-geostationary-satellites-as-passive-microwave-, by on4aa, Phil Frost - W8II, PearsonArtPhoto. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
