# How can I do direct digital synthesis of a 630m WSPR signal?

*Tags: digital-modes, amplifier, mf · score 10*

## Question

I want to do direct digital synthesis of a 630m band WSPR signal.

Specifically I'd like to use an Atmega 328 chip running at 20 MHz to produce such a signal.

I will use standard phase accumulator algorithm which I believe I can get to run in less than 12 cycles. This gives a frequency of 1.66 MHz.

For a target frequency of 472 kHz operation, this is 3.53 times the operating frequency.

I am not concerned with power efficiency in this design, any antenna I can use on 630m will have an radiation efficiency of less than 1%. As long as the transmitter can put out ~10 watts of power or so I should be fine.

I'll use a 24 bit phase accumulator that is truncated to access a wavetable with a length of 128. This corresponds to 7 bits, read on to figure this out. A phase accumulator of 24 bits gives me a frequency resolution of 1.6 MHz / 2^24 = 0.0993 Hz or almost 15 times the needed 1.4648 Hz precision for WSPR.

In order to generate the signal I'll need a DAC. I am choosing to use an R2R ladder made of a precision 220 ohm resistors. I will assemble a 5-bit DAC using these resistors. Given a 5 volt operating voltage, this gives me a peak output voltage of 5.0 * 31/32 = 4.84. I'm not trying to synthesize a voice signal, so "only" 32 steps of output should be acceptable.

Normally people use a DDS to generate a sine wave signal with a peak of +5 VDC from a microcontroller and a minimum of 0 volts. In my case I am going to generate a sine wave only in the region between 0 and pi. In other words, just the positive half. The wavetable will cover from 0 to 2 pi. In the wavetable of my DDS, I will include two other bits. Each bit will be driven high during half of the wavetable. So my DDS will actually generate 3 signals

- A sine wave that only goes between 0 and pi, basically just the positive part.
- A square wave with the same period as the sine wave
- A square wave 180 degrees out of phase of the other square wave.

This may seem pretty wacky, but the square waves allow me to select where my DAC's output is being sent. The goal here is to driven a two transistor pull push arrangement on a center tapped transformer. The output of the DAC is connected to two standard PNP (2N3906) transistors. When one of the square waves is high, the other is low. The one that is low turns on the corresponding PNP transistor. Each PNP transistor controls the drive circuit for the power transistor that is running half of the transformer.

This allows me to use a single DAC to control two power transistors. I was a little skeptical if this would work, but the idea seems reasonable.

The power transistor arrangement is a BC337-40 and MJE13007 in a darlington arrangement. The MJE13007 is a common power transistor from cheap ATX power supplies. 472 kHz is definitely on the upper side of what is possible with this transistor. The gain is pretty low, something like 10 in a practical circuit. The BC337-40 was the cheapest small signal transistor I could find with a large gain and large current capacity. This transistor can easily drive ~400 mA into the MJE13007.

The MJE13007 is biased using a resistive voltage divider driven by 5 volts into a 100 ohm (upper half) resistor and 12 ohm (lower half) resistor. This gives a voltage of 5.0 * 12.0/(12.0+100.0) = 0.535 V bias voltage on the transistors. I have more questions about this below. It seems to work but would be extremely sensitive to the tolerances of the resistor.

I'm going to use a crummy random iron powder toroid as the output transformer. The target values I settled on is 1400 nH for the center tapped primary and 16 microhenries for the output. The output is of course going to be 50 ohm impedance such that a standard bandpass filter for 630m can be fitted. I'm not actually building that as part of this project. If the iron powder toroid becomes an issue or a bottleneck I can always buy a decent piece of material.

The actual software that runs on the microcontroller I do not anticipate being an issue. I've reviewed some other people's work and the concepts are simple enough.

Clearly I am not going to drop an entire Atmega328 into a SPICE simulation, so in LTSpice I used a bunch of independent voltage sources to recreate what I expect out of my DAC. The definition of the MJE13007 comes directly from on-semi's website.

- V1 and V5 form the expected 0 to pi sinewave output from my DAC. The negative portion is irrelevant
- V3 and V6 form the two square waves from my DAC
- Q3 and Q6 are the "enable" PNP transistors for the darlington circuits
- Q1, Q2, Q4, and Q5 are the two darlingtons arrangements
- R2 and R8 are current limiting resistors for the base.
- L1, L2, L3 is the toroid
- R1 is my load, modeled as a 50 ohm resistor. In real life this will be an antenna
- R3, R4, R6, & R7 bias the MJE13007 transistors. V4 provides the voltage source for this. Presently 5 volts.
- V2 is the current source for the transformer. Presently 5 volts.
- R5 and R9 limit current to the "enable" transistors.

In real L2 would be a balanced output, it will not be tied back to earth at the transmitter. I just had to throw a ground on it so that LTSpice would run.

This is the output current in the load. It actually seems very reasonable. The current in R1 goes from +200 mA to -300 mA. I am a little confused as to why it doesn't show as symmetric. But since this is supposed to be a balanced output I do not suppose it would matter.

This an FFT of the current in R1. There are clear peaks at the first and second harmonic which a bandpass filter will need to remove. The third harmonic is down at -55 dB so I am not very concerned because this is smack in the middle of 160 meters. With poor antenna efficiency taken into account this would only bother other ham operators who were in my driveway.

I am confused because I expected the peak I was predicting to be at 472 kHz is instead at 450 kHz. At first I thought I had some sort of distortion going on. But I ran an FFT on the voltage of V1 (the sine wave). Instead of a 236 kHz peak I see 250 kHz peak in the FFT. Given that a voltage source is a pure sine wave in LTSpice I do not understand this. Is the problem with my circuit or is the FFT in LTSpice just buggy?

There is still more work to be done to make this a real thing, such as designing a circuit board. I am at this point trying to make sure I haven't made any large errors in this circuit or just plain made things more complex than needed. I've never build any transmitter before and I am mostly working from what parts are available to me.

**Questions**

- Should I replace V4 with an LM317 ? This way I could tune the bias voltage on Q2 and Q4 with some degree of precision. Or should I just try and bias Q1 and Q5 instead?
- R2 and R8 I think must have to be constructed from a 1000 ohm resistor in series with a 10K pot. Otherwise the variations in the BC337-40 would make the output lopsided I think. How do I determine if a potentiometer can pass a medium frequency signal?
- My DAC will need to drive an op amp to create the signal used to modulate Q1 or Q5. What op-amp is appropriate for use at 472 kHz? Rail-to-rail design is preferred.

## Answer (score 4, by Brian K1LI)

I entered your circuit into LTSpice and made some test runs to verify the following:

In order to get reasonably accurate Fourier analysis, you need to simulate at least 20 cycles. I prefer 50. And, you need to add a SPICE statement setting plotwinsize=0 to eliminate data compression that compromises Fourier analysis.

The "polarity" of V6 needs to be PULSE(0 5 ...) rather than PULSE(5 0 ...) to match the 180 degree phase shift of V5 from V1.

I find that simulating a center-tapped transformer as two series-connected transformers produces more reliable results. There's no problem placing the 50$\Omega$ load across the transformer secondary in a balanced configuration, as shown below.

This circuit produces these currents:

And so the RMS output power is a bit more than 3W (with k=1 on the transformer).

Note the sharp frequency spike at the 236kHz carrier frequency:

The only resistor I can imagine having trouble at this frequency is a wirewound. Any other type of resistor or pot should work fine. Your choice of DAC will depend on whether you want a serial or parallel data interface, as well as the "usual" parameters of bit depth, settling time, etc. The best way to choose is to search the web site of your favorite distributor.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9555/how-can-i-do-direct-digital-synthesis-of-a-630m-wspr-signal, by Eric Urban, Brian K1LI. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
