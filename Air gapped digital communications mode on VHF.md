# Air gapped digital communications mode on VHF?

*Tags: united-states, digital-modes, cw, modes · score 5*

## Question

According to [this question](Is%20Morse%20code%20allowed%20on%20FM%20in%20the%20USA.md) MCW (modulated continuous wave) is allowed on large portions of the VHF bands in the U.S.

Is using MCW suitable for passing small amounts of digital data between 2 PCs or mobile phones using just air-gapped audio (speaker and mic, no wired connections or acoustic couplers) with generic handheld VHF HT radios? Are there other standard modes more suitable for this purpose?

If using MCW, what encoding methods (arbitrary digital data to hex characters in Morse Code?) might be legal in the U.S.?

## Answer (score 5, by Phil Frost - W8II)

Suitable, I suppose, though not especially efficient in terms of spectrum or power. Morse code was never really designed for machine demodulation, so unless you also need the ability to decode by ear, Morse code isn't a great choice.

The 1200 baud FSK modes used for packet and APRS are something to consider. Normal use involves hooking a PC to the radio's audio input or output via a cable. If you add a speaker and microphone of good fidelity in between it continues to work.

If the fidelity isn't so great, or it's noisy, you can slow down the baud rate. "Packet" goes down to 300 baud, but if you want FSK slower than that, look at RTTY.

Mobile phones in particular present a challenge because the compression they employ is optimized for human voice, and introduces a ton of distortion otherwise. But a sufficiently slow FSK modulation should work fine, and at least as good as morse code.

## Answer (score 3, by Edwin van Mierlo)

To add to the answer already given:

This would require some experimentation, but you could run an audio modem on each of the computers (one sender, one receiver) then TX/RX the audio from A to B.

An example of such audio modem is here

First test is to take the two computes side by side, line up speaker of sender to mic of receiver, and test such package over a simple air-gap without any TX/RX, the following from the documentation:

Calibration

Connect the audio cable between the sender and the receiver, and run the following scripts:

On the sender's side:

```
~/sender $ export BITRATE=48  # explicitly select high MODEM bit rate (assuming good SNR).
~/sender $ amodem send --calibrate

```

On thereceiver's side:

```
~/receiver $ export BITRATE=48  # explicitly select high MODEM bitrate (assuming good SNR).
~/receiver $ amodem recv --calibrate

```

If BITRATE is not set, the MODEM will use 1 kbps settings (single frequency with BPSK modulation).

Change the sender computer's output audio level, until all frequencies are received well:

```
3000 Hz: good signal
4000 Hz: good signal
5000 Hz: good signal
6000 Hz: good signal
7000 Hz: good signal
8000 Hz: good signal
9000 Hz: good signal
10000 Hz: good signal

```

Various test modes of this mentioned software exists, to test for SNR, example:

```
2015-02-06 18:12:48,198 DEBUG      Prefix OK
2015-02-06 18:12:48,866 DEBUG        3.0 kHz: SNR = 34.82 dB
2015-02-06 18:12:48,866 DEBUG        4.0 kHz: SNR = 36.39 dB
2015-02-06 18:12:48,867 DEBUG        5.0 kHz: SNR = 37.88 dB
2015-02-06 18:12:48,867 DEBUG        6.0 kHz: SNR = 38.58 dB
2015-02-06 18:12:48,867 DEBUG        7.0 kHz: SNR = 38.86 dB
2015-02-06 18:12:48,867 DEBUG        8.0 kHz: SNR = 38.63 dB
2015-02-06 18:12:48,867 DEBUG        9.0 kHz: SNR = 38.07 dB
2015-02-06 18:12:48,868 DEBUG       10.0 kHz: SNR = 37.22 dB

```

You can test without TX/RX, then add this in once the you are sucsesfully transferring info over the air-gap.

HTH, Edwin.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6736/air-gapped-digital-communications-mode-on-vhf, by hotpaw2, Phil Frost - W8II, Edwin van Mierlo. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
