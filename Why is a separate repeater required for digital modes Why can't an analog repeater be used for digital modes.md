# Why is a separate repeater required for digital modes? Why can't an analog repeater be used for digital modes?

*Tags: digital-modes, repeater · score 3*

## Question

Regardless of the mode: digital or analog, the radios always transmit sinusoidal EM waves. So wouldn't a regular analog repeater be able to rebroadcast that EM signal regardless of its encoding?

## Accepted answer (score 11, by Phil Frost - W8II)

There is a kind of repeater that can repeat any kind of transmission: it's called a *linear translator*. It's technically equivalent to an SSB receiver linked to an SSB transmitter. It works for any mode because SSB is simply a shift in frequency. Other than the change in frequency, the baseband and RF signals are linearly related. This is also why an SSB tranciever can be used to implement any digital mode, like PSK-31, FT8, and so on. The only requirement is the SSB radio's bandwidth needs to be wide enough to accommodate the mode.

This linear relationship does not exist for FM. For FM, only the phase of the input is relevant, and so as part of the demodulation process information about amplitude is lost. This means an analog FM repeater can't repeat any mode: it can only repeat modes that don't rely on changes in amplitude.

Theoretically this means an FM repeater could be used for some but not all digital modes. In FM demodulation, higher deviation in the RF signal relates to higher amplitude in the baseband signal. If the repeater includes any kind of AGC this will result in the input and output RF signals differing in deviation. Some digital modulations rely on the deviation to be some precise value, and so this further reduces the set of possible digital modulations that an analog repeater can repeat.

Besides AGC, an analog repeater might have additional filtering which distorts the digital modulation in ways that prevent demodulating it.

Finally, even for modulations that can still pass successfully through this repeater, there are significant technical advantages to using a purpose-engineered digital repeater. An analog repeater, with no knowledge of the modulation or coding of the signal, can only repeat exactly what it received, noise included. A digital repeater however can demodulate and decode the signal to recover the original digital message, then re-encode and re-modulate it, re-transmitting an equivalent signal with no noise. This significantly extends the useful range of the repeater.

## Answer (score 2, by MacGuffin)

Part of what makes a repeater valuable is it filters out "invalid" or weak signals. This makes them efficient in power use as it's not transmitting all the time. This makes them valuable to the users as they aren't hearing noise all the time through their radios.

What makes the signal "valid" is having sufficient power, at the correct kind of modulation, and often with other factors like a PL tone. Once it is considered "valid" then it repeats the incoming signal on its outbound channel.

There are repeaters made to repeat digital and analog signals, they are still transmitting a phone mode but with the "valid" signal being FM or a specific digital phone mode. Depending on how the repeater is configured it can then transmit the same signal it receives or convert the audio to FM for backward compatibility with those that have not yet upgraded to digital radios.

A digital signal can be sent through an analog repeater but it must be done in a way that is compatible with the analog systems it uses. A series of DTMF tones is a simple example of digital information sent by an analog repeater.

A linear translator can retransmit an analog or digital signal, as pointed out by W8II in another answer, but this comes with costs. A linear translator will retransmit the noise with the signal. An analog repeater will do this as well to some extent but the noise is not retransmitted constantly and the inherent filtering of demodulating and remodulating filters some noise. A digital repeater will cut out more of the noise because of this same demodulation and remodulation. Without that filtering the increased range benefits of a repeater will be diminished.

Linear translators are still used and considered superior in many applications from a repeater precisely because it doesn't try to demodulate. This means it will work with any kind of modulation so long as it fits within the frequency, power, and other limits of the translator.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16554/why-is-a-separate-repeater-required-for-digital-modes-why-can-t-an-analog-repe, by rsn, Phil Frost - W8II, MacGuffin. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
