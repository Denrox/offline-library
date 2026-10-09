# WSPR RX dial frequency

*Tags: ssb, wspr, tecsun · score 3*

## Question

I tried but failed to decode WSPR using Tecsun PL-600 receiver that tunes in 1KHz step. I heard tones with good SNR but cannot be decoded. So, I mis-set it somewhere.

1.

Is it correct that transmission is around 10.140200MHz, with a few Hz bandwidth?

2.

What are the four symbol RF frequencies? I seem to read documentation saying that they are 10.140200 + (0_to_3 x 1.4648Hz). I observed WSPR sound card output, using Spectrum Lab software, and they are spreading from 1497 to 1503 Hz, instead of 1500 to 1506Hz. Where did I miss?

3.

On a 'normal' receiver, should I set the receiver frequency to 10.138700MHz, get audio at 1500Hz and WSPR software will auto search and decode signal around 1500Hz?

4.

On my receiver, is it correct that audio will be 1200 and 2200Hz, when dialed to 10.138 or 10.139MHz? Will WSPR software auto search to 1200 and 2200Hz? If not, can I set it in the software? Or, I should vary BFO to make it "back to" 1500Hz?

5.

Are the below tabled calculation of LO and BFO, etc correct?

6.

The receiver only have setting of AM/SSB. It does not have separate setting for USB and LSB. It has a BFO knob with a 'central click" which got a good zero beat for 10MHz time signal.

To get effective USB mode, I believe I should turn it "away from the central click" in order to set BFO to 453.5KHz, right?

1. If I turn the BFO knob to the "wrong" direction, setting BFO to 456.5KHz, resulting in LSB mode, I will hear similar signal tone, but, the 4 symbols are in "up side down frequency order" and cannot be decoded. Are these right?

## Answer (score 2, by rclocher3)

I'm neither an electrical engineer nor a software-defined radio expert, but I have used WSPR, so I'll have a go at answering your question.

You're correct that WSPR transmissions on 30m are centered around 10.1402 MHz, but the WSPR 2.0 User's Guide says that the passband is about 200 Hz wide since the software will generate tones between 1400 and 1600 Hz, and transceiver frequency drift can add to that. The screen shots in the User's Guide show a passband of slightly more than 200 Hz wide (see the scale at the right of the waterfall).

Most ham radio software for digital modes shows signals in the entire passband sent by the radio, typically 2.7 kHz wide or so, but K1JT's software decodes a much smaller passband, probably with the intention of keeping WSPR signals confined to a small part of the band since there is no need to use a larger passband.

I had a look at the manual for your Tecsun PL-600, which is quite vague about SSB reception. I think you're probably right about turning the BFO knob one way for USB and the other way for LSB. If I were in your situation I would test that theory by tuning the radio to the ham 20m band (14.225 to 14.350 MHz in the US), where USB is the norm, and also to the ham 40m band (7.175 to 7.300 MHz) where LSB is common. Tuning SSB signals in those two bands will tell you how the BFO knob works, and which way you twist for USB and which way for LSB.

I would suggest that you try W1JT's software before trying that Spectrum Lab software. If you can successfully decode signals with W1JT's software then you will know that your radio is tuned correctly, that the incoming signal voltage levels are correct, and so on.

Please keep in mind also that signals from the headphone jack of the radio are at about line level (~ 1 V), but the input level of the sound card in your computer may be at microphone level (millivolts). If that is the case, then an attenuator is necessary between the radio and the computer. Some sound cards have a line-level input, in which case an attenuator may not be necessary. For more details about such an attenuator, do a web search for "ham radio sound card interface". Sometimes galvanic isolation (a transformer) is required in the sound card interface in order to prevent ground loop problems.

Good luck, and let us know in a comment how things go!

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6342/wspr-rx-dial-frequency, by EEd, rclocher3. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
