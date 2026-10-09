# Why can a monopole antenna receive wavelengths significantly longer than its physical length?

*Tags: frequency, rtl-sdr, waves · score 3*

## Question

I am new to ham radio and have been playing with a **RTL-SDR receiver** to which I have connected a vertical **1.5m monopole antenna**.

However, **I can receive transmissions belonging to the 40m band** (albeit with quite a lot of noise).

I have read in ham radio manuals that it is recommended to use a monopole of half the wavelength. But in this case, the length is much shorter.

**Why an antenna of that length is able to receive bigger waves**, is it because of the harmonics of the frequency or is it another physical phenomenon?

Thank you very much in advance.

—Fabian CD6FIQ

73

## Accepted answer (score 4, by Marcus Müller)

An antenna that's the wrong length doesn't stop being an antenna; it just becomes a less efficient antenna for the given frequency.

As a matter of fact, basically every conductor is an antenna. That's why your antenna cable cannot just be a single wire running from your RTL-SDR to the antenna; it would become part of the antenna and pick up signals, as well.

As cheap and insensitive an RTL-SDR is, compared to say your phone for cellular frequencies it's designed for, you seem to be picking up a lot of the 40 m transmission – that happens, though you could expect quite significant attenuation.

Now, it *does* also happen that transmissions on some other bands actually get mixed up in frequency, before they reach your antenna. But then you wouldn't "see" them in the 40m band, but somewhere else!

The cause for this frequency mixing would be a defect either with the transmitter, or a large antenna structure close to you, introducing nonlinearities. In the case of active components like transmitter power amplifiers, that is something you always need to take care about when designing the transmitter, and add sufficient filtering to suppress such harmonics (or else you'd be in violation of your transmitting license). In the case of passive components, like cabling, filters, and antennas themselves, there's a thing called Passive Intermodulation Products, and they happen when you either put too strong a field across a material that starts to behave non-linearily, or when corrosion on a metal connector lead to semiconductor properties. Both annoying!

## Answer (score 6, by hobbs - KC2G)

As Marcus Müller says, a small antenna is still an antenna, just a less efficient one. Adding to that: an inefficient transmitting antenna is something we try really hard to avoid if we can. An inefficient transmitting antenna means wasted power and less signal available to the receiver.

But an inefficient receiving antenna, a lot of the time, is *not a problem at all*. As long as the noise received from the antenna (natural or manmade) is significantly stronger than the thermal noise coming from inside the receiver, making the antenna more or less efficient has basically no effect on the signal-to-noise ratio, because the dominant source of noise increases or decreases proportionally to the signal. On HF and below, where the noise levels are always well above the sensitivity of modern receivers, it's perfectly fine to use an antenna that's <1% efficient for receiving.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21611/why-can-a-monopole-antenna-receive-wavelengths-significantly-longer-than-its-p, by Fabián Iglesias, Marcus Müller, hobbs - KC2G. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
