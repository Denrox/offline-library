# Transmitting Morse Code as Tone vs. Carrier

*Tags: cw, morse-code · score 6*

## Question

Normal CW is just carrier on/off; this means simple transmitters are possible. The BFO of the receiver is adjusted to give a tone in the speaker within the audio passband. Narrow band filtering is done and noise performance is good.

I have seen some schemes where the carrier is Amplitude modulated with an Audio tone of say 440Hz and this is demodulated in an AM receiver. Why would one do this? Is there any communications effectiveness advantage of this tone modulated approach? Surely it uses more bandwidth with the carrier and the two sidebands which is not good, but is there any upside, even when more sophisticated demod schemes are considered?

## Answer (score 6, by tomnexus)

As a mode for communication, as you say, it's pretty redundant and inefficient. I've never heard of it being used seriously.

Occasionally people might hold a morse code practice class and transmit the sound of morse code on a 2 m FM channel. Presumably because FM radios are what the students have, and perhaps they're not yet allowed to transmit on HF. This idea could extend to AM... maybe.

But one place you will regularly hear morse code as an amplitude modulated tone, is on a Non-directional beacon. These are transmitters set up on long or medium wave, 190 - 535 kHz. An aircraft uses a direction finder to get a bearing to each beacon. This allows them to locate themselves and fly routes from beacon to beacon, pre-GPS and still today without GPS.

Each NDB in an area is assigned a different frequency, so the pilot can dial in which one they want to check, but they also identify themselves with a few morse code letters. These are amplitude modulated for identification, because they don't want to turn the carrier off at all. DF works best with a continuous carrier. The signals are strong, which is required for DF, so no problem with efficiency. And an AM tone is easy to demodulate and decode.

I used to scan around for these in my car (its radio went down to 150 kHz) and try to figure out which airport was which, based on the cryptic two letter codes.

## Answer (score 3, by Zeiss Ikon)

One significant advantage (probably the biggest one) of transmitting Morse as an AM tone rather than a simple carrier on-off is that the simplest radio receivers (crystal sets and other single-stage detectors) can receive AM, but can't hear a tone for true CW.

This is because they don't have any internal oscillator -- these simple sets just rectify the signal to high frequency pulsating DC, and depend on the physics of the circuit and the headphone or speaker to distort that into audio frequency -- but without an internal oscillator, there's no audio frequency produced by these simple receivers.

Even a "modern" (post 1930 or so) superheterodyne receiver can't make CW audible, because the internal oscillator, is at IF, 455 kHz in the common ones for broadcast band, and that can't produce an audible tone with any reasonably accessible tuning method. Rather, it depends on a detector after the internal oscillator has extracted the IF from the (usually) medium wave carrier.

AM tone Morse, on the other hand, is perfectly audible with a radio built from a pencil lead, blued razor blade (or any other slightly corroded steel), enough wire to make a tuning coil and antenna, and a high impedance earpiece.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20144/transmitting-morse-code-as-tone-vs-carrier, by Autistic, tomnexus, Zeiss Ikon. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
