# Why don't I hear the CTCSS tones when listening on the repeater input frequency?

*Tags: repeater, uv-5r, tone-squelch · score 8*

## Question

I am newly licensed (Technician) and bought a UV-5RA as a cheap way to check out what's going on in my area and see if I'm finding it interesting enough to get a better UHF/VHF HT.

The other day I was listening to a conversation happening on a local repeater and when one of the guys gave their call I looked it up for the heck of it and it turned out he was near me. That made me curious to see if I could receive him directly, so I switched the radio from "channel" mode to "free-tune" mode and tuned to the repeater's receive frequency.

Turned out I could hear him. However, I could not hear a CTCSS tone on his transmission. The repeater in question uses one (I checked in the local listings and on RepeaterBook) so the person talking through the repeater had to be transmitting one. And according to various references, the tones run (approximately) from 67Hz to 250Hz.

Those frequencies are well within the human range of hearing (for example, the fundamental frequency for adult male speech is generally in the 85-180Hz range), so why didn't I hear them when listening to the repeater receiver frequency?

Similarly, when doing some UV-5R receive testing by transmitting to it from an old Motorola GMRS Talkabout (I know not to transmit back to it) I did not hear any tones, even though the Talkabout has PL turned on.

Is it as simple as the CTCSS tone is simply transmitted at a such low intensity level that it is hard to hear? Or is something else going on?

## Accepted answer (score 10, by user3486184)

Many radio manufacturers are aware that people don't want to hear CTCSS tones - so they put high-pass filters on both the output (speaker) and input (microphone).

That eliminates the tone before it gets to your ears, and will also prevent an errant tone near the microphone from triggering a repeater somewhere.

Some of us might not agree that the tones are within human hearing range - at least, not all of them for all of us!

## Answer (score 4, by user10489)

The volume of the tones is typically low enough with respect to the voice signal that you can't hear it. Occasionally the tone generator in a radio will be poorly calibrated, and you do hear it.

Usually the radio has a tone scan function, and you can use that to find out what tone is being used. You can also turn on tone squelch if you have the tone set correctly, and if it is there, the radio will not block the signal.

Repeaters frequently filter out tones on the incoming signal and then add it back in on transmit. This allows using a different tone on input and output, although this is rare. Many repeaters and nearly all regular radios just pass the tone through without attempting to filter it.

## Answer (score 3, by hotpaw2)

Same with SDR software. My SDR code runs on a iPhone that's connected to "HiFi" audio transducers. So I had to add a 270 Hz high-pass biquad IIR audio filtering subroutine to get rid of annoying hum when listening to NFM from local 2M repeaters. (I obviously switch that subroutine out when listening to broadcast wideband FM music.)

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18316/why-don-t-i-hear-the-ctcss-tones-when-listening-on-the-repeater-input-frequenc, by QuantumMechanic, user3486184, user10489, hotpaw2. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
