# What is dB(μV/m), and what are its applications?

*Tags: math · score 6*

## Question

Many radio coverage tools yield results in dB(μV/m). For example, CRC-COVWEB or nearly any tool based on the Longly-Rice model.

The unit occurs in regulations sometimes as well. For example, maximum permissible exposure limits may be given in V/m, which seems like a similar unit.

What's a dB(μV/m)? How is it defined? I'd like to see some math.

And why use it, instead of some other more familiar unit?

## Accepted answer (score 7, by koalo)

**TL;DR:** $\frac{V}{m}$ and $\text{dB}(\mu V/m)$ are units for the field strength of an electric field. For a practical application skip to the end!

**Derivation of the field strength**

A point charge $q_1$ generates a field strength* of $E = \frac{1}{4\pi\varepsilon_0}{q_1\over r^2}$ at a distance of $r$.

This is derived from Coulomb's law that is $F=\frac{1}{4\pi\varepsilon_0}{q_1q_2\over r^2}$ giving the force acting on two charges $q_1$ and $q_2$ at a distance of $r$. It can be rewritten as

$F=q_2 \cdot \frac{1}{4\pi\varepsilon_0}{q_1\over r^2}=q_2\cdot E$ or the other way around $E = \frac{F}{q_2}$

So from the field strength $E$ we can calculate the force on a test charge of $q_2$ by multiplication.

Now for the units. If we have a test charge of $q_2 = 1\,C$ that experiences a force of $F = 1\,N$, we get a field strength of $E = \frac{F}{q_2} = \frac{1\,N}{1\,C} = 1\,\frac{N}{A\cdot s} = 1\,\frac{N\cdot m}{A\cdot s\cdot m} = 1 \frac{V}{m}$.

* I use the scalar form and assume all amounts have the same sign and direction for simplicity.

**Decibel**

But your actual question was about $\text{dB}(\mu V/m)$, but that is just a numerical transformation to get values that are easier to calculate with in real world applications, because the values are usually very small. $0\,\text{dB}(\mu V/m)$ corresponds to $1 \frac{\mu V}{m}$ and that is also $10^{-6} \frac{V}{m}$.

So this is a usual decibel conversion. For example to get the field strength in $\frac{V}{m}$ for $45\,\text{dB}(\mu V/m)$ we calculate

$E = 10^{-6} \frac{V}{m} \cdot 10^\frac{45}{20} = 178 \cdot 10^{-6} \frac{V}{m}$

The 20, because $E$ is a field quantitiy and not a power quantity.

**From field strength to reception power**

Now we know what $\text{dB}(\mu V/m)$ is. Its main advantage is that it specifies the properties of the electic field without the need to take the reception antenna or the receiver into account!

Unfortunately, it does not help a lot for radio transmission, because we usually do not receive with force meters attached to probe charges, but antennas and receivers ;-)

This transformation to get the reception power is not straightforward, because it highly depends on the antenna and other parameters, but I can give an approximative calculation. For this we need the wave impedance in free space $Z_0 = \sqrt{\frac{\mu_0} {\varepsilon_0}}$. With this we get the surface power density in the far field of $S = \frac{E^2}{Z_0}$.

And with the antenna aperture or effective area $A_w$ that is for example $\frac{\lambda^2}{4\pi}$ for an isotropic radiator or $0.1305\, \lambda^2$ for a half wave dipole, where $\lambda$ is the wave length, we can then calculate the reception power

$P = S \cdot A_w = \frac{E^2}{Z_0} \cdot A_w$.

**Complete example**

Lets say we want to estimate the reception quality of the DB0ZU repeater on the Zugspitze at Ohlstadt in a distance of $30\,\text{km}$ with a nice unobstructed view to the Zugspitze (except for the cow). We assume a radiation power of $1\,W$ and a frequency of $145\,\text{MHz}$ ($\lambda = 2.07\,\text{m}$).

According to CRC-COVWEB we get $45\,\text{dB}(\mu V/m)$ in Ohlstadt. Look above for the calculation to get $178 \cdot 10^{-6} \frac{V}{m}$ from this. We can then calculate a surface power density of

$S = \frac{E^2}{Z_0} = \frac{\left(178 \cdot 10^{-6} \frac{V}{m}\right)^2}{377\,\Omega}$ $= 84\,\frac{pW}{m^2}$

Assuming we receive with a half wave dipole without further losses, we get a reception power of

$P = S \cdot A_w = 84 \frac{pW}{m^2} \cdot 0.1305\, \lambda^2 = 84 \frac{pW}{m^2} \cdot 0.1305\, (2.07\,\text{m})^2 $ $= 4.6 \cdot 10^{-11} W$ $= -73\,\text{dBm}$. That is a nice S9+20 dB signal.

For an isotropic radiator we have to replace the 0.1305 with $\frac{1}{4\pi}$ and get $-75\,\text{dBm}$. This result is in line with the calculator found here.

**Shortcut calculation**

All the calculations above can be combined resulting in a single formula.

$P_r \,(\text{dBm}) = E \,(\text{dB}\mu V/m) - 20 \cdot \log_{10}\,\, f \,(\text{MHz}) - 77.2$

So for our example:

$P_r = 45 - 20 \cdot \log_{10}(145) - 77.2 = -75\,\text{dBm}$.

This approach is taken from Christopher Haslett, "Essentials of Radio Wave Propagation", Cambridge University Press, 2008. Chapter 2 also provides some more explanation.

**Comparison with free space path loss**

Instead of using the CRC-COVWEB tool, we can also estimate this reception power of an isotropic radiator by using the free space path loss model.

$\mbox{FSPL(dB)} = 20\log_{10}(d) + 20\log_{10}(f) + 20\log_{10}\left(\frac{4\pi}{c}\right)$

Since there are no obstacles between the Zugspitze and Ohlstadt the result should be quite similar. And in fact,

$\mbox{FSPL(dB)} = 20\log_{10}(30\,\text{km}) + 20\log_{10}(145\,\text{MHz}) + 20\log_{10}\left(\frac{4\pi}{c}\right) = 105\,\text{dB}$

$1 W = 30\,\text{dBm}$, so the reception power is $-75\,\text{dBm}$.

## Answer (score 3, by Glenn W9IQ)

**Introduction**

In amateur radio, we are used to giving signal reports in the form of "S-units". The S-unit is based on the amount of power at the receiver's input terminals. Thus we can see that the gain of the receive antenna plays a role in the level of the S-unit.

In professional circles, it is more common to be concerned with the "field strength" of the signal in the area in which the receive antenna is located. This measurement must then specifically eliminate the effect of the receive antenna. Field strength is typically expressed as volts per meter or V/m. Often the field strength is quite small so it may be shown as mV/m (millivolts per meter) or μV/m (microvolts per meter). It is also common to do a logarithmic comparison to 1 μV/m in dB form. This can be shown as dB(μV/m) or often simply dBμ.

**The Math**

Start with the notion of an isotropic antenna centered in a sphere of radius $r$. The antenna is illuminating the sphere uniformly with RF energy. We can then imagine that there are a certain number of watts per square meter on the surface of the sphere at some point called $O$. This is an expression of RF power density.

If we express the radius of the sphere in meters, we can then directly calculate the power density as:

$$P_d=\frac{P_t}{4\pi r^2} \tag 1 $$

where $P_d$ is the resulting power density in watts/meter, $P_t$ is the input power to the isotropic antenna in watts, and $r$ is the radius of the sphere in meters.

By definition, the isotropic antenna has a linear gain of 1. We can expand equation 1 to work for any gain of transmitting antenna, provided the point of maximum gain is at the observation point $O$ on the sphere:

$$P_d=\frac{P_t G_t}{4\pi r^2} \tag 2 $$

where $G_t$ is the linear gain of the transmitting antenna.

We can now convert the power density to field strength (intensity) in $\mathrm{V/m}$ by applying Ohms law using the impedance of free space which is $120\pi$ ohms:

$$E=\sqrt{P_d120\pi} \tag 3 $$

This is the field strength in volts/meter at the observation point $O$.

But now we must detect this signal using a receive antenna. The antenna will not necessarily intercept exactly one square meter of power from the transmitter. The effective intercept area or capture area of an antenna is known as the Effective Aperture:

$$A_e=\frac{G_r\lambda^2}{4\pi} \tag 4 $$

where $A_e$ is the effective aperture in meters, $G_r$ is the linear gain of the receive antenna and $\lambda$ is the wavelength of the received signal.

The power received by the antenna is:

$$P_r=P_dA_e \tag 5 $$

The receive antenna will convert the received power to voltage according the impedance of the antenna:

$$E_r=\sqrt{P_rZ_{ant}} \tag 6 $$

where $E_r$ is the voltage at the receive antenna terminals and $Z_{ant}$ is the impedance of the receive antenna.

Combining equations 5 and 6 and solving for $P_d$:

$$P_d=\frac{E_r^2}{A_eZ_{ant}} \tag 7 $$

And finally combining equations 3 and 7:

$$E=\sqrt{\frac{E_r^2 120\pi}{A_eZ_{ant}}} \tag 8 $$

This gives us the field strength in $\mathrm{V/m}$ after "backing out" the effect of the receive antenna. We can now convert the linear numerical $E$ from equation 8 in $\mathrm{V/m}$ referenced to $1\:\mathrm{\mu V/m}$ in decibel form:

$$\mathrm{dB(\mu V/m)} =20 \cdot \log\left( E \over 10^{-6}\:\mathrm{V/m} \right) \tag 9$$

## Answer (score 2, by Richard Fry)

A dB(**µV/m**) is a decibel relation for a sub-unit of **V/m**, which is appropriate for units of the e-field intensity of a radiated e-m wave existing between two physical points in space separated by a linear distance of one meter. These units are used commonly by the FCC, and other regulators of the use of the e-m spectrum.

Examples: 0 dB(µV/m) = 1 microvolt/meter; 60 dB(µV/m) = 1,000 microvolts/meter.

Often the unit dB(µV/m) is written as simply "dBu." However that term is meaningless as an SI definition* because the basic unit of measure (volts) is not included, and must be inferred by the reader.

- see https://en.wikipedia.org/wiki/SI_derived_unit

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9658/what-is-db-mv-m-and-what-are-its-applications, by Phil Frost - W8II, koalo, Glenn W9IQ, Richard Fry. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
