# Maximum legal QRQ CW speed?

*Tags: united-states, legal, cw, bandwidth · score 3*

## Question

Computer generated and decoded Morse Code seems to be a not-uncommon operating practice in the HF bands. Given this, and that there's no reason why Morse/CW signals can't be synthesized and decoded at at many 100s or even 1000s of WPM (perhaps with Gaussian pulse shaping at the higher rates), is there a maximum legal (in the U.S.) CW/Morse QRQ WPM in the HF bands? How about even higher WPM rates in the higher amateur UHF bands? (10e6 WPM?)

Or does CW plausibly have to be human copiable?

Also, does QRQ CW require the operator to slow down to 20 WPM every 10 minutes to ID?

## Accepted answer (score 4, by Glen Ellis K4KKQ)

I have noticed that hams using CW, PSK31, RTTY, etc, use different equations to describe their bandwidth requirements.  
Over the years, I have used an equation which combines the "k" and the "baud" and the "freq shift" : BW = (k) (baud) (delta freq) . This has worked well with various forms of pulse signals, and matches spectragraph samples of RF signals.

(1) "k" is the squareness shape from 1 (sine) to above 10 (requires much odd harmonic energy to produce a very 'square' shaped waveform ). Sharply shaped Squared CW pulses require much Odd Harmonics energy and this produce sideband 'splatter' for CW pulses.

(2) "baud" is the repitition rate, the number of square pulses produced per second. The more square pulses per second, the more 'sideband' required.

(3) "freq shift" related directly to the FSK signals of PSK31 and RTTY. Here we should note that even a Pierce crystal oscillator has 'jitter' of 3 to 10 Hz, but this is so close to zero shift that we notate it as "1".

Thus, my personal CW bandwidth is calculated at BW= (3) (15) (1) = 45 Hz. Speeds of a K=10 squared signal at 360 wpm would be BW= (10) (360) (1) = 3600 Hz. We should note that at higher speeds, the 'ear' requires a crisper defined wave-form in order to be 'heard'. A soft ( K=1.2 as per PSK31 ) CW waveform would require a slower wpm rate. A harder ( K=5 ) CW waveform would be intelligible at 25 wpm. A harder ( K=7 ) CW waveform would be intelligible at 45 wpm.

Using a SDR approach and DSP, software phase-locked loop algorithms, a computer could 'copy' CW at very high speeds, but might also require some clocking signals. PSK31 has clocking markers embedded in the waveform design ( this is the +/- shift of 15.25 Hz between elements. ) The JT65, et al, also rely on inherent clock signals, either for reasons of speed in decoding or in identifying a weak signal below noise level.

Still, to the question at hand, Faster Speeds require More Band-Width, and there are good equation descriptors of this electrical phenomenom.

I have calculated this for PSK31 hams and inspected RF spectrographs , and it fits well. PSK31 at a K= 1.2 always occupies a BW of 67 Hz, measured -27dB down (per FCC).

Same goes for RTTY, where the FreqShift is d=200 or d=1200 ( depending on your country and operating system. ) In RTTY, the delta(F) swamps the other factors.

So, with regards to CW band-width restrictions, we can , in general , see that high speed and squared-wave-shape can possibly require a potentially illegal bandwidth.  
The suggested limit of 360 wpm fits in this equations description.

These are generalizations, based on my engineering and personal experience, and 62 years of CW experience. Please note the Caveat " Y M M V " [ Your Milage May Vary ] always applies when evaluating our own experiences. We do NOT invite a casual debate on the issues of CW pulse shape and human 'hearing' in this forum, at least NOT with me.

Note: Mike Waters has some good insight into the electrical requirements of producing a 'clear' CW signal. My first experience 'hearing' fast CW was ... In our Navy Ham Club, N.A.S. Norfolk, 1957, our chiefs from WWII operated CW at 65 wpm !!! You have not heard "real CW" until you have listened in awe as real Navy CW ops play ball at high speed ! Bugs & head-copy & a rattling mill ... ... amazing. Just imaagine how very short the 'dit' signal was, and imagine just how much 'crispness' that 'dit' must have to be 'heard' ! My 'dit' length is about 18 mS at 17wpm, and would be about 4 mS at 65 wpm. At 65wpm, the RF bandwidth could be more than 320 Hz at -27 dB (FCC).

Good luck with your discussions, I am going back to listening to CW on 20M and see who is up today !  
Glen Ellis, K4KKQ ( see QRZ.com )

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16252/maximum-legal-qrq-cw-speed, by hotpaw2, Glen Ellis K4KKQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
