# Is there an optimum transmission line length for maximum power transfer?

*Tags: transmission-line · score 10*

## Question

Consider a typical source -> transmission line -> load (i.e. TX->transmission line->antenna) arrangement and assume that the load is not matched to the transmission line characteristic impedance.

It's always possible to select a length of transmission line that transforms the load impedance, X+jY, into a pure resistance, R+j0, at the source (where R is not equal to the characteristic impedance of the transmission line). This can be illustrated by moving around a constant VSWR circle on the Smith Chart - starting from any random load impedance, you can always arrive at a pure resistance at the source end of the line

My question is: would there any advantage in doing that - i.e. does a source prefer to see a mismatched resistive load rather than a mismatched load with a reactive component?

As a specific example, take a normalised characteristic impedance, Zo = 1+j0, a source with the same matched output impedance, and assume we have a mismatched load impedance of 0.5+j. Initially assume a line of length equal to an integer number of half-wavelengths so that the source sees 0.5+j. Now change the length of the line (i.e. move around a constant VSWR circle starting from 0.5+j) until we reach a pure resistance of about 0.24+j0. Would the source, with output impedance 1+j0, prefer to see 0.24+j0 or 0.5+j (or, perhaps, no preference)?

## Answer (score 5, by Phil Frost - W8II)

Ideally, it doesn't matter where on the constant VSWR circle you are. The transmitter is an ideal voltage source with 0Ω impedance, essentially a short. There's no way to couple power into a short, so whatever power is reflected from the antenna gets reflected back when it reaches the transmitter, so all you need to worry about is the impedance presented to the transmitter, and what effect that will have on the current required.

But transmitters are rarely just a voltage source. Usually they have filters at the output to strip off the harmonic distortion created by the amplifier. Even a linear class AB amplifier will generate a little harmonic distortion, enough to require a filter to avoid spurious emissions.

The filters are designed with a 50Ω load assumed. Since they are passive filters, loading them differently will change the frequency response.

Let's look at the schematics for the Alex-TX board of HPSDR for an example. Here's the 20/30m transmit filter. R1 isn't part of the filter, but the impedance seen by the transmitter, which we will vary.

Here's the power dissipated in R1 (that is, RF power radiated) as a function of frequency. Shown is what happens at 5, 50, and 500 ohms, normalized to the power that would be expected at a given voltage into a 50Ω load:

The orange line is a 50Ω load. You can see the filter makes a good low-pass filter, with a steep cutoff above the 20 meter band, effectively suppressing harmonic distortion.

However, look at the peaks and valleys introduced by the mismatch. One of those peaks in the 5Ω case is at 14 MHz, so on 20 meters it looks like you get an extra 10dB of transmit power with this particular filter and load.

That might seem like a good thing, but that power isn't free: it comes from your transmitter. That means the transmitter will be asked to deliver a lot more current, and probably overheat if it lacks appropriate protection.

The reactive 10:1 SWR cases fall around (9±49j)Ω. Unfortunately, CircuitLab doesn't provide a way to model a complex impedance, but it's basically the same, except the peaks and valleys fall in different places.

There's another issue as well: since the filter is made of resonant, reactive components, there is a potential for very high currents or voltages to develop in there if you start messing with the load impedance. So although in these 10:1 conditions the power in the transmitter and the load are identical to the 1:1 case, that doesn't mean the current and voltages within the filter are the same. High currents will overheat or saturate inductors, and high voltages will arc.

So to answer your question, there usually is a transmission line length which will spin the impedance around to one that will allow the transmitter to deliver full power without overheating. But in practice we don't know the details of the transmitter's design, so there's not really a way to know what that length is.

## Answer (score 2, by K4ERO)

Google "load pull" and you will find that with real world solid state amplifiers, it is useful for the designer to try many different loads on an amplifier,(at its output, typically), and see what combination of real and reactive load produces the best combination of power, efficiency and distortion. The output networks of the single frequency/single power level amplifier would then be designed so that that optimum operating point corresponds with the specified design load (typically 50 ohms). While one or more parameters might be better operating away from a 50 ohms resistive load, that would violate the designers choice of overall optimum operation.

If you have to use a length of transmission line as a matching device, you are not operating with a flat line and loss will increase. Not a recommended technique in most cases. You could however use a 75 ohm line to connect between a 50 ohm transmitter and a 50 ohm antenna by cutting the line to an electrical half wave. This causes the transmitter to see the antenna impedance since to a good approximation (neglecting losses), the impedance on a line repeats each half wave. Using 75 ohm line in this way operates the line with 1.5 SWR, but this would not be a serious problem in most cases.

However, I see your question as asking if in the general case there is any advantage when operating into a high SWR to have a particular line length,for example a pure resistance not a mixed real and reactive one. While you will be operating away from the design load it could improve efficiency or power or distortion but probably at the expense of the other two. Not recommended, but in some cases you might find that one line length would burn up your amplifier and another wouldn't. In that case I suppose the one that didn't would be more optimum. The transistors would likely run cooler when the load at the transistors real and higher than the normal load. Because of the effect of the output networks, this point would be very difficult to find.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5106/is-there-an-optimum-transmission-line-length-for-maximum-power-transfer, by Chu, Phil Frost - W8II, K4ERO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
