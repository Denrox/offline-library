# How can I inject an oscillator output into the RF input to my radio?

*Tags: antenna, oscillator · score 5*

## Question

I have a Bodnar GPS disciplined oscillator, and I would like to inject its output into the antenna input to my HF rig. This will allow me to compare the frequency of received unknown signals to the highly accurate Bodnar signal. There are a couple of problems here. First, the Bodnar output is far more powerful than the antenna input and so must be attenuated. Second, simply joining the two wires doesn't seem appropriate because at the very least it will cause an impedance mismatch. I'm only interested in receiving in the rig, not transmitting. How would I go about doing this?

## Accepted answer (score 4, by hotpaw2)

HF receivers and antennas are usually sensitive enough to receive signals when light bulbs are used as transmit antennas, even if attached to RF sources of around 10 to 20 dBm (typical digital outputs). Instead of a light bulb, you can attach a generic 50 Ohm dummy load to the output of your signal generator. If the dummy load isn't too far from the receiver or its antenna, the receiver might pick up the signal generator signal as well as signals off of the antenna, allowing you to compare their frequencies. This "air gap" connection both attenuates the digital signal, and reduces the possibility of ground loops or other DC offsets and low frequency AC noise getting coupled into your receiver.

## Answer (score 2, by Marcus Müller)

First, to get this off my chest: The most "proper" way to be able to measure frequencies is of course to use an oscillator *derived* through ratio-guaranteeing ways from the GPS clock. That way, what your HF gear says is 30.0001 MHz is indeed 30.0001 MHz +- GPS receiver frequency error. Now, this requires a radio with a reference oscillator input that internally uses some locked-ratio synthesizer (e.g., most likely, rational or fractional-N synthesizers and/or DSP synthesis of the local oscillator). I have no idea whether that is a common feature on HF rigs. Maybe feeding in an LO directly is an option on your rig? If so, do that! Your Bodnar GPS device can generate LOs between 400 Hz and a couple 100 MHz.

Now, you're right:

First, the Bodnar output is far more powerful than the antenna input and so must be attenuated.

Luckily, SMA screw-in-line attenuators are cheap, and if you just need attenuation, and not *precise* attenuation, can be bought used / cheap.

Second, simply joining the two wires doesn't seem appropriate because at the very least it will cause an impedance mismatch.

Right, and you'd also be emitting your reference clock from your antenna!

So, honestly, as the simplest method, I'd probably use a coax / RF relay, to quickly switch between clock and antenna input.

Alternatively, you need a *directive coupler*, which *isolates* the antenna port from the oscillator port, but connects both to your rig's input. The *Wilkinson Divider* is probably the design of choice on HF:  
You'll probably need to modify it, though! Say, in the above picture, your rig is at P1, your antenna at P2 and your clock source at P3. We know that fields in transmission lines *superimpose* linearly, so we can look at the different signals in isolation first and then add up our results.

Let's assume clock source and antenna reception are on the same frequency, which has wavelength $\lambda$. Look at the clock signal fed in from S3: it has to travel half a wavelength to get to P2. Which means the exact opposite phase arrives at P3 compared to P2! "Opposite phase" just means "negative amplitude"; and in other words, the voltage between P3 and P2 is always twice the voltage of P3 in itself; so, to match a load to terminate that pair, you need twice the wave impedance. Lo and behold: that's what $2\cdot Z_0$ is. So, at that port P2, the currents and E-fields from P3 coming through the termination resistor completely cancel with the half-a-wavelength-delayed version travelling around the ring.

For symmetry reasons, the same happens to antenna-originating (i.e., coming in from P2) signals at P3. However, at P1, both of these signals just add up. For the impedance matching to work, you need that ring to be $\sqrt{2}$ the impedance of the lines going to your rig, coming from the antenna and the oscillator source. Luckily, 75Ω line is a thing, and matching 50Ω to 75/$\sqrt 2$ Ω = 53 Ω at 10 to 30 MHz takes only little effort (if you can't live with the mismatch, which reduces the isolation).

One thing, though: As you can see, the cancellation here works because the wavelengths of the signals. They don't have to be identical – all that needs to happen is that the ring's circumference is an odd multiple of half the wavelength of each. So, you need to find the least common odd multiple of both half-wavelengths.

This becomes impossible to do when these frequencies change – sure, a 1 ‰ change in frequency (say, observing the band from 30 MHz - 30 kHz to 30 MHz + 30 kHz) will only slightly affect isolation, but it will. Because the radio signal is the weaker one, and there's also a lot of attenuation on P3 to "swallow" reflections, it's more important that the ring lenght is a perfect odd multiple of the GPS oscillator's half-wavelength. So: keep that constant, otherwise you'll be emitting a nice clean reference tone on HF, and I don't think your ham neighbors want you to provide a frequency standard on the ham bands!

Another corollary of this is that you **must not** have even multiples of the fundamental frequency of your reference oscillator. But guess what: Your Bodnar GPS outputs a *square wave*; a square wave luckily is composed of only odd harmonics,

$$s(t) = \frac{4}{\pi} \sum_{\ell=1}^\infty \frac{\sin\left(2\pi(2\ell - 1)ft\right)}{2\ell - 1}.$$

Since you still don't want to have high odd multiples (and even multiples, due to physics forbidding any square wave to be *perfectly* square) leaking around your system, you'd want to not only keep your GPS frequency fixed, but also have a good low-pass filter that filters out anything above the fundamental frequency (i.e., the frequency you want to compare to). The good thing is: this is relatively low-frequency, low power, and hence, a simple RC low pass filter with a a cutoff frequency slightly above your desired frequency can do that. As a bonus, you can design that filter to "as a byproduct" match 50Ω to 53Ω!

## Answer (score 2, by hobbs - KC2G)

The *really* simple option: make a coil out of a few turns of wire and connect it to the coax with the 10MHz, then lay the coil right on top of your radio's case. I bet you'll get enough signal leaking into the radio to serve as a marker, without the danger of overloading the radio, blowing up the Bodnar GPSDO, or radiating any noticeable amount of power out the antenna.

Feel free to experiment with the specs of the coil, but a starting point might be 4 turns of the thinnest insulated/enameled wire you have on hand, in a loop with a diameter of 5cm or so, and the turns laid right on each other (negligible "length"/"thickness" to the coil). You can either strip a piece of coax and connect it to the loop directly, or use one of those cheap ubiquitous BNC to binding-post adapters.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21191/how-can-i-inject-an-oscillator-output-into-the-rf-input-to-my-radio, by Bill KG5RMJ, hotpaw2, Marcus Müller, hobbs - KC2G. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
