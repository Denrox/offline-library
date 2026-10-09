# Frequency Modulated Light

*Tags: modes, optical · score 5*

## Question

I've been doing a bit of work on optical open-air transmission, and have been thinking, any hays that varies the intensity of the light or whatever else would affect the amplitude.

Would it be possible to send and receive a frequency modulated light transmission? And if so how hard would it be?

## Accepted answer (score 4, by Brian WB4ES)

Technically speaking, frequency modulation of light would involve shifting the color since, if you look at the EM spectrum, you basically see a rainbow in the visible part of it from red (lowest frequency) to violet (highest frequency). If you wanted to, you could take the original signal, run it through an analog-to-digital converter, and do the calculations to modulate the different parts of an RGB LED. The receiving side of that wouldn't be trivial, though, but it could be done.

Most light modulation that I've seen has instead been amplitude modulation. The details for the circuit would depend on what you're using for a light source, but it's basically a matter of making the light bright or dim based on the input signal. The receiving side for this could be a simple phototransistor circuit.

One possibility that would combine both would work better for digital signals, and that would be to approach it like the way that RTTY works for radio waves. Use two colors of light, the more distinguishable the better, one for your "high" and one for your "low" frequency. You then shift between the two to transmit, and use 2 phototransistor circuits behind 2 color filters matching what you're sending to receive. You would probably need to use amplitude modulation as well, if only to filter out stray light, just like IR remote controls do.

## Answer (score 3, by JanKanis)

There exist tunable lasers, where the output frequency can be modulated. And there exists such a thing as an acousto-optic modulator though I'm not sure if those are used to actually modulate the frequency of light.

Or a more D.I.Y. method could be: shine a narrow beam of continuous spectrum light (e.g. incandescent light) through a prism. Then capture a small part of the diffracted beam, e.g. by having it shine into an optical fiber, or using a small slit. When you rotate the prism a few degrees, the frequency of the captured light varies accordingly.

And accordingly to demodulate the signal: have an array of photoelectric cells and a prism in front of it. Which cell is hit by the light depends on the wavelength. Though you will then need more electronics to combine the outputs of all the cells into a single signal.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1279/frequency-modulated-light, by Skyler 440, Brian WB4ES, JanKanis. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
