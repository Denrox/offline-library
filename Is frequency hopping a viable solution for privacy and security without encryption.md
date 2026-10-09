# Is frequency hopping a viable solution for privacy and security without encryption?

*Tags: modes, security · score 7*

## Question

In terms of radio transmission, three major issues seem to arise for various sensitive transmissions:

1. Others do not gain access to the content of the message
2. Others cannot determine the location of the sender
3. Others cannot block (jam) message channels
4. Others do not know a message is being sent at all

In terms of amateur radio and non-amateur radio in different bands (if this is applicable) and different protocols/specifications (if this is applicable), how well does frequency hopping (without encryption) address each of these issues both in terms of avoiding the accidental observer, deliberate amateur (not as in amateur radio but amateur as in non-professional) observer, and determined professional government/authority observer.

**BONUS:** How well does frequency hopping work in these matters when combined with encryption?

## Accepted answer (score 7, by Kevin Reid AG6YO)

1. Others do not gain access to the content of the message

In the US amateur radio service, transmitting “messages encoded for the purpose of obscuring their meaning” is prohibited by §97.113 and specifically for spread-spectrum (SS) by §97.311. I would imagine other jurisdictions have similar rules which prohibit such transmissions and/or require that hopping patterns etc. be published.

I'll leave the detailed question of whether it is useful for this purpose when legal to others who are more familiar with the technical aspects of spread-spectrum modulation. Some remarks from general principle follow.

1. Others cannot determine the location of the sender

No method can give you this as an absolute guarantee. Someone can always take a wide-band receiver and a directional antenna and look for where the received power is higher. All that spread-spectrum gets you here is requiring the receiver to have a wider bandwidth, therefore being unable to filter out unrelated signals from other radiators, making it harder to find the transmitter at a longer distance.

1. Others cannot block message channels

Spread-spectrum techniques increase the power requirements of jamming, because the jammer must decrease the SNR sufficiently across the entire bandwidth and not just a narrow band.

1. Others do not know a message is being sent at all

This falls into the same category as point 2; as you move away from the transmitter, a spread-spectrum transmission will apparently disappear into the noise floor sooner, but if you are close enough a transmission is obvious no matter what the frequency.

For the “accidental observer” as you put it, not attempting to decode spread-spectrum transmissions, they will receive the SS transmission as a (possibly imperceptible) increase in the noise floor. Thus, spread-spectrum signals are indeed unlikely to be accidentally received (or interfered with).

## Answer (score 4, by Bradley Evans)

Frequency hopping is more typically considered an ECCM measure. That is to say that a transciever that continuously cycles frequencies in accordance with some "hop set" is more difficult to jam than a single-channel radio system. In and of itself, it doesn't constitute proper encryption of your signal -- you are still transmitting data in plain text. It would make it more difficult for unmatched hardware to receive your signal in its entirety, but considering the narrow bands of spectrum you're allowed to operate on with an amateur license I'd be extremely concerned about inadvertently causing interference as your radio hops across the spectrum.

I've only really seen freqhop implemented on the VHF spectrum as an ECCM measure, and other matched radios designed to talk on that net need carefully matched radio time (a time drift of as little as a second would cause a radio to fall out of net).

It would not obscure that you're sending a signal at all -- on the contrary, a frequency hopping radio would, to me, be quite notable and draw my attention. If your objective is to prevent your signal from being received by third party stations, the tried and true solution is to use a directional antenna. This also wouldn't run afoul of any FCC regulations and would actually help mitigate interference, in my opinion.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5224/is-frequency-hopping-a-viable-solution-for-privacy-and-security-without-encryp, by J-S, Kevin Reid AG6YO, Bradley Evans. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
