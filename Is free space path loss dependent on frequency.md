# Is free space path loss dependent on frequency?

*Tags: propagation, math · score 16*

## Question

Free space path loss is calculated as:

$$ \left( 4 \pi df \over c \right)^2 $$

The presence of $f$ in this equation means that losses increase with increasing frequency, so there's an inherent advantage in lower frequencies, right?

## Accepted answer (score 23, by Phil Frost - W8II)

Mathematically yes, the value of that equation increases with frequency. However, that's not to say there's some physical mechanism for frequency-dependent attenuation in free space.

Rather, the frequency term is in the equation due to the assumption of unity gain antennas at each end. A larger antenna is required to get the same gain at a lower frequency. This [larger antenna collects energy from a larger area](Why%20is%20antenna%20aperture%20a%20function%20of%20wavelength.md), and thus the loss between them is less, even though the attenuation in free space happens at the same rate.

To do a fair comparison, let's compare two similarly sized antennas. Let's compare a 2.4 GHz antenna with a 5 GHz antenna, each a parabolic dish antenna with a 5 meter reflector diameter.

We can approximate the gain of these antennas with the the equation:

$$ G = {4\pi A f^2 \over c^2}e_A \tag{1}$$

where:

- $A$ is the area of the reflector,
- $f$ is the frequency, in Hz
- $c$ is the speed of light in m/s, and
- $e_A$ is the [aperture efficiency](What%20is%20the%20aperture%20efficiency%20of%20an%20antenna.md).

If we assume an aperture efficiency of 80%, then:

$$ G_\text{2.4GHz} \approx 41\:\mathrm{dBi} $$

$$ G_\text{5GHz} \approx 47\:\mathrm{dBi} $$

In other words, despite these antennas being the same size, the 5 GHz antenna has about 6dB more gain. Does this compensate for the higher free space path loss at 5 GHz?

Let's do the math. Assuming a constant gain receiving antenna in any case, the power received will be proportional to the transmitting antenna's gain (from equation 1), multiplied by the reciprocal of the free space path loss (equation from the question):

$$ \require{cancel} \left({4\pi A f^2 \over c^2}e_A\right) \left( c \over 4 \pi df \right)^2 \\ \ \left({\cancel{4\pi} A \cancel{f^2} \over \cancel{c^2}}e_A\right) \left( \cancel{c^2} \over (\cancel{4 \pi} d)(4 \pi d) \cancel{f^2} \right) \\ \ {A \: e_A \over 4 \pi d^2} \tag 2 $$

Notice that this equation is just the area of the reflector and the aperture efficiency divided by the surface area of a sphere with radius $d$.

In other words, irradiance is proportional to the inverse-square of distance, regardless of frequency.

However, the 5 GHz antenna will have a smaller beam width, thus focusing the transmitted power over a smaller area. This means the 5 GHz case will have a higher irradiance than the 2.4 GHz case, assuming the antenna is optimally aimed. If the receiving antenna has an *equal effective aperture* (rather than a constant gain) at any frequency, the receiving antenna will then be subject to a greater radiant flux with increasing frequency.

So in summary:

- The definition of *free space path loss* describes the loss between two unity gain antennas, not the rate at which free space attenuates electromagnetic radiation.
- Electromagnetic radiation "spreads out" according to the inverse square law, regardless of frequency.
- The definition of *unity gain* is frequency dependent: lower frequencies correspond to a larger aperture.
- Higher frequency antennas generally allow for a tighter beam within a given physical size.

## Answer (score 6, by Mike Waters)

I'd like to offer a parallel and simplified explanation to W8II's correct answer above, for the mathematically-challenged VHF+ enthusiasts among us. :-)

As was mentioned in recent threads here, *effective aperture* is a measure of the power captured by an antenna. Effective aperture can be expressed as a function of the antenna gain and the wavelength.

Now, how does this affect real-world communications on VHF, UHF, and microwave amateur bands? Here is a simplified alternative answer based on information from the book *VHF-UHF Manual* (3rd edition, published by the RSGB). On pages 7.2 and 7.3 (photo attached) they state:

It is the capture area of the [antenna] that determines its effectiveness in absorbing the incoming radiation: it means that as the wavelength is reduced it becomes increasingly important to design the [antenna] to have a higher gain.

In simpler terms:

1.

We make contact with a distant station on 144 MHz, who has an identical phased array and height as our antenna. The gains and patterns are identical. Signals are just readable.

2.

We then attempt to make contact with this station on 432 MHz with a scaled-down version of the 144 MHz array **with the same gain and pattern**. The statement above from that book implies that we will not succeed!

Part of the reason is that the received power at the receiver input will be significantly less on the higher band, *even though the gain of both antennas is the same*! If we want to communicate with that distant station on the higher band, then **we need to increase the gain of the 432 MHz array so that its aperture is the same as the 144 MHz antenna**.

It goes without saying the band conditions will vary; but we are assuming that the conditions are the same for both tests.

Some related material: https://books.google.com/books?id=QtJ5tNdlyYAC&lpg=PA304&ots=Vd0TqH016t&dq=antenna%20capture%20area%20OR%20aperture%20vs%20gain&pg=PA303#v=onepage&q=antenna%20capture%20area%20OR%20aperture%20vs%20gain&f=false

https://www.google.com/search?newwindow=1&safe=active&q=aperture+antenna+lecture+notes&sa=X&ved=0ahUKEwjrgcC417PUAhVE6YMKHR8xD1cQ1QIIkwEoBw&biw=1105&bih=863

https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-661-receivers-antennas-and-signals-spring-2003/readings/ch3new.pdf

http://www.rfcafe.com/references/electrical/ew-radar-handbook/one-way-radar-equation.htm

https://en.wikipedia.org/wiki/Antenna_aperture

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/3692/is-free-space-path-loss-dependent-on-frequency, by Phil Frost - W8II, Mike Waters. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
