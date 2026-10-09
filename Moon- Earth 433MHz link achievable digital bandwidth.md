# Moon->Earth 433MHz link achievable digital bandwidth

*Tags: antenna, digital-modes, vhf, uhf, bandwidth · score 10*

## Question

Let's assume we have the following situation:

1.

Transmitter on moon orbit (distance from earth ~400'000km), around 433Mhz.

2.

Transmitter power 1W, antenna gain 10dB, circular polarization. Steered to point to earth.

3.

Receiver is on Earth. Antenna is steerable 25dB, matching circular polarization.

4.

On-off keying modulation.

What data transfer speed is achievable in this configuration?

## Answer (score 15, by Marcus Müller)

**Short answer:** Math says max link rate is 2Mb/s if you knew the perfect channel coding. Which is still an unsolved puzzle.

**Long answer:**

You're calculating a link rate. That is fine, and can be answered using *Shannon's Channel Capacity*, which gives us the upper limit for bits per second that we can get across a given channel:

$$ C= b\cdot \log_2\left(1+ \frac SN\right)$$

with $b$ being the channel bandwidth, $S$ the signal energy and $N$ the noise power.

**This is a upper limit. It's a mathematically proven limit. Over a bandwidth-limited channel with a given SNR, you cannot get more bits per second reliably. There's no technical way around that limit.**

Now, you didn't mention $b$ at all. But that doesn't matter, we'll just calculate a "per Hertz of bandwidth" rate, and you can multiply that with the bandwidth of your transceiver.

Now, $S$ is only partly specified – you said what your transmit power $P$ was, and thus, we'll simply apply free space path loss to that (which simply is "since the sphere on which we distribute the energy grows, by how does the field strength go down?"). This incorporates the surface of a sphere, divided by the wavelength:

$$\begin{align} A_\text{free space} &= \left(\frac{4\pi d}\lambda \right)^2\\ &=\left(\frac{4\pi dc_0}f\right)^2\\ &=\frac{16\pi^2 d^2 f^2}{c_0^2}\\ &\approx\frac{160\,\cdot \,4^2\cdot10^{16}\,\text{m}^2\,\cdot\,4.33^2\cdot10^{12} \frac1{\text{s}^2}}{9\cdot 10^{18}\frac{\text{m}^2}{\text{s}^2}}\\ &\approx\frac{48000\cdot10^{16}\,\cdot10^{12}}{9\cdot 10^{18}}\\ &=\frac{48}9 10^{13}\\ &\approx 5 \cdot 10^{13}\\ &\approx 136\,\text{dB} \end{align}$$

So $S\approx \frac{1\,\text W}{5 \cdot 10^{13}} = 2 \cdot10^{-14}\,\text W$.

So, what is your noise power? We don't know, since we don't know your receiver!

Now, let's assume you operate that receiver at room temperature.

That means you get -174 dBm/Hz of spectral noise power density. Ok, that means your

$$\frac SN = \frac{-136\,\text{dBW}}{-204\frac{\text{dBW}}{\text{Hz}}\cdot b}= \frac{\text{Hz}}b \cdot 68\,\text{dB}\approx \frac{\text{Hz}}b \cdot 6.3\,\text{MHz}$$

(ignoring Noise Figure For Now)

When $\frac SN$ is smaller than 1, the argument of the logarithm becomes roughly 1, and $\log 1=0$, so you can basically get nothing across. So we must postulate:

$$\begin{align} \frac{\text{Hz}}b &< (68-\text{NF}_\text{dB})\,\text{dB} \end{align}$$

Since the logarithm falls slower than $b$ rises, you'll get the best result with a $b_\text{dBHz}\lim (68-\text{NF}_\text{dB})$; assuming a Noise Figure of 5 dB, a 63 dBHz = 2 MHz channel leads to maximized $C$:

$$C_{max} \approx 2\,\text{MHz}\log_2\left(1+3.15\right)\approx 2\log_2(4.15)\frac{\text{Mb}}{\text s} \approx 4\frac{\text{Mb}}{\text s}$$.

You **cannot** get that with On-Off-keying; you need at least 2 bits per Hz. So the "lowest" modulation that **might** be able to fulfill this purpose would be QPSK, if zero-roll-off channel filters existed. So you'd probably settle for something like 8-PSK with a whole metric effton of channel coding/error correction on top, to get even close to that. You'll probably be happy if you get a single megabit per second.

## Answer (score 8, by Phil Frost - W8II)

*Summary*: Theoretical maximum in the neighborhood of 10s of megabits per second. Less than that in practice, perhaps a lot less depending on budget.

Let's start with the [Friis transmission equation](What%20does%20the%20Friis%20transmission%20equation%20represent%20and%20how%20is%20it%20derived.md):

$$ P_{r(\mathrm{dB})} = P_{t(\mathrm{dB})} + G_{t(\mathrm{dB})} + G_{r(\mathrm{dB})} + 147.6 - 20 \log_{10} (rf) $$

Insert the values you've given for antenna gain, transmitter power, frequency and distance, to calculate the signal power at the receiver:

$$ \begin{align} P_{r(\mathrm{dB})} &= 30\:\mathrm{dBm} + 10\:\mathrm{dB} + 25\:\mathrm{dB} + 147.6 - 20 \log_{10} (400,000\:\mathrm{km} \cdot 433\:\mathrm{MHz})\\ &= -132\:\mathrm{dBm} \\ &= 6.31\cdot 10^{-14}\:\mathrm{W} \tag{1} \end{align} $$

Now knowing the signal power, we can use the Shannon-Hartley theorem to determine the maximum theoretical channel capacity $C$ in the presence of noise power $N$, signal power $S$, and channel bandwidth $\Delta f$:

$$ \begin{align} C &= \Delta f \log_2 \left ( 1 + {S / N} \right) \\ \tag{2} \end{align} $$

We've already calculated the signal power, but what's the noise power? Let's assume there's no interference or ambient RF noise, and that your receiver introduces no noise of its own. The only noise then is Johnson-Nyquist noise, which is a function temperature $T$ (in kelvin), and the bandwidth of the channel $\Delta f$, and Boltzmann's constant ($k_B \approx 1.38 \cdot 10^{-23}$)

$$ P_\mathrm{noise} = k_B \: T \: \Delta f \tag{3}$$

It's also the case for OOK (with appropriate pulse shaping) that the bandwidth of the signal is equal to the bitrate. That is:

$$ \Delta f = C \tag{4} $$

Combining theoretical channel capacity (2), thermal noise (3), and the bandwidth efficiency of OOK (4), we get:

$$ C = C \: \log_2 \left( 1 + {S \over k_B \: T \: C} \right) $$

Solving for C:

$$ \begin{align} 1 &= \log_2 \left( 1 + {S \over k_B \: T \: C} \right) \\ \ 2 &= 1 + {S \over k_B \: T \: C} \\ \ C &= {S \over k_B \: T} \\ \end{align} $$

Let's approximate Boltzmann's constant and add the received signal power calculated in equation 1:

$$ \begin{align} C &= {6.31\cdot 10^{-14} \over 1.38 \cdot 10^{-23} \: T } \\ \\ &= {4.57\cdot 10^{9} \over T } \end{align}$$

In sunlight, the moon can be about 400K, and you'd then need to integrate the moon's temperature (and the 4K or so for the night sky) over your antenna's pattern to get the noise temperature. The comments in Marcus Müller's answer have a little discussion.

That will give you an upper bound on the possible channel capacity. It's in the neighborhood of tens of megabits per second.

I'd also note that you should be able to do better with QPSK: it has the same bit error rate for a given energy-per-bit as BPSK, while being able to fit the same bit rate within half the bandwidth of OOK or BPSK. A narrower channel bandwidth means less noise, and thus a higher SNR and channel capacity.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7154/moon-earth-433mhz-link-achievable-digital-bandwidth, by BarsMonster - R2AYN, Marcus Müller, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
