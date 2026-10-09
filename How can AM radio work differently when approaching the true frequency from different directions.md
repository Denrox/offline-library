# How can AM radio work differently when approaching the true frequency from different directions?

*Tags: receiver, am, swl · score 5*

## Question

I bought a very cheap world band receiver, Nedis RDWR1000GY. It has MW, SW and FM reception. MW is useless where I live (no MW stations nearby and signals don't propagate far), but I was primarily interested in the SW and FM reception. The FM reception is advertised as PLL. My primary aim was to increase battery life for power outages compared to my Degen DE1103, that eats 4 AA's in less than 40 hours whereas the Nedis eats 2 AA's in 60 hours when doing FM reception.

The SW reception seems to not be very selective. If there's a station at 7220 kHz, I can often hear it at 7215 kHz too.

However, there's a peculiar feature in the shortwave AM reception of this radio. If there's a station at 7220 kHz, and I tune in first to 7220 kHz, then down to 7215 kHz, I will hear the radio station. However, if I tune in first to 7210 kHz, then up to 7215 kHz, it usually doesn't receive the signal at 7220 kHz well.

What could explain this peculiar feature in AM shortwave reception? I can understand it for PLL FM reception, but for AM it seems strange.

I understand that most AM radios are superheterodyne radios. A superheterodyne radio should convert the signal to an intermediate frequency with a voltage controlled or digitally controlled oscillator and a mixer, filter out undesired frequencies, and then use envelope detector to detect the signal. However, a superheterodyne radio shouldn't work differently when approaching a frequency from different directions, right?

Could the radio be a direct conversion radio, with a phase-locked loop where a local oscillator tracks the remote transmitter oscillator, and then directly converts the signal to baseband with a mixer? Then the phase-locked loop might lock differently to the transmitter signal when approaching the frequency from different directions.

If it helps, the radio consumes (FM reception) 40 mA at 3 V DC nominal (although when batteries run out it has to operate close to 2 V DC). It really requires batteries, if I use the DC connector with a SMPS having lots of ripple noise, I can no longer hear the weakest stations that I can hear with batteries although strong stations can be heard with a noisy SMPS.

Also, the radio is small, far smaller than DE1103, in case this could be a clue for how the radio works. It's about the size of a mobile phone but twice as thick.

## Accepted answer (score 4, by Marcus Müller)

I can tell you of how your radio is built: It's got an integrated radio IC that does everything, from preselection to mixing (if any) to digitization to digital filtering, audio demodulation, audio enhancement. That's how you get the good battery life!

if I use the DC connector with a SMPS having lots of ripple noise, I can no longer hear the weakest stations that I can hear with batteries although strong stations can be heard with a noisy SMPS.

And: it's a low-cost solution (you can see that starting at the type of batteries it uses – AA batteries are not really "state of the art" when you need a lot of energy on limited space, but including a lithium battery, necessary charging and protection circuitry would have just increased the price. Same about compactness – this device could be much smaller than a smartphone, but then people wouldn't buy it, and it would be more expensive to manufacture. This has effect on what the frontend is designed to provide in terms of selectivity. And of course, there's not a lot of supply voltage filtering. Who's got money for that?

There's probably many chips that could provide this functionality, especially on the internal Chinese market, into which I, lacking basic language abilities, have no real insight. If you want to see an example of an IC from an international company, consider the Skyworks Si4735.

What could explain this peculiar feature in AM shortwave reception? I can understand it for PLL FM reception, but for AM it seems strange.

That's a nice firmware bug, probably, and an interesting puzzle about what you can infer about the used digital / hybrid hardware's architecture. The honest truth is that probably a designer, either on the side of the central IC in your device, or on the side of whoever took that IC and made a consumer product around it, made a mistake.

AM selectivity is probably implemented through a digital filter, and there might be multiple of these implemented in the software running in this device, or one adjustable one, and something goes wrong when you "tune in from the wrong end".

Or, really, anything. Really sounds like a bug.

I understand that most AM radios are superheterodyne radios.

As wikipedia would say, [citation needed]. Short wave is something you could reasonably well directly sample, which is quite an attractive approach in a highly-integrated IC that only receives SW. However, you're probably right, it's also trivial to chopper-mix down, so hm. Might be right, might not be right.

For example, the Si4735 I mention above has this architecture:

That doesn't look like a classical superhet to me! (It actually *is* a superhet, of kinds, because this is a low-IF $\eqref{1}$ quadrature mixer, but it's not using the architecture for the same reasons you usually use a superhet, and hence, the filtering is different, slightly.)

(You can find an example schematic of how to build the full multiband receiver on page 18 of the datasheet I've linked to above. Antenna matching, and audio amplification, nonwithstanding, that's 1 Receiver IC, 5 passives, and a microcontroller that speaks I²C to control the receiver. I'd actually say: you could build that radio you have yourself! (It's also

A superheterodyne radio should convert the signal to an intermediate frequency

yep.

with a voltage controlled or digitally controlled oscillator

or with just a fixed oscillator. And I don't know whether an oscillator implemented and adjusted by the timer unit of a microcontroller-style device would be called a "digitally controlled oscillator", but that's semantics.

Point is: A superhet has a mixing stage to an IF. How that is implemented is up to design.

filter out undesired frequencies,

That's usually the reason why going to a fixed IF is desirable, indeed!

and then use envelope detector to detect the signal.

Hm, no. That *can* be one way of implementing it. It's easier than the alternatives if you're in the 1950s.

In reality, for the last ca 2 to 3 decades, integrated receives will simply sample the IF with an ADC and then have a digital IF or equivalent complex baseband signal to do the rest of the processing.

So, in general, you can't claim that. A product detector, or any combination of these two principles, is equally likely. Since we're doing this on an IC, honestly, the product detector *might* even be easier (no nonlinear function, less filtering, just a multiplication with a digital oscillation).

That's also where the PLL might come in. It's generally useful to have a PLL to lock onto your transmission's carrier, right, so that you don't have to tune as precisely, and so that oscillator drift doesn't make your reception worse over time.

If you have a PLL, then you already have the thing that generates the oscillation a product receiver needs.

However, a superheterodyne radio shouldn't work differently when approaching a frequency from different directions, right?

I'd agree with the *should*, but if it's not designed that way, for example because something's a bit off about the loop filter, or the oscillator has a bias in one phase direction, then that's not what you observe.

Could the radio be a direct conversion radio, with a phase-locked loop where a local oscillator tracks the remote transmitter oscillator, and then directly converts the signal to baseband with a mixer?

As said above, I don't know which chip your radio is using, but if that chip happens to be architected the way the Si473x is: yeah, but no!

There's a phase-locked loop, but it's likely controlled from further down the receiver chain, where you have the filtered signal, already, and hence get a better SNR. It's a digitally-controlled / generated oscillation, and not something attached more or less directly to the antenna. And as mentioned, low-IF, not usually baseband. (Baseband comes with many problems for such receivers, namely DC offset and problems with phase and amplitude uniformity in the lowest frequency components. For bandwidths so trivially low, it's easier to have an I and Q, which are not actually baseband. (works really the same as the direct conversion quadrature mixer, just that you don't mix to 0 Hz, but a bit above. In the case of LW reception, you'd actually mix up, most likely, not down ;) )

This used to be a Silicon Labs device, but they moved that part of their business to Skyworks

$\tag1\label1$ J. Crols and M. S. J. Steyaert, "Low-IF topologies for high-performance analog front ends of fully integrated receivers," in IEEE Transactions on Circuits and Systems II: Analog and Digital Signal Processing, vol. 45, no. 3, pp. 269-282, March 1998, doi: 10.1109/82.664233. available online

## Answer (score 3, by timetraveller)

Your radio, as do many of the inexpensive portables over the last five years or so, uses the Silicon Labs Si473x DSP chip or one of the recent Asian clones.

Tuning is controlled entirely by software. SiLabs provided default control software for all their chips, but the end-user could also custom-program them too.

AM tuning with these DSP chips is quirky at best. The 473x chips have the ability to be tuned digitally or (the 483x chips) more simply through an analog potentiometer mechanism (a 100 K pot). Before audio is presented to the listener as he or she tunes, software must determine if a valid station has been captured.

Valid station status primarily depends on three things:

1. RSSI, or signal strength must be above a predetermined software-set threshold.
2. SNR, or signal-to-noise ratio must be above a predetermined software-set threshold.
3. AFC, or automatic frequency control settings will have effect on internal auto-tuning.

Depending on the internal bandwidth setting being used in your radio (these chips typically have selectable bandwidths of 1-6 KHz), with consumer-grade radios likely set at 6 KHz, it is quite possible that tuning down from a strong station to a "vacant" channel might still present enough signal strength from the strong channel for the radio to auto-tune using AFC back to the peak signal. Tuning by approaching from the other direction may negate this effect.

Further complicating tuning, additionally a new function was unleashed on the listening world called Soft Mute which limits the ability to hear weaker signals.

What is soft mute?

Soft-mute is a further lowering of the audio level of the received signal when it drops below a prescribed signal-to-noise ratio. It was implemented in consumer grade DSP radios to provide a more "comfortable listening experience" for the casual listener and not the DXer. The idea is to relieve the listener from all that nasty low level "static" and "interference", or as Silicon Labs states: "....to attenuate the audio outputs and minimize audible noise in compromised signal conditions."

The soft mute feature is triggered by the SNR (signal-to-noise) metric. The software reads the quality of the signal through its SNR value and makes soft mute changes accordingly. The SNR threshold for activating soft mute is programmable, as are soft mute attenuation levels, attack/release rates and attenuation slope.

Soft mute may or may not be activated in your radio. It's up to the firmware programmer. Soft mute can and will mask weaker stations, and particularly weaker stations next to stronger stations.

I've had numerous inexpensive small portables using the SiLabs chips/clones, some digitally tuned and some analog tuned through a potentiometer. Most suffer to varying degrees from the anomaly you describe, particularly the analog tuned ones. Even worse is trying to receive a weak station between two strong channels. Tuning is forced to the stronger channel. The only radios I have currently which seem to have conquered this problem are the C.Crane CCRadio EP Pro, a tabletop-sized analog tuned portable at about $100, and the RadiWow R-108 digitally tuned portable. Both use a version of the SiLabs DSP chip/clone. The CCSkywave, another C.Crane radio, is most likely okay as well. I'm sure there are others.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21422/how-can-am-radio-work-differently-when-approaching-the-true-frequency-from-dif, by juhist, Marcus Müller, timetraveller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
