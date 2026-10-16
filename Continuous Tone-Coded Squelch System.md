# Continuous Tone-Coded Squelch System

In telecommunications, **Continuous Tone-Coded Squelch System** or **CTCSS** is one type of in-band signaling that is used to reduce the annoyance of listening to other users on a shared [two-way radio](Two-way%20radio.md) communication channel. It is sometimes referred to as **tone squelch** or **PL** for Private Line, a trademark of Motorola. It does this by adding a low frequency audio tone to the voice. Where more than one group of users is on the same radio frequency (called *co-channel users*), CTCSS circuitry mutes those users who are using a different CTCSS tone or no CTCSS.

CTCSS tone codes are sometimes referred to as **sub-channels**, but this is a misnomer because no additional radio channels are created. All users with different CTCSS tones on the same channel are still transmitting on the identical radio frequency, and their transmissions interfere with each other. However, this interference can be masked under most conditions. Although it provides some protection against interference, CTCSS does not offer any security against interception or jamming, and receivers without CTCSS enabled will still hear all traffic.

A receiver with just a carrier or noise [squelch](Squelch.md) does not suppress any sufficiently strong signal; in CTCSS mode it unmutes only when the signal also carries the correct sub-audible audio tone. The tones are not actually below the range of human hearing, but are poorly reproduced by most communications-grade speakers and are usually filtered out before being sent to the speaker or headphone.

### Theory of operation

Radio transmitters using CTCSS always transmit their own tone code whenever the transmit button is pressed. The tone is transmitted at a low level simultaneously with the voice. This is called CTCSS *encoding*. CTCSS tones range from 67 to 254.1 Hz. The tones are usually referred to as *sub-audible tones*, since the audio circuit filters them out.

In an FM two-way radio system, CTCSS encoder levels are usually set for 15% of system deviation. For example, in a 5 kHz deviation system, the CTCSS tone level would normally be set to 750 Hz deviation. Engineered systems may call for different level settings in the 500 Hz to 1 kHz (10–20%) range.

The ability of a receiver to mute the audio until it detects a carrier with the correct CTCSS tone is called *decoding*. Receivers are equipped with features to allow the CTCSS "lock" to be disabled. On a base station console, a microphone may have a split push-to-talk button. Pressing one half of the button, (often marked with a speaker icon or the letters "MON", short for "MONitor") disables the CTCSS decoder and reverts the receiver to hearing any signal on the channel. This is called the *monitor* function. There is sometimes a mechanical interlock: the user must push down and hold the monitor button or the transmit button is locked and cannot be pressed. This interlock option is referred to as *compulsory monitor before transmit* (the user is forced to monitor by the hardware design of the equipment itself). On mobile radios, the microphone is usually stored in a hang-up clip or a hang-up box containing a microphone clip. When the user pulls the microphone out of the hang-up clip to make a call, a switch in the clip (box) forces the receiver to revert to conventional carrier squelch mode ("monitor"). Some designs relocate the switch into the body of the microphone itself. In hand-held radios, an LED indicator may glow green, yellow, or orange to indicate another user is talking on the channel. Hand-held radios usually have a switch or push-button to monitor. Some modern radios have a feature called "Busy Channel Lockout", which will not allow the user to transmit as long as the radio is receiving another signal.

A CTCSS decoder is based on a very narrow bandpass filter which passes the desired CTCSS tone. The filter's output is amplified and rectified, creating a DC voltage whenever the desired tone is present. The DC voltage is used to turn on, the tone is present and the receiver is unmuted, when it is not present the receiver is silent.

Because period is the inverse of frequency, lower tone frequencies can take longer to decode (depends on the decoder design). Receivers in a system using 67.0 Hz can take noticeably longer to decode than ones using 203.5 Hz. In some repeater systems, the time lag can be significant. The lower tone may cause one or two syllables to be clipped before the receiver audio is unmuted (is heard). This is because receivers are decoding in a chain. The repeater receiver must first sense the carrier signal on the input, then decode the CTCSS tone. When that occurs, the system transmitter turns on, encoding the CTCSS tone on its carrier signal (the output frequency). All radios in the system start decoding after they sense a carrier signal then recognize the tone on the carrier as valid. Any distortion on the encoded tone will also affect the decoding time.

Engineered systems often use tones in the 127.3 Hz to 162.2 Hz range to balance fast decoding with keeping the tones out of the audible part of the receive audio. Most amateur radio repeater controller manufacturers offer an audio delay option—this delays the repeated speech audio for a selectable number of milliseconds before it is retransmitted. During this fixed delay period (the amount of which is adjusted during installation, then locked down), the CTCSS decoder has enough time to recognize the right tone. This way the problem with lost syllables at the beginning of a transmission can be overcome without having to use higher frequency tones.

In early systems, it was common to avoid the use of adjacent tones. On channels where every available tone is not in use, this is good engineering practice. For example, an ideal would be to avoid using 97.4 Hz and 100.0 Hz on the same channel. The tones are so close that some decoders may periodically false trigger. The user occasionally hears a syllable or two of co-channel users on a different CTCSS tone talking. As electronic components age, or through production variances, some radios in a system may be better than others at rejecting nearby tone frequencies.

#### Digital-Coded Squelch

CTCSS is an analog system. A later Digital-Coded Squelch (DCS) system was developed by Motorola under the trademarked name Digital Private Line (DPL). General Electric responded with the same system under the name of Digital Channel Guard (DCG). The generic name is CDCSS (Continuous Digital-Coded Squelch System). The use of digital squelch on a channel that has existing tone squelch users frequently precludes the use of the 131.8 and 136.5 Hz tones as the digital bit rate is 134.4 bits per second and the decoders set to those two tones will sense an intermittent signal (referred to in the two-way radio field as "falsing" the decoder).

### List of tones

CTCSS tones
- NS    PL   Hz   Notes
- 1   XZ   67.0
- 39   WZ   69.3
- 2   XA   71.9
- 3   WA   74.4
- 4   XB   77.0
- 5   WB   79.7
- 6   YZ   82.5
- 7   YA   85.4
- 8   YB   88.5
- 9   ZZ   91.5
- 10   ZA   94.8
- 11   ZB   97.4
- 12   1Z   100.0
- 13   1A   103.5
- 14   1B   107.2
- 15   2Z   110.9
- 16   2A   114.8
- 17   2B   118.8
- 18   3Z   123.0
- 19   3A   127.3
- 20   3B   131.8
- 21   4Z   136.5
- 22   4A   141.3
- 23   4B   146.2
- NATO      150.0
- 24   5Z   151.4
- 25   5A   156.7
- 40      159.8
- 26   5B   162.2
- 41      165.5
- 27   6Z   167.9
- 42      171.3
- 28   6A   173.8
- 43      177.3
- 29   6B   179.9
- 44      183.5
- 30   7Z   186.2
- 45      189.9
- 31   7A   192.8
- 46      196.6
- 47      199.5
- 32   M1   203.5
- 48   8Z   206.5
- 33   M2   210.7
- 34   M3   218.1
- 35   M4   225.7
- 49   9Z   229.1
- 36   M5   233.6
- 37   M6   241.8
- 38   M7   250.3
- 50   0Z   254.1

CTCSS tones are standardized by the EIA/TIA. The full list of the tones can be found in their original standard RS-220A, and the most recent EIA/TIA-603-E; the CTCSS tones also may be listed in manufacturers instruction, maintenance or operational manuals. Some systems use non-standard tones. The NATO Military radios use 150.0 Hz, and this can be found in the user manuals for the radios. Some areas do not use certain tones. For example, the tone of 100.0 Hz is avoided in the United Kingdom since this is twice the UK mains power line frequency; an inadequately smoothed power supply may cause unwanted squelch opening (this is true in many other areas that use 50 Hz power). Tones typically come from one of three series as listed below along with the two character PL code used by Motorola to identify tones. The most common set of supported tones is a set of 39 tones including all tones with Motorola PL codes, except for the tones 8Z, 9Z, and 0Z (zero-Z). The lowest series has adjacent tones that are roughly in the harmonic ratio of 2 to 1 (≈1.035265), while the other two series have adjacent tones roughly in the ratio of 10 to 1 (≈1.035142). An example technical description can be found in a Philips technical information sheet about their CTCSS products.

### Reverse CTCSS

Some professional systems use a phase-reversal of the CTCSS tone at the end of a transmission to eliminate the squelch crash or squelch tail. This is common with General Electric Mobile Radio and Motorola systems. When the user releases the push-to-talk button the CTCSS tone does a phase shift for about 200 milliseconds. In older systems, the tone decoders used mechanical reeds to decode CTCSS tones. When audio at a resonant pitch was fed into the reed, it would resonate, which would unmute the speaker audio. The end-of-transmission phase reversal (called "Reverse Burst" by Motorola (and trademarked by them) and "Squelch Tail Elimination" or "STE" by GE) caused the reed to abruptly stop vibrating which would cause the receive audio to instantly mute. Initially, a phase shift of 180 degrees was used, but experience showed that a shift of ±120 to 135 degrees was optimal in halting the mechanical reeds. These systems often have audio muting logic set for CTCSS only. If a transmitter without the phase reversal feature is used, the squelch can remain unmuted for as long as the reed continues to vibrate—up to 1.5 seconds at the end of a transmission as it coasts to a stop (sometimes referred to as the "flywheel effect" or called "freewheeling").

### Interference and CTCSS

In non-critical uses, CTCSS can also be used to hide the presence of interfering signals such as receiver-produced intermodulation. Receivers with poor specifications—such as scanners or low-cost mobile radios—cannot reject the strong signals present in urban environments. The interference will still be present and may block the receiver, but the decoder will prevent it from being heard. It will still degrade system performance but the user will not have to hear the noises produced by receiving the interference.

CTCSS is commonly used in VHF and UHF [amateur radio](Amateur%20radio.md) operations for this purpose. Wideband and extremely sensitive radios are common in the amateur radio field, which imposes limits on achievable intermodulation and adjacent-channel performance.

[Family Radio Service](Family%20Radio%20Service.md) (FRS), [PMR446](PMR446.md) and other consumer-grade radios often include a CTCSS feature called "CTCSS tones", "PL tones", or "sub-audible tones". These do not afford privacy or security, but serve only to reduce annoying interference by other users or other noise sources; a receiver with the tone squelch turned off will hear everything on the channel. GMRS/FRS radios offering CTCSS codes typically provide a choice of 38 tones, but the tone number and the tone frequencies used may vary from one manufacturer to another (or even within product lines of one manufacturer) and should not be assumed to be consistent (i.e. "Tone 12" in one set of radios may not be "Tone 12" in another).

---

*Source: Wikipedia, Continuous Tone-Coded Squelch System (https://en.wikipedia.org/wiki/Continuous_Tone-Coded_Squelch_System), by Wikipedia contributors, CC BY-SA 4.0.*
