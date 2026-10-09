# 2m or 70cm FM mobile radio for digital mode operation

*Tags: digital-modes, vhf, uhf · score 9*

## Question

Are there any 2m and/or 440cm FM mobile radios that have audio inputs for supporting digital modes, like PSK31 or SSTV?

I have a Rigblaster that I use with my HF radio so I could get a mike cable and connect it directly to the mike input in the same way, but is there any VHF/UHF radio available that has better options for connectivity for working digital modes on VHF/UHF?

## Accepted answer (score 11, by oh7lzb)

**Most modern VHF/UHF FM mobile rigs designed for Amateur Radio use have a "data" connector on the back.** Currently manufactured dual-band examples include Yaesu FT-7900, Kenwood TM-V71, Icom IC-208H - they all have the same 6-pin mini-DIN "data" connector using the same main pinout.

The 6-pin data connector is originally designed for attaching packet radio TNCs and other data equipment, and usually has at least the following pins:

- Ground
- TX audio in (transmitted audio)
- PTT (ground to transmit)
- RX audio out, "1200 bit/s" "normal audio"
- RX audio out, "9600 bit/s" discriminator output

I quoted the bit rates, since the radio documentation often cites these standard packet radio speeds, although in reality it's just audio, and the radio doesn't really care about any bit rates as such. The "9600" pin audio output is taken before audio filter/amplifier stages of the radio, and has a flatter audio frequency response that is good for high speed data such as 9600 bit/s packet or AIS reception.

**Technically, you can run SSTV or PSK31 over FM, and that "data" connector will suit that purpose perfectly.** But it's not overly popular in most areas, so you might have to talk some friends to play with it. Most of SSTV and PSK31 activity is on HF SSB, although VHF/UHF digital chat as such should be a lot of fun.

PSK31 over FM in particular is quite strange and unusual, since PSK31 is designed to be a very narrow-bandwidth (31.25 Hz) mode for SSB transceivers, and transmitting it over FM (some 20 KHz) would be a waste of perfectly good radio spectrum and transmitter power. It works, but it's not efficient. Then again, it might be fun, and **if** you live in an area where most of 70cm is almost completely quiet and inactive (like I do), a little inefficiency on an irregular basis is not going to do harm, if you're having fun. A lot of amateur FM voice communications don't have a lot of useful information content, either.

SSTV isn't so narrow (about 3 kHz), and there have been more or less official FM channel allocations for it. Some US web sites cite VHF/UHF SSTV AFSK FM calling frequencies. IARU Region 1 (Europe) SSTV(FM/AFSK) frequency for 70 cm is currently 433.400.

I also often use the "data" connector of my FT-7800 for recording received voice communications on a computer. Works fine.

## Answer (score 8, by Dan KD2EE)

Sure, most radios have the ability to patch in audio. If it isn't through the front microphone connector, it's through an accessory connector, which is available on every commercial radio I'm aware of - although perhaps only on a few amateur mobiles.

But why would you want to? **SSTV and PSK31 cannot be reasonably transmitted over FM.** FM transmits a carrier at a single frequency that is modulated. That is not the same as the SSB that is used in HF transceivers for digital mode operation - it's a **completely different kind of modulation**. In SSB, the bandwidth actually occupied by the output signal is equal to the bandwith occupied by the input signal - so if your input audio shifts by 31.25Hz, your output RF shifts by 31.25Hz. In FM, **every** input signal uses up the **entire** channel width. You couldn't use something like fldigi to receive multiple PSK31 signals in the same FM channel at once, because your FM receiver is **physically incapable** of receiving and demodulating more than one signal at a time. You would effectively be taking up an entire FM channel but only using **less than one percent** of it. SSTV operates in a similar way. The properties of FM do not allow for use of digital modes in the same way as SSB does.

If you want to use digital in VHF/UHF, you need either an SSB transceiver (might be available for 2 meters?) or a digital radio (using D-STAR, TRBO, or something else) or an SDR (a software defined radio may allow the necessary types of operation).

There are a few modes that sacrifice radio efficiency in exchange for simplicity, such as APRS, however APRS has much shorter transmit durations than PSK31 allowing for the frequency to be shared (I've seen operators with an active PSK31 signal for over a minute, imagine the APRS pileup if every station in range was forced to wait that long for an open carrier). The root of the difference is that PSK31 - very small bandwidth but very slow - was designed for Frequency Division Multiple Access (**FDMA**), while APRS was designed for Time Division Multiple Access (**TDMA**) all on the same frequency.

If you'll excuse a few signal processing terms, SSB as a modulation scheme is a **linear function** - that means that adding two audio signals together and passing it through SSB results in the same thing as if the audio signals had been encoded individually - whereas FM is not. This interesting property of SSB is what makes it possible to receive more than one signal at once. Linear modulation schemes like SSB preserve FDMA as well as TDMA, however nonlinear modulation schemes like FM preserve only TDMA, and not FDMA.

References:

- Why PSK31 over FM is nonsense
- "FM only...is NOT a popular PSK mode
- ["PSK31 would [lose] most of its benefits if run thru an FM system. Certainly it would no longer be narrow band. PSK31 via a 2M SSB system would be a good weak signal mode.](http://webcache.googleusercontent.com/search?q=cache%3aF1fuZMQBKKIJ%3awww.eham.net/ehamforum/smf/index.php%3Ftopic%3D13984.0+&cd=2&hl=en&ct=clnk&gl=us)
- ["Using PSK31 over FM results in [losing] most of the benefits of PSK31. You are still transmitting a wide FM signal and the threshold needed by the FM receiver still requires the same signal level as voice FM.](http://webcache.googleusercontent.com/search?q=cache%3aYsjTS4NJRQwJ%3awww.eham.net/ehamforum/smf/index.php%3Ftopic%3D26178.0+&cd=3&hl=en&ct=clnk&gl=us)
- "on FM? It would defeat the purpose of PSK31."

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/464/2m-or-70cm-fm-mobile-radio-for-digital-mode-operation, by Kevin Hooke KK6DCT, oh7lzb, Dan KD2EE. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
