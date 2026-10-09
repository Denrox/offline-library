# How does tuning in 2.4 GHz Wifi radios work?

*Tags: wifi · score 4*

## Question

I'm working with a Wifi chipset that has very poor documentation and I was wondering whether I should wait a bit after switching the channel or if I can send a Wifi frame right away.

That's when I realized that I have no idea how tuning in Wifi radios actually works. Is there some kind of VCO that is physically adjusted to select a channel or is channel selection somehow part of the modulation (that is technically possible, isn't it)?

## Answer (score 5, by Marcus Müller)

Nobody can tell you how *your* specific 2.4 GHz Wifi chip works, as we don't know it, let alone its internals. However, reasonable assumptions can be made:

WLAN of the IEEE802.11a variant has been designed with direct conversion receivers in mind, so for downmixing to an Inphase and Quadrature component using a quadrature mixer; the I and Q components would then be, pretty much directly, be sampled by a two-channel DAC simultaneously, which also runs at the OFDM system bandwidth as sampling rate. A classical direct conversion receiver, as you'll find in a modern digital communications textbook!

If we assume that your modern receiver still adheres to the same design principle that was in the back of the mind of the people standardizing the waveform (that's not a given – communication standards specify *what* to transmit and receive, but by no means *how*), that will be the case for your receiver as well.

So, there will be an integrated mixer which needs to be fed with an local oscillator of the target frequency (e.g., 2440 MHz), and a 90° phase-shifted version of the same. Luckily, that's easy to create using a PLL on integrated circuitry, but it's not telling us whether the LO is going to be something rectangular created through saturating CMOS logic, or with something more sinusoidal as a nice analog VCO with a tank capacitor, transistors in their linear region and a control voltage directly modulating the circuit would give.

Now, what's smaller (and hence cheaper to integrate on a semiconductor die)? Probably the rectangular wave created through means of counting and XOR rectangular oscillations. Also, that would make things easier to control programmatically than a classical VCO would be (as that would need a DAC, some amplifier for that, and multiple feedback loops to achieve the required stability). Again, this is getting more speculative: I certainly don't know what the design elements that intel, atheros, apple, espressif, broadcom, qualcomm, … are using in their chips are doing, and I'd assume you find very different solutions to this problem. Even if it is just to avoid someone else's patent on a single approach!

So, let's assume this is a rectangular LO; that's fine, as with any mixer, you need to get rid of unwanted harmonics through filtering anyways.

The required frequency agility would suggest an integer-N synthesizer: The possible LO frequencies all fall into a fixed raster, and could be generated from a single reference oscillator (e.g. at 10 MHz). So, there's no need for the more flexible fractional-N synthesizer, which tends to (at same implementation effort, cost) have higher spurs. Both architectures *still* include a VCO, but it's probably not the kind of VCO from your ham textbook, but not too dissimilar. From page 9 of the TI appnote on Integer-N and Fractional-N Synthesizers I've linked to above:

However, the crux of any receiver architecture's frequency synthesis is how to deal with correction of frequency error. (Your signal reception, especially in case of IEEE802.11a, will allow you to tell pretty exactly how much your receiver's frequency is "off" relative to the transmit frequency.)

Now, one could implement the reference clock (from which the 2.4 GHz-range frequencies are generated) as VCO itself. That, however, is a solution that is often not very desirable – the reference oscillator is one of the few things you typically can't integrate into the chip die itself, as it's a cut crystal (or MEMS silicon device) in its core, and thus not possible to make in the same semiconductor device production process as the rest of the chip. So, you'd need to deal with an off-chip VCO, with unknown characteristics and spurs. Also, you'd again need a very fine DAC to make fine adjustments.

The alternative is to digitally fine-adjust the receive frequency, simply by calculating the error frequency and applying a correction, simply by multiplying the complex-valued sample stream from the I/Q-DAC with a complex oscillation $e^{-2\pi j f_{\text{error}}t}$; while that certainly is a lot of multiplications per second (20, 40 or 80 million complex multiplications per second, to be precise), but since these happen on digital numbers, that's easy to integrate into a digital chip – and thus technologically and economically feasible.

On the other hand, in a direct conversion receiver, the leakage of the local oscillator through the mixer ends up at 0 Hz, just like static ADC offsets, and thus are easy to correct – but even easier to ignore: in wifi a.k.a. IEEE802.11a, the DC carrier of the OFDM frame is simply unused on transmit site, and thus ignored at receive side. 0 Hz hits that perfectly, and thus has absolute no influence on any on the data-carrying OFDM subcarriers whatsoever. That solves the need for LO leakage and DC offset cancellation completely, without costing anything. If, however, you need to correct your frequency after sampling digitally, that 0 Hz artifact suddenly ends up at $-f_{\text{error}}$, and you will need to cancel it, or it *will* interfere with data.

So, you're basically facing the choice of either making your digital receiver a significant bit more complicated by adding compensation for these imperfections, or you would need a more finely adjustable LO syntesizer. Fractional-N synthesizers *are* that solution, and complexity-wise not much worse than Integer-N, but as said, come with more spurs, and thus, more need for filtering, which again is hard to integrate on chips.

So, as you can see, one can't *really* tell you what happens in the specific IC *you* are considering (unless one happens to be a designer that worked on said IC), but one can make reasonable assumptions, and can point out possible choices and resulting technical necessities.

It's also worth stressing that any specific communication method doesn't *dictate* a specific solution, but standards were often designed with technical possibilities in mind. But the technical feasibilities change, and I promise you, while your modern phone can still work GSM (2G) cellular networks, it doesn't work the way that the architects of the GSM waveforms envisioned, at all (they really assumed the demodulation would happen in discrete components, and that waveforms would need to be designed for the ability of such simple analog circuits to do that), but much more generally in software-defined radio subsystems within your phone's sytem-on-chip that encompasses the whole cellular and WLAN and bluetooth processing, for multiple versions of these standards. So, it's really not impossible that your wifi chip does something completely different than what I described here – it's just not, to the best of a wireless engineer's ability to guess from what he's seen – very likely that the LO synthesizer methods have been fundamentally replaced by other principles.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21330/how-does-tuning-in-2-4-ghz-wifi-radios-work, by AndreKR, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
