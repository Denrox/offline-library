# What does a SSB frequency actually indicate?

*Tags: modes, frequency, theory, ssb · score 12*

## Question

An SSB signal is an AM signal with the carrier and other sideband filtered out, if I understand correctly.

As such, when specifying an SSB frequency do you specify the carrier frequency, then state which sideband, or do you specify the frequency the sideband is *actually* centered on?

## Accepted answer (score 14, by user)

Normally in amateur radio when specifying a frequency you specify the nominal carrier frequency.

For SSB and other suppressed-carrier transmission modes, you specify the frequency to which the BFO needs to be tuned to re-insert the suppressed carrier. For this to work, you also need to specify which sideband you are transmitting on; lower, upper, or both. (Remember it's possible to have suppressed carrier double sideband, with identical or separate modulation of the sidebands.)

Even if you specified the center frequency rather than the suppressed-carrier frequency, you'd still need to specify which sideband you are modulating. If you get the sideband wrong, the audio will sound very strange because the demodulation will be inversed compared to the modulating signal. You can try this out for yourself by e.g. using USB to scan across the 7 MHz amateur radio band, where by convention the lower sideband is used.

For CW and other carrier-only transmission modes, it means that you specify the actual center frequency of your transmission. (It's a center frequency because the on/off keying causes sidebands to appear around the center frequency.) The receiver's actual BFO frequency is offset from this value by some amount, normally 400-700 Hz, to generate an audible tone at a reasonable frequency. Most modern transceivers allow you to configure the BFO offset for CW.

The above, combined with the fact that SSB often uses a 300-2700 Hz modulation passband, means that on SSB you normally aren't actually transmitting on the indicated frequency, only near it.

Note that other services may do things differently, and that channel-based amateur radio allocations may actually specify the center frequency rather than the BFO frequency. This is done e.g. for the 5 MHz amateur radio channels in the US, which are legally specified as center frequencies with a maximum total transmission bandwidth.

## Answer (score 5, by Phil Frost - W8II)

SSB is, as you say, half of AM, without a carrier. That's the way to think about it if you are implementing it with traditional analog electronics.

However, here's a simpler way to think about it: SSB is the baseband signal shifted up into RF. Human hearing works from about 20Hz to 20,000Hz. Human voice needs only up to about 4000Hz. So, take your voice from 20Hz to 4000Hz, and shift that up to 14,000,020Hz to 14,004,000Hz, and you have SSB. (Although you are in the CW band, I won't tell anyone.)

Specifically, this is USB. LSB is the same, except all the frequencies are backwards: higher frequency in baseband is lower frequency in RF.

The dial frequency in either SSB mode is the one that corresponds to 0Hz in baseband. So, for USB, the dial frequency is the lowest frequency in the transmission passband, and for LSB it's the highest frequency. Typically the passband is 4kHz wide to accommodate human voice with reasonable fidelity.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/954/what-does-a-ssb-frequency-actually-indicate, by Adam Davis, user, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
