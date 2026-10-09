# Electromagnetic signal from spark gap

*Tags: antenna-theory, antenna-construction, wire-antenna, frequency, lightning · score 4*

## Question

I am a power electrical engineer college student, and I have a project to make an antenna for magnetic direction finding.

My main topic is to detect lightning strikes, but its to hard due to randomness of the lightning occurence. So my lecturer suggest me to model the lightning strike into a spark gap from impulse voltage generator. I learned that lightning spark radiates electromagnetic waves on radio frequency

My question:

1. How can I know on which frequency I need to make my receiver antenna resonate?
2. Is it true that I can model lightning strike into spark gap from impulse voltage generator? (I can't just write on my paper that my lecturer told me to.)

## Accepted answer (score 6, by rclocher3)

Don't worry, there have been many researchers before you, and you can borrow some of their work. Your English is fine.

1.

If you do a web search for "lightning spectrum", you will find a graph showing lightning intensity vs. frequency. The range of frequencies emitted by lightning discharges is very broad. From amateur radio experience I can tell you that in the US, the 160m, 80m, 60m, and 40m bands (wavelengths) are difficult to use in summer because of noise from lightning.

2.

Try it and see! Build a high-voltage source, discharge it through a spark gap, and listen with a radio, such as an AM radio or shortwave radio receiver. I think that you will hear a noise.

## Answer (score 4, by Mike Waters)

**A bolt of lightning has an average center frequency of about 16 kHz**, which varies with the height of the bolt.

This is a distant stroke that I captured on one of my SDR lightning receivers, using three 4-turn 1-meter dia. vertical loop antennas, spaced 120° apart:

(Ignore the apparent 50 mV offset)


Note how the energy on this particular stroke is concentrated below 20 kHz, in the LF region (very typical). The two higher frequency, broad areas are almost certainly due to ionospheric Doppler shifting.


The harmonics extend up into to the VHF region. However, since this FFT spectrogram's vertical axis is based on power —and the filters roll off the unneeded higher frequencies— the much weaker harmonics do not display.

Having said that, occasionally I see many significant ionospherically-Doppler-shifted "bounces" up to 80 or 90 kHz. They appear as equally-spaced bell curves that decrease in height with each higher frequency-shifted bounce.

The 16 kHz figure is based on many observations of mine over a long period of time.

This signal was sent to the blitzortung.org and lightningmaps.org servers in Europe, and was displayed on the map at https://lightningmaps.org as a line from my rural location in SW Missouri to the distant (>1300 km) stroke.

**A short spark gap on a laboratory tabletop** will tend to produce much higher frequencies, unless you incorporate a suitable tuned circuit in your design. (Googling *spark transmitter* will return many designs and information from the late 18th and 19th century up to 1927.) Heinrich Hertz' first spark experiment was centered somewhere in the VHF region, IIRC.

**The antenna does not necessarily have to be resonant.** No one on the Blitzortung network uses resonant antennas. You might get more ideas if you also ask this on https://forum.blitzortung.org.

Some radio amateurs that operate on 137 kHz and 630 kHz use loop antennas with many turns of wire for receiving.

Others report success with short, high vertical antennas with a high-gain, high-impedance preamp like this one from PA0RDT.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17692/electromagnetic-signal-from-spark-gap, by Ramanda Nvl, rclocher3, Mike Waters. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
