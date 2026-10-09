# How to find or derive the maximum safe input power to a receiver?

*Tags: receiver, rf-power, electronics · score 5*

## Question

A number of my RF devices have a specified safe maximum input power, for example:

- "The maximum RX power of HackRF One is -5 dBm. Exceeding -5 dBm can result in permanent damage!" source
- "If you look at the R820T datasheet … you can see the max input power is 10dBm" source
- For the VNWA3 a "Maximum permissible external RF Input Level to TX-Out and RX-In ports: 0 dBm" source: page 5 (pdf)
- "In any configuration the maximum input power to the RSP1 must not exceed 0dBm" source: page 5 (pdf)

I'm wondering how I could determine a similar number for a general purpose receiver or a ham transceiver?

For example the specifications for my IC-706MKIIG include some "receiver sensitivity" and "squelch sensitivity (threshold)" values in microvolts, as well as some "selectivity" and "spurious and image rejection ratio" values in decibels, but it's not clear what this means as far as safely hooking it to a signal generator, or operating near other stations at field day, etc.

How do I know how much input power a commercial receiver can safely handle?

## Answer (score 3, by Kevin Reid AG6YO)

I'm going to start with an extremely conservative approach and work upward in power from there. It is highly likely that you can apply more power than the following analysis concludes.

Also, I assume you are considering a transmitter and a receiver tuned to the same frequency, nearby or connected by a transmission line. That is, we are concerned with how much power we can supply as a single in-band signal, rather than the total power of signals at frequencies unrelated to the receiver's tuning (where the safe limit *may* be higher but need not be).

Let's suppose that you have a *sensitivity* specification for the receiver — that gives us a *minimum* input level and we can work from there. First, if we have it in (micro)volts then we want to convert to power instead. Let's suppose that our sensitivity spec is 2.0 µV for the relevant band and mode.

$$ \begin{align} P &= \frac{V^2}{R} & \frac{(2.0\:\mathrm{µV})^2}{50\:\Omega} = 8\cdot10^{-14}\:\mathrm{W} \end{align} $$ Then convert to dBm (decibels relative to one milliwatt) for future convenience: $$ 10\log_{10}\left(\frac{8\cdot10^{-14}\:\mathrm{W}}{1\:\mathrm{mW}}\right) = -101 \:\mathrm{dBm} $$

So this tells us that if we put in a -101 dBm signal it'll definitely be safe, but we won't necessarily hear it very well.

The easy conservative solution at this point is to arrange exactly that much attenuation — that is, figure the output power in dBm of your transmitter at minimum setting, and the difference between that and -101 dBm is how much attenuation you need — and then gradually decrease the attenuation until you have an adequate SNR at the receiver.

(This attenuation can be obtained using a variable (or fixed) attenuator in a coax line, or by separating two antennas with enough distance, or cross polarization or aiming high-gain antennas in the wrong direction, et cetera. Though there's a point at which the dominant signal path between transmitter and receiver will be unintended leakage from the chassis, power cables, et cetera rather than whatever's hooked up to the antenna ports.)

But we'd like a more generous figure. We can obtain one by looking for any information that implies a *ratio* between two signals the receiver is able to receive safely.

An easy one to obtain that doesn't even need a spec-sheet is an S-meter. Standardized S-units are 6 dB, and a typical S-meter will read S1 through S9 and some number of dB beyond S9. Your IC-706MKIIG has an S-meter which reads from S1 to S9 + 60 dB — an overall ratio of $(8 \cdot 6\:\mathrm{dB}) + 60\:\mathrm{dB} = 108 \:\mathrm{dB}$. So we apply that to our minimum-power figure and get $-101\:\mathrm{dBm} + 108\:\mathrm{dB} = 7 \:\mathrm{dBm}$, which is nice and large.

On the other hand, I've just assumed that the sensitivity figure is “below S1” which might be wrong, and it looks like it is wrong: There's also [a standard for the reference level of an S-meter](What%20would%20be%20the%20typical%20received%20power%20of%20an%20S9%20signal.md), S9 = -73 dBm. So we take $-73\:\mathrm{dBm} + 60\:\mathrm{dB} = -13 \:\mathrm{dBm}$, which is smaller than the previous figure. But not by much.

Actually, we can even skip the part where we started from receiver sensitivity: the S-meter scale convention implies that it should be safe for any such receiver to receive a signal between S1 and S9, or -121 to -73 dBm.

But also note, as I mentioned at the start, that it is likely that a receiver is designed with a substantial margin of safety beyond the maximum on its S-meter scale.

So in a fairly pessimistic case, let's say you have a transmitter with an output power of 5 watts and no less; that's 37 dBm. Then in order to put it at our supposedly generally-safe level of -73 dBm, we need $-73\:\mathrm{dBm} - 37\:\mathrm{dBm} = -110 \:\mathrm{dBm}$.

That much attenuation is probably most conveniently achieved by the approach of putting a dummy load on the transmitter and letting the leakage carry your signal. But if you have enough attenuation (given the power level, more in the form of "dummy load with a sampling port") then there you go.

On the other hand, if you have a 1 mW (0 dBm) transmitter and a safe-for-10 dBm receiver, then you don't need any attenuation at all to be safe. (Though *safe* is likely not the same thing as *undistorted signal*.)

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7376/how-to-find-or-derive-the-maximum-safe-input-power-to-a-receiver, by natevw - AF7TB, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
