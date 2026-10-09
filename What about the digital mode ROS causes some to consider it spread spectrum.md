# What about the digital mode ROS causes some to consider it spread spectrum?

*Tags: united-states, legal, modes, digital-modes · score 5*

## Question

The FCC disallows amateur spread spectrum communications below 220MHz. At the moment the relatively new digital mode, ROS, is considered, by some, to be spread spectrum. So this mode is getting little to no use in the US.

It doesn't seem much different than other tone digital modes though, and never claims a bandwidth larger than phone.

What is the definition of "spread spectrum" according to the FCC?

In what ways could ROS be considered spread spectrum?

What about ROS suggests that it's not spread spectrum?

The only page on ROS I've been able to find, http://rosmodem.wordpress.com/ , doesn't seem to have an in-depth explanation of what the mode is and does.

## Accepted answer (score 5, by WPrecht)

Some consider ROS Modem Spread Spectrum because of statements on the author's website call it: Frequency Hopping Spread Spectrum. It's worth noting that the author is European and in Europe, spread spectrum is allow on the HF bands. Undoubtedly, part of this is marketing. Describing a new mode as Spread Spectrum gives it a more techy feel and spread spectrum is something that came out of the military, further increasing the cool factor.

The FCC's definition of Spread Spectrum:

Spread spectrum techniques are emissions that use bandwidth-expansion modulation >techniques to intentionally spread the information transmitted over a wide bandwidth. At any frequency in the frequency segment or bandwidth the SS emission occupies, either the spectral power density of the transmitted signal is reduced to a comparatively low level or the duration of the transmitted signal is very brief.

Source: *WT Docket No. 10-62* **RM-11325** *REPORT AND ORDER*  
Adopted: February 22, 2011 Released: March 4, 2011

The FCC's ruling on the matter simply reaffirms what SS is and where it's allowed. They didn't rule that ROS *is* SS or not. This probably has more to do with conflicting information and lack of clear guidance. The author calls it SS, but examining the actual protocol reveals that it's not. It's not very popular in the US (largely due to this conflict) and so the FCC didn't have the number of opinions it usually gets when considering a ruling.

To lump the remaining two questions together:

It's not spread spectrum; it doesn’t hop the VFO frequency. It is simply FSKs according to a programmable algorithm, and it meets the infamous 1kHz shift 300 baud rule (FCC §97.307(f)3):

Only a RTTY or data emission using a specified digital code listed in §97.309(a) of this part may be transmitted. The symbol rate must not exceed 300 bauds, or for frequency-shift keying, the frequency shift between mark and space must not exceed 1 kHz.

Digging into it further, ROS uses multiple tones over either a 2kHz or 500Hz bandwidth, (the frequencies for each mode/bandwidth are hard coded in the software). According to the rather thin documentation, ROS has three main speeds, 16 baud, 8 baud and 4 baud. There are some special modes, such as 7bd/100Hz for 136 and 502kHz (and 80m for some reason), plus an ‘EME’ mode for use on 2m and some other bands, for weak signal work as it has, in theory at least, the capability to decode signals that have a Signal to Noise Ratio (SNR) of -35dB, which is even lower than WSPR.

## Answer (score 2, by Andy K3UK)

FYI, several years ago I emailed a person at the FCC about this question. I forgot her name but she was the person that replaced Riley Hollinsworth. She replied and said clearly to me that she considered it illegal. She did not say that the FCC considered it SS and officially declared it illegal, she simply said that the author of ROS said it was SS, and therfore she was taking him at his word, and therefor it is illegal. I think she is wrong, but you will really have to convince me this mode is SO GOOD that the benefits of using it outweigh the risks.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1105/what-about-the-digital-mode-ros-causes-some-to-consider-it-spread-spectrum, by Adam Davis, WPrecht, Andy K3UK. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
