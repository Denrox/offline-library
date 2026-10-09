# Images up and down the spectrum

*Tags: rtl-sdr · score 5*

## Question

I brought an rtl-sdr USB stick to a foreign country. I am listening with gqrx, and I am surprised to find audio (e.g. television or radio) up and down the spectrum, up to 600, 700 and 800 MHz ranges. I haven't experienced this in the States. I can tune up and down several MHz (between say 7 and 20 MHz) and come across the same and different signals at what seem like multiples (I don't have to fine-tune, just tune several MHz at a time.) They are all WBFM signals What might cause this?

## Accepted answer (score 4, by Phil Frost - W8II)

Sounds like the receiver is being overloaded by a strong station.

Those inexpensive RTL receivers work by feeding the RF into a quadrature mixer to downconvert the frequency, and then into a pair of analog to digital converters (ADCs). At that point the data are processed by computer software that does all the filtering and demodulation.

Those ADCs have a limited range: 0 is only so small, and 0xFFFF (for a 16 bit ADC) is only so big. Any input outside of this range gets clipped.

Clipping is what we call it in the time domain, where it looks like someone clipped off the tops and bottoms of all the peaks with scissors. In the frequency domain, this generates a bunch of harmonic images. Here's a spectogram of a 40 Hz sine wave that has been clipped:

You can see here that the 40 Hz signal is repeated at each odd harmonic:

- 120 Hz (40*3)
- 200 Hz (40*5)
- 280 Hz (40*7)
- etc...

This is the same harmonic progression as a square wave. This makes sense: if you clip a sine wave enough, it becomes a square wave. The spectogram above has a logarithmic frequency scale. On a linear frequency scale, the harmonics look evenly spaced:

SDRs have particular difficulty with this problem because their input bandwidth is so large. A wider input bandwidth means more power is making its way to the ADC. When there's too much power, you get clipping. Your software may be tuned to a 15 kHz channel somewhere in the spectrum, but the filtering that selects that one channel happens *after* the ADC. A much wider bandwidth (as wide as the sample rate of the ADCs) reaches the ADCs. Thus, even if the very strong station isn't the one you are listening to, it can still overload the ADC and cause clipping, which causes harmonic distortion all across the input bandwidth.

You can address this problem by attenuating the RF input until the distortion goes away. More sophisticated radios have automatic gain control (AGC) which does this automatically, but the RTL is built to be cheap, not sophisticated. You can then run into a problem where you've eliminated the distortion, but now weaker stations are attenuated so much that they are below the receiver's noise floor and are thus unreceivable. This is called desensitization. The range between the noise floor and clipping is called dynamic range, and is sometimes specified as a figure of merit for receivers.

A better solution is to use a higher resolution ADC. If you had a 16 bit ADC, you could only go up to 0xFFFF. With a 32 bit ADC, you can go up to 0xFFFFFFFF. That means the peak signal can be higher before you run into clipping. See [SDR sampling bandwidth - do the bits per sample matter?](SDR%20sampling%20bandwidth%20-%20do%20the%20bits%20per%20sample%20matter.md)

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2446/images-up-and-down-the-spectrum, by Ken - Enough about Monica, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
